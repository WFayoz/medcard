from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.admin import admin
from app.models.base_model import db
from app.routers import router
from app.utils.superuser import create_superuser


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.create_all()
    # await create_superuser()
    print('project ishga tushdi')
    admin.mount_to(app)

    yield
    # await db.drop_all()
    print('project toxtadi')


app = FastAPI(docs_url='/', title="MedCard", lifespan=lifespan)

app.add_middleware(SessionMiddleware, secret_key="supersecretkey")

# TODO router qoshish
# TODO api/v1/clinics GET (client)
# TODO api/v1/clinics POST (admin)
app.include_router(router)

# adminka, client web
