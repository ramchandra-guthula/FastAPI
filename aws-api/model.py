from datetime import datetime
from pydantic import BaseModel, Field
from fastapi import Query
from typing import Optional


class S3GetBucketRequestModel(BaseModel):
    bucket_name: str = Query(...,
                             title='Bucket Name',
                             description='Give your bucket name to create or get',
                             min_length=5,
                             max_length=30)
    region: Optional[str] = Field(default='ap-south-1',
                                  title='Region where you want to create bucket or get it',
                                  min_length=9
                                  )
    user: Optional[str] = Query(...,
                                title='Requested user',
                                description='User who is requesting',
                                default="RamGuthula",
                                min_length=3,
                                max_length=20
                                )

    class Config:
        schema_extra = {
            "example": {
                'bucket_name': "sample-bucket",
                "region": "ap-south-1",
                "user": "RamGuthula"
                }
            }


class S3GetBucketModelParams(BaseModel):
    parameters: S3GetBucketRequestModel


class S3CreateBucketRequestModel(S3GetBucketRequestModel):
    created_date =  datetime


class S3CreateBucketRequestParams(BaseModel):
    parameters: S3CreateBucketRequestModel


class S3ListBucketRequestModel(BaseModel):
    region: Optional[str] = Field(
                                  default="ap-south-1",
                                  title='Region where you want to create bucket or get it',
                                  min_length=9
                                  )
    user: Optional[str] = Field(
                                title='Requested user',
                                description='User who is requesting for the record purpose',
                                default="RamGuthula",
                                min_length=3,
                                max_length=20
                                )


class S3ListBucketModelParams(BaseModel):
    parameters: S3ListBucketRequestModel


class S3BucketResponseModel(BaseModel):
    response_data: dict = Field(description="Data received from the API")
    status_code: int
    requester: str = Field(
                            title="Name of the requestor",
                            default="RamGuthula",
                            min_length=3,
                            max_length=20)
    request_date = datetime
    CRUD_method: str = Field(
        title="CRUD operation type"
    )

