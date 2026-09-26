from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.database import Base, engine
from src.users.router import router as users_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield


app = FastAPI(
    title="FastAPI CRUD",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(users_router)