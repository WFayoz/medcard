from starlette_admin.contrib.sqla import ModelView

from app.models import User


class DoctorModelView(ModelView):
    model = User
    name = 'doctor'
    label = 'doctor'

    identity = 'user'

    exclude_fields_from_list = ['id', 'created_at', 'updated_at']


class PatientModelView(ModelView):
    model = User
    name = 'doctor'
    label = 'patient'

    identity = 'user'

    exclude_fields_from_list = ['id', 'created_at', 'updated_at']
