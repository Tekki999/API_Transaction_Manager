from sqlalchemy import Column, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class IdempotencyKey(Base):
    __tablename__ = "idempotency_keys"
    key = Column(String, primary_key=True)

class TransactionLog(Base):
    __tablename__ = "transaction_logs"
    key = Column(String, primary_key=True)
    payload = Column(Text)
    result = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)