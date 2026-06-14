from fastapi import APIRouter, status
from fhir.resources.patient import Patient



API_ROUTER = APIRouter(
    prefix="/Patient",
    tags=["Patient"]
)


@API_ROUTER.post("/", status_code=status.HTTP_201_CREATED)
async def create_patient(patient_data: Patient):
    return patient_data