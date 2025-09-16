from starlette_admin.contrib.sqla import Admin

from app.admin.clincs import ClinicAdmin
from app.admin.users import UserAdmin
from app.models import Clinic, User
from app.models.base_model import db

# templates papkasini ko‘rsatamiz
admin = Admin(
    engine=db.engine,
    title="MedCard Administration",
    templates_dir="templates"   # ✅ shuni ishlatish kerak
)

admin.add_view(ClinicAdmin(Clinic))
admin.add_view(UserAdmin(User, identity="user"))
