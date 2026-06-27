from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.config import settings

engine = create_async_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True,
    echo=False,
    pool_size=10,        # max persistent connections
    max_overflow=5,     # extra connections under high load
    pool_timeout=30,     # seconds to wait for a connection
    pool_recycle=1800,   # recycle connections every 30 mins
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass