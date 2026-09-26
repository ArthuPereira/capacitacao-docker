from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.users.exceptions import EmailAlreadyExists, UserNotFound
from src.users.models import User
from src.users.schemas import UserCreate, UserUpdate


async def create_user(
    data: UserCreate,
    session: AsyncSession,
) -> User:
    existing_user = await session.scalar(
        select(User).where(User.email == data.email)
    )

    if existing_user:
        raise EmailAlreadyExists()

    user = User(**data.model_dump())

    session.add(user)

    await session.commit()
    await session.refresh(user)

    return user

async def get_user_by_id(
    user_id: int,
    session: AsyncSession,
) -> User | None:
    
    result = await session.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise UserNotFound()

    return user


async def get_users(session: AsyncSession) -> list[User]:
    result = await session.execute(select(User))
    
    return list(result.scalars().all())


async def update_user(
    user_id: int,
    data: UserUpdate,
    session: AsyncSession,
) -> User:
    user = await get_user_by_id(user_id, session)

    update_data = data.model_dump(exclude_unset=True)
 
    for field, value in update_data.items():
        setattr(user, field, value)

    await session.commit()
    await session.refresh(user)

    return user


async def delete_user(
    user_id: int,
    session: AsyncSession,
) -> None:
    user = await get_user_by_id(user_id, session)
 
    await session.delete(user)

    await session.commit()