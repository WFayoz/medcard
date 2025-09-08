from starlette_admin.contrib.sqla import ModelView

from app.models import User


class UserAdmin(ModelView):
    model = User
    identity = 'user'

    exclude_fields_from_list = ['id', 'created_at', 'updated_at']
