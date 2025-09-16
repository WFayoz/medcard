from starlette_admin.contrib.sqla import ModelView
from app.models import Clinic
from app.utils.OSM import OSMMapField


class ClinicAdmin(ModelView):
    model = Clinic
    exclude_fields_from_create = ["id", "created_at", "updated_at", "branches", "lat", "lng"]
    exclude_fields_from_edit = ["id", "created_at", "updated_at", "branches", "lat", "lng"]

    fields = [
        "name",
        "description",
        "phone",
        "email",
        "website",
        "parent",
        "medowner",
        OSMMapField("coordinates", label="Select Location on Map")

    ]

    async def before_create(self, request, data, obj):
        coords = data.pop("coordinates", None)
        if coords:
            obj.lat = coords["lat"]
            obj.lng = coords["lng"]

    async def before_edit(self, request, data, obj):
        coords = data.pop("coordinates", None)
        if coords:
            obj.lat = coords["lat"]
            obj.lng = coords["lng"]
