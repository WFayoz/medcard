from typing import Any
from starlette.requests import Request
from starlette_admin.fields import BaseField


class OSMMapField(BaseField):
    def __init__(self, name: str = "coordinates", label: str = "Clinic Location", required: bool = False):
        super().__init__(name=name, label=label, required=required)
        self.form_template = "osm_map.html"
        self.display_template = "osm_map_display.html"

    async def parse_form_data(self, request: Request, form_data, action) -> dict[str, Any]:
        # FormData object orqali olamiz
        print("FORM DATA:", form_data)
        print("REQUEST FORM:", await request.form())
        lat = form_data.get("lat") if form_data else None
        lng = form_data.get("lng") if form_data else None
        return {
            "lat": float(lat) if lat else None,
            "lng": float(lng) if lng else None,
        }

    async def serialize_value(self, request: Request, value: Any, action) -> Any:
        if isinstance(value, dict):
            return value
        if value:
            return {"lat": getattr(value, "lat", None), "lng": getattr(value, "lng", None)}
        return None
