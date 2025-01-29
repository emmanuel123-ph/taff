from fastapi import FastAPI
from app.controllers.router import api_router
from app.core.config import Config

description = """
    This is a FastAPI training program designed to help aspiring developers master web development with FastAPI. 
    The course covers building robust APIs, handling database connections, implementing authentication, and optimizing performance. 
    By the end of this training, participants will have the skills needed to become proficient FastAPI developers and build scalable, high-performance applications.
"""


app = FastAPI(
    title=Config.PROJECT_NAME,
    description=description,
    version=f"{Config.PROJECT_VERSION}",
    docs_url="/docs",  # Swagger UI accessible via /docs
    redoc_url="/redoc",  # ReDoc accessible via /redoc (facultatif)
    openapi_url="/openapi.json"  # Spécification OpenAPI accessible via /openapi.json
)

# Inclure les routes de l'API
app.include_router(api_router, prefix=Config.API_V1_STR)

@app.get("/api/")
async def root():
    return {"message": "Welcome to the formation API!"}