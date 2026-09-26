from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from .docs import create_user_docs, delete_user_docs, get_user_by_id_docs, get_users_docs, update_user_docs
from src.core.database import get_db_session
from src.users import service
from src.users.schemas import (
    UserCreate,
    UserResponse,
    UserUpdate,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    **create_user_docs,
)
async def create_user(
    data: UserCreate,
    session: AsyncSession = Depends(get_db_session),
):
    return await service.create_user(data, session)


@router.get(
    "/",
    response_model=list[UserResponse],
    **get_users_docs,
)
async def get_users(
    session: AsyncSession = Depends(get_db_session),
):
    return await service.get_users(session)


@router.get(
    "/{id}",
    response_model=UserResponse,
    **get_user_by_id_docs,
)
async def get_user_by_id(
    id: int=Path(gt=0),
    session: AsyncSession = Depends(get_db_session),
):
    return await service.get_user_by_id(id, session)


@router.put(
    "/{id}",
    response_model=UserResponse,
    **update_user_docs,
)
async def update_user(
    data: UserUpdate,
    id: int = Path(gt=0),
    session: AsyncSession = Depends(get_db_session),
):
    return await service.update_user(id, data, session)


@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    **delete_user_docs,
)
async def delete_user(
    id: int = Path(gt=0),
    session: AsyncSession = Depends(get_db_session),
):
    await service.delete_user(id, session)


