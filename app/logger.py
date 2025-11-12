from app.models import TransactionLog
from app.config import SessionLocal
import json

def log_transaction(key, payload, result):
    session = SessionLocal()
    entry = TransactionLog(
        key=key,
        payload=json.dumps(payload),
        result=json.dumps(result)
    )
    session.add(entry)
    session.commit()
    session.close()