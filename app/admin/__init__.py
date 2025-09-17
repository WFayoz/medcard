from starlette_admin.contrib.sqla import Admin

from app.admin.clincs import ClinicAdmin
from app.admin.users import PatientModelView, DoctorModelView
from app.models import Clinic, User
from app.models.base_model import db


admin = Admin(engine=db.engine, title='MedCard Administration')

admin.add_view(ClinicAdmin(Clinic))
admin.add_view(DoctorModelView(User, identity='user'))
admin.add_view(PatientModelView(User, identity='user'))
