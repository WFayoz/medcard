from starlette_admin.contrib.sqla import Admin

from app.admin.models import ClinicAdmin
from app.models import Clinic
from app.models.base_model import db

admin = Admin(engine=db.engine, title='MedCard Administration')

admin.add_view(ClinicAdmin(Clinic))
