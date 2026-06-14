from fastapi import APIRouter, HTTPException, status
from fhir.resources.patient import Patient
from app.database import db 
from uuid import UUID

router = APIRouter(
    prefix="/Patient",
    tags=["Patient"]
)

CL_CORE_PROFILE = "https://hl7chile.cl/fhir/ig/clcore/StructureDefinition/CorePacienteCl"


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_patient(patien_data: Patient):
    result = await db["Patient"].insert_one(patien_data.model_dump())
    return {
        "message": "Paciente creado exitosamente bajo la norma CL Core",
        "fhir_id": str(result.inserted_id)
    }