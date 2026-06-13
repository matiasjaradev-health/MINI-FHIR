from fastapi import FastAPI

# FastAPI instance
app = FastAPI(
    title="Mini FHIR Project",
    description="A simple FHIR validator",
    version="0.1.0",
    contact={
        "name": "Matias Jara",
        "email": "matiasjaravargas987@gmail.com",
    },
    license_info={
        "name": "MIT License"
    }
)



@app.get("/fhir/metadata")
async def get_metadata():
    return {
        "resourceType": "CapabilityStatement",
        "status": "active",
        "date": "2026-06-12",
        "kind": "instance",
        "fhirVersion": "4.0.1",
        "format": ["json"],
        "rest": [{
            "mode": "server",
            "resource": [
                {"type": "Patient", "interaction": [{"code": "create"}, {"code": "validate"}]},
                {"type": "Practitioner", "interaction": [{"code": "create"}, {"code": "validate"}]}
            ]
        }]
    }