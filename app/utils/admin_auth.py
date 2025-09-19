from sqlalchemy import select
from starlette.requests import Request
from starlette.responses import Response
from starlette_admin.auth import AdminConfig, AdminUser, AuthProvider
from starlette_admin.exceptions import FormValidationError, LoginFailed

from app.models import User
from app.models.base_model import async_session_maker


class UsernameAndPasswordProvider(AuthProvider):

    async def login(
            self,
            username: str,
            password: str,
            remember_me: bool,
            request: Request,
            response: Response,
    ) -> Response:
        phone_number = username

        if len(phone_number) < 9:
            raise FormValidationError(
                {"username": "Ensure phone_number has at least 9 characters"}
            )

        user = await User.get_by_phone(phone_number)
        # TODO fix
        # async with async_session_maker() as session:
        #     result = await session.execute(
        #         select(User).where(User.phone_number == phone_number)
        #     )
        #     user = result.scalar_one_or_none()

        if not user:
            raise LoginFailed("Invalid phone_number or password")

        if not user.is_admin:
            # if user.role != User.Role.ADMIN:
            raise LoginFailed("You are not allowed to access admin panel")

        if not password == user.password:
            raise LoginFailed("Invalid phone_number or password")

        request.session.update({"phone_number": phone_number})
        request.state.user = user
        return response

    async def is_authenticated(self, request: Request) -> bool:
        phone_number = request.session.get("phone_number")
        if not phone_number:
            return False

        async with async_session_maker() as session:
            result = await session.execute(
                select(User).where(User.phone_number == phone_number)
            )
            user = result.scalar_one_or_none()

        if user:
            request.state.user = user
            return True
        return False

    def get_admin_config(self, request: Request) -> AdminConfig:
        user: User = request.state.user
        return AdminConfig(app_title=f"Hello, {user.firstname}!")

    def get_admin_user(self, request: Request) -> AdminUser:
        user: User = request.state.user
        return AdminUser(username=user.phone_number)

    async def logout(self, request: Request, response: Response) -> Response:
        request.session.clear()
        return response
