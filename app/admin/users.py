from starlette.requests import Request
from starlette_admin.contrib.sqla import ModelView
from typing import Any, List, Optional, Union, Dict, Sequence
from sqlalchemy.orm import Session
from app.models import User


class RoleFilteredAdmin(ModelView):
    role_name: User.Role = None  # subclass da role nomi belgilanadi

    async def get_list(
            self,
            request,
            session: Session,
            offset: int = 0,
            limit: Optional[int] = None,
            where: Optional[Any] = None,
            order_by: Optional[List[Any]] = None,
    ):
        query = session.query(self.model).filter(self.model.role == self.role_name)
        if where is not None:
            query = query.filter(where)
        if order_by is not None:
            query = query.order_by(*order_by)
        total = query.count()
        items = query.offset(offset).limit(limit).all()
        return items, total

    async def before_create(self, request, data, session):
        data["role"] = self.role_name
        return data

    async def before_edit(self, request, obj, data, session):
        data["role"] = self.role_name
        return data


class PatientAdmin(RoleFilteredAdmin):
    identity = "patients"
    label = "Patients"
    model = User
    role_name = User.Role.PATIENT
    exclude_fields_from_list = ["id", "created_at", "updated_at", "role", "password", "specialty"]
    exclude_fields_from_create = ["id", "created_at", "updated_at", "role", "specialty"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at", "role", "password", "specialty"]


class DoctorAdmin(RoleFilteredAdmin):
    identity = "doctors"
    label = "Doctors"
    model = User
    role_name = User.Role.DOCTOR
    exclude_fields_from_list = ["id", "created_at", "updated_at", "role", "password"]
    exclude_fields_from_create = ["id", "created_at", "updated_at", "role"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at", "role"]

    async def before_create(self, request, data, obj):
        if "specialty" in data and data["specialty"]:
            data["specialty"] = User.DoctorSpeciality[data["specialty"].upper()]
        return data

    async def before_update(self, request, data, obj):
        if "specialty" in data and data["specialty"]:
            data["specialty"] = User.DoctorSpeciality[data["specialty"].upper()]
        return data


class NurseAdmin(RoleFilteredAdmin):
    identity = "nurses"
    label = "Nurses"
    model = User
    role_name = User.Role.NURSERY
    exclude_fields_from_list = ["id", "created_at", "updated_at", "role", "specialty", "password"]
    exclude_fields_from_create = ["id", "created_at", "updated_at", "role", "specialty"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at", "role", "specialty"]


class MedOwnerAdmin(RoleFilteredAdmin):
    identity = "medowners"
    label = "Medical Owners"
    model = User
    role_name = User.Role.MED_OWNER
    exclude_fields_from_list = ["id", "created_at", "updated_at", "role", "specialty", "password"]
    exclude_fields_from_create = ["id", "created_at", "updated_at", "role", "specialty"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at", "role", "specialty"]


class AdminPanel(ModelView):
    identity = "admins"
    label = "Admins"
    # model = User
    # role_name = User.Role.ADMIN
    exclude_fields_from_list = ["id", "created_at", "updated_at", "specialty", "password"]
    exclude_fields_from_create = ["id", "created_at", "updated_at", "specialty"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at", "specialty"]

    def get_list_query(self, request: Request):
        return super().get_list_query(request).where(User.role == User.Role.ADMIN)
