from starlette_admin import BaseField


class OSMMapField(BaseField):
    def __init__(self, name: str = "coordinates", label: str = "Select Location on Map", required: bool = False):
        super().__init__(name=name, label=label, required=required)
        self.form_template = "osm_map.html"
        self.display_template = None

    async def parse_form_data(self, request, form_data, action):
        lat = form_data.get("lat")
        lng = form_data.get("lng")
        return {
            "lat": float(lat) if lat else None,
            "lng": float(lng) if lng else None,
        }

    async def serialize_value(self, request, value, action):
        if value: #Clinic Object
            return {"lat": getattr(value, "lat", None), "lng": getattr(value, "lng", None)}
        return None
