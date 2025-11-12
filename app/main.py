from fastapi import FastAPI, Request
from app.transaction import process_transaction
from app.idempotency import is_duplicate, store_key
from app.logger import log_transaction
from app.models import TransactionLog
from app.config import SessionLocal


app = FastAPI()

@app.post("/submit")
async def submit_transaction(request: Request):
    data = await request.json()
    key = data.get("idempotency_key")
    payload = data.get("payload")

    if not key or not payload:
        return {"status": "error", "message": "Missing idempotency_key or payload"}

    if is_duplicate(key):
        return {"status": "duplicate"}

    store_key(key)
    result = await process_transaction(key, payload)
    log_transaction(key, payload, result)
    return result

@app.get("/status/{key}")
def get_transaction_status(key: str):
    session = SessionLocal()
    entry = session.query(TransactionLog).filter_by(key=key).first()
    session.close()
    if entry:
        return {
            "key": entry.key,
            "payload": entry.payload,
            "result": entry.result,
            "timestamp": entry.timestamp
        }
    return {"status": "not found"}