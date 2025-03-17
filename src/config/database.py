from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config.settings import settings


async_engine = create_async_engine(
    url=settings.DATABASE_URL_async,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

async_session_factory = async_sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)
