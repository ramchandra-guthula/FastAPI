from controller import s3_actions
from model import S3GetBucketRequestModel, \
    S3ListBucketRequestModel, \
    S3CreateBucketRequestModel,\
    S3BucketResponseModel,\
    S3CreateBucketRequestParams,\
    S3ListBucketModelParams, \
    S3GetBucketModelParams
from fastapi import Depends, APIRouter

# Router initialize
router = APIRouter(prefix="/aws", tags=["AWS"])


@router.post('/s3/create', response_model=S3BucketResponseModel)
async def create_bucket(request_model: S3CreateBucketRequestParams = Depends(S3CreateBucketRequestParams)):
    bkt_create = s3_actions(request_model.parameters)
    return bkt_create.bucket_create(request_model.parameters)


@router.put('/s3/get_buckets', response_model=S3BucketResponseModel)
async def get_buckets(request_model: S3ListBucketModelParams = Depends(S3ListBucketModelParams)):
    return s3_actions(request_model.parameters).list_buckets(request_model.parameters)


@router.put('/s3/list_objects', response_model=S3BucketResponseModel)
async def get_s3_objects(request_model: S3ListBucketModelParams = Depends(S3ListBucketModelParams)):
    return s3_actions(request_model.parameters).list_objects(request_model.parameters)
