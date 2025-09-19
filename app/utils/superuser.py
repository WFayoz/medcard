import asyncio
from getpass import getpass

from sqlalchemy import select

from app.models import User
from app.models.base_model import async_session_maker


async def create_superuser():
    phone_number = input("Phone number: ")
    password = getpass("Password: ")

    async with async_session_maker() as session:
        # User oldin mavjudmi tekshiramiz
        result = await session.execute(select(User).where(User.phone_number == phone_number))
        existing = result.scalar_one_or_none()
        if existing:
            print("❌ User already exists")
            return

        user = User(
            phone_number=phone_number,
            firstname="superuser",
            lastname="superuser",
            password=User.get_password_hash(password),
            role=User.Role.ADMIN.name
        )
        session.add(user)
        await session.commit()
        print("✅ Superuser created!")

#
# if __name__ == "__main__":
#     asyncio.run(create_superuser())
