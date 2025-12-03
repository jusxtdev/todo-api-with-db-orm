from fastapi import APIRouter
from app.main import app

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)
