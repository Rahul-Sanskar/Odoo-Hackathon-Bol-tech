from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import auth, users, skills, swaps, admin
from app.core.database import engine
from app.models import Base

app = FastAPI(title="Skill Swap Platform API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(skills.router, prefix="/api/v1/skills", tags=["skills"])
app.include_router(swaps.router, prefix="/api/v1/swaps", tags=["swaps"])
app.include_router(admin.router, prefix="/api/v1/admin", tags=["admin"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Skill Swap Platform API"}