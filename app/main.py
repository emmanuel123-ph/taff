from sched import scheduler
from fastapi import FastAPI
from fastapi.security import HTTPAuthorizationCredentials
from app.controllers.router import api_router
from app.core.config import Config
from app.core.security import decode_access_token
from app.models.db.session import SessionLocal
import os
import secrets
import time

from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.middleware.cors import CORSMiddleware
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
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)+ " s"
    return response


