import sqlite3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_NAME = "database.sqlite"
# База данных
SQLALCHEMY_DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Зависимости для работы с базой данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_db():
#     conn = sqlite3.connect(DB_NAME)
#     conn.row_factory = sqlite3.Row  # Это позволяет получать данные в виде словаря
#     return conn
#
# def create_table():
#     conn = sqlite3.connect(DB_NAME)
#     cursor = conn.cursor()
#
#     cursor.execute("""
#     CREATE TABLE IF NOT EXISTS items (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )
#     """)
#
#     conn.commit()
#     conn.close()
