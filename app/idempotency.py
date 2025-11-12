from app.models import IdempotencyKey
from app.config import SessionLocal

def is_duplicate(key: str) -> bool:
    session = SessionLocal()
    exists = session.query(IdempotencyKey).filter_by(key=key).first()
    session.close()
    return exists is not None

def store_key(key: str):
    session = SessionLocal()
    session.add(IdempotencyKey(key=key))
    session.commit()
    session.close()

