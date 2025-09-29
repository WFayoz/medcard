from fastapi import APIRouter

from app.routers.auth import auth_router
from app.routers.clinics import clinic_router

router = APIRouter()

router.include_router(auth_router)
router.include_router(clinic_router)
