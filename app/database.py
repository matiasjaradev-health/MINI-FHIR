import os
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MONGO_ROOT_USER: str
    MONGO_ROOT_PASSWORD: str
    MONGO_DB_NAME: str

    # Buscamos el archivo .env una carpeta más arriba de "app/"
    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), "..", ".env"),
        extra="ignore"
    )

settings = Settings()

MONGO_DETAILS = f"mongodb://{settings.MONGO_ROOT_USER}:{settings.MONGO_ROOT_PASSWORD}@localhost:27017"

# 3. Inicializar el cliente asíncrono te amooooooooooooo muchoooooo
client = AsyncIOMotorClient(MONGO_DETAILS)

# 4. Obtener la referencia a la base de datos FHIR
# ¡Recuerda que Mongo la creará automáticamente al insertar el primer documento!
db = client[settings.MONGO_DB_NAME]

# Función utilitaria para obtener la base de datos en los endpoints
def get_database():
    return db