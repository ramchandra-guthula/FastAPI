from controller import create_bucket
from fastapi import Depends, APIRouter
router = APIRouter()

@router.post('/aws/s3/create')
async def