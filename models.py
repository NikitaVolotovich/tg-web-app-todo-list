from sqlalchemy import ForeignKey, String, BigInteger
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from sqlachemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine("sqlite+aiosqlite:///db.sqlite3", echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    tg_id = mapped_column(BigInteger, unique=True, nullable=False)
    #username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    #email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    title: Mapped[str] = mapped_column(String(128), nullable=False)
    completed: Mapped[bool] = mapped_column(default=False)
    user: Mapped[int] = mapped_column(ForeignKey("users.id"), ondelete='CASCADE', nullable=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("Database initialized successfully.")