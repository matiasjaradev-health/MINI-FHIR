from fastapi import APIRouter, status
from fhir.resources.patient import Patient



API_ROUTER = APIRouter(
    prefix="/Patient",
    tags=["Patient"]
)


@API_ROUTER.post("/", status_code=status.HTTP_201_CREATED)
async def create_patient(patient_data: Patient):
    return patient_data


#TODO: Implementar la validación CL Core
#TODO: Implementar la inserción en MongoDB
#TODO: Implementar la obtención de un paciente por ID
#TODO: Implementar la actualización de un paciente por ID
#TODO: Implementar la eliminación de un paciente por ID
#TODO: Implementar la obtención de todos los pacientes
#TODO: Implementar la obtención de un paciente por RUN
#TODO: Implementar la obtención de un paciente por nombre
#TODO: Implementar la obtención de un paciente por apellido
#TODO: Implementar la obtención de un paciente por email
#TODO: Implementar la obtención de un paciente por teléfono