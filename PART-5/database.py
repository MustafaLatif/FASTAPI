from  sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
DATABASE_URL ="sqlite:///./blog.db"
engine = create_engine(
    DATABASE_URL,
    connect_args={" =check_same_thread": False}
)

sessionLocal = sessionmaker(
    bind=engine,
    autocomit=False,
    autoflush=False
)

class Base(DeclarativeBase):
    pass

def get_db():
    with sessionLocal() as db:
        yield db