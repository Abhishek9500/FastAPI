from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQLite database file
DATABASE_URL = "sqlite:///./users.db"

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for database models
Base = declarative_base()

# Provide a database session to FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
'''

engine: manages the connection to SQLite.

SessionLocal: creates sessions used to query or modify data.

Base: parent class for your database models.

get_db(): provides a session to an endpoint and closes it after the request.

'''