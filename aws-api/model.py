from pydantic import BaseModel
from fastapi import Query
from typing import Optional


class bucket_model(BaseModel):
    bucket_name: str = Query(...,
                             title='Bucket Name',
                             description='Give your bucket name')
    region: Optional[str] = None

