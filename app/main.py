from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette_admin.contrib.sqla import Admin
from admin.models import ClinicAdmin
from app.models import Clinic
from app.models.base_model import db


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # await db.create_all()
    print('project ishga tushdi')
    yield
    # await db.drop_all()
    print('project toxtadi')


app = FastAPI(docs_url='/', root_path='/api', title="MedCard", lifespan=lifespan)
admin = Admin(engine=db.engine, title='Clinics Administration')

admin.add_view(ClinicAdmin(Clinic))
admin.mount_to(app)