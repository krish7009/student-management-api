from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="student_app",
    password="Student@123",  
    host="localhost",
    port=3306,
    database="student_management",
)

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False
)

class Base(DeclarativeBase):
    pass

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()
        