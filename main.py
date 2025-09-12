from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.admin import admin


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # await db.create_all()
    print('project ishga tushdi')
    admin.mount_to(app)

    yield
    # await db.drop_all()
    print('project toxtadi')


app = FastAPI(docs_url='/', title="MedCard", lifespan=lifespan)
