import boto3
from model import S3GetBucketRequestModel, S3BucketResponseModel, S3GetBucketModelParams, S3CreateBucketRequestModel, \
    S3ListBucketRequestModel, S3ListBucketModelParams
import random
import string
from libs.aws_actions import s3_client
import botocore


class s3_actions():

    def __init__(self, standard_params: S3GetBucketRequestModel):
        self.region_name = standard_params.region
        self.s3_client = s3_client("ap-south-1")

    def bucket_create(self, params: S3CreateBucketRequestModel):
        """
        Method to create a s3 bucket in aws
        :return:
        """
        # Creating random string to avoid duplicate S3 Buckets
        _bucket_extension = ''.join(random.choices(string.ascii_lowercase, k=6))
        _bucket_full_name = params.bucket_name + _bucket_extension

        try:
            if self.region_name is not None:
                location = {'LocationConstraint': self.region_name}
                response = self.s3_client.create_bucket(Bucket=_bucket_full_name, CreateBucketConfiguration=location)
                sc = response['ResponseMetadata']['HTTPStatusCode']
                return S3BucketResponseModel(
                    response_data={"data": response},
                    status_code=sc if sc == 200 else "400",
                    requester=params.user,
                    CRUD_method="PUT")

        except botocore.errorfactory.BucketAlreadyOwnedByYou as error:
            return S3BucketResponseModel(
                response_data={"Data": f"Bucket already exists with the same name, "
                                       f"Try Create with different name or look for this error - {error}"},
                status_code=response['ResponseMetadata']['HTTPStatusCode'],
                requester=params.user,
                CRUD_method="POST")

    def list_objects(self, params: S3GetBucketRequestModel):
        """
        Method to list Objects under the given bucket
        :return: Dic
        """
        try:
            if self.region_name is not None:
                response = self.s3_client.list_objects(Bucket=params.bucket_name)
                for _obj in response:
                    obj_list = _obj['Key']
                sc = response['ResponseMetadata']['HTTPStatusCode']
            return S3BucketResponseModel(
                response_data={"Data": obj_list},
                status_code=sc if sc == 200 else "400",
                requester=params.user,
                CRUD_method="GET")

        except botocore.errorfactory.NoSuchBucket as error:
            return S3BucketResponseModel(
                response_data={"data": error},
                status_code=response['ResponseMetadata']['HTTPStatusCode'],
                requester=params.user,
                CRUD_method="GET")

    def list_buckets(self, params: S3ListBucketRequestModel):
        try:
            bucket_list = []
            response = self.s3_client.list_buckets()
            for _buk in response['Buckets']:
                bucket_list.append(_buk["Name"])
            sc = response['ResponseMetadata']['HTTPStatusCode']
            result = {"received_data": bucket_list}
            print(f"========={result}============")

            return S3BucketResponseModel(
                response_data={"data": result},
                status_code=sc if sc == 200 else "400",
                requester=params.user,
                CRUD_method="GET")
        except Exception as error:
            return S3BucketResponseModel(
                response_data={"Data", error},
                status_code=sc if sc == 200 else "400",
                requester=params.user,
                CRUD_method="GET")

