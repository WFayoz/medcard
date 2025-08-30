from starlette_admin.contrib.sqla import ModelView

from app.models import Clinic


class ClinicAdmin(ModelView):
    model = Clinic
    exclude_fields_from_create = ["id", "created_at", "updated_at"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at"]

