from app.models import Base
from app.config import engine

def init_db():
    Base.metadata.create_all(bind=engine)