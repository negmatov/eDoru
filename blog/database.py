from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://u0946_pharm:6M_0fym5@31.31.198.209/u0946565_pharmdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL, encoding='utf-8', echo=True)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, )

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
