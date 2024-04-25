# app/main.py

from fastapi import FastAPI
from app.routes import job_application, job_posting, user

app = FastAPI()

app.include_router(job_application.router, prefix="/job_applications", tags=["job applications"])
app.include_router(job_posting.router, prefix="/job_postings", tags=["job postings"])
app.include_router(user.router, prefix="/users", tags=["users"])
