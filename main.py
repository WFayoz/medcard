from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.admin import admin
from app.models.base_model import db


@asynccontextmanager
async def lifespan(_app: FastAPI):
    await db.create_all()
    print('project ishga tushdi')
    admin.mount_to(app)

    yield
    # await db.drop_all()
    print('project toxtadi')


app = FastAPI(docs_url='/', title="MedCard", lifespan=lifespan)


# TODO router qoshish
# TODO api/v1/clinics GET (client)
# TODO api/v1/clinics POST (admin)


# adminka, client web
