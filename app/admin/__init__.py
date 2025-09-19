from starlette_admin.contrib.sqla import Admin

from app.admin.clincs import ClinicAdmin
from app.admin.users import PatientAdmin, DoctorAdmin, MedOwnerAdmin, NurseAdmin, AdminPanel
from app.models import Clinic, User
from app.models.base_model import db
from app.utils.admin_auth import UsernameAndPasswordProvider

admin = Admin(
    engine=db.engine,
    title="MedCard Administration",
    templates_dir="templates",
    auth_provider=UsernameAndPasswordProvider()
)

admin.add_view(ClinicAdmin(Clinic))
admin.add_view(PatientAdmin(User))
admin.add_view(DoctorAdmin(User))
admin.add_view(MedOwnerAdmin(User))
admin.add_view(AdminPanel(User))
admin.add_view(NurseAdmin(User))
