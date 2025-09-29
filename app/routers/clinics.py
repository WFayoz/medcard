from fastapi import APIRouter

from app.models import Clinic
from app.schemas import ResponseSchema, ReadClinic
from fastapi import Query

from app.schemas.clinics import ClinicPagination

clinic_router = APIRouter(tags=["clinics"])


@clinic_router.get("/clinics")
async def get_clinics(
        page: int = Query(1, ge=1),
        size: int = Query(10, ge=1, le=100),
):
    clinics, total = await Clinic.paginate(page=page, size=size)

    return ResponseSchema[ClinicPagination](
        message="all clinics",
        data=ClinicPagination(
            total=total,
            page=page,
            size=size,
            items=clinics,
        ),
    )

@clinic_router.get("/clinics/search")
async def search_clinics(name: str):
    clinics = await Clinic.filter(Clinic.name.ilike(f"%{name}%"))
    return ResponseSchema[list[ReadClinic]](
        message=f"clinics matching '{name}'",
        data=clinics
    )
