import boto3
from model import bucket_model

class create_bucket(bucket_model):
    def __init__(self):
        self.bucket_name = bucket_model.bucket_name
        self.region_name = bucket_model.region

    def bucket_create(self):
        """
        Method to create a bucket
        :return:
        """
        if self.region_name is not None:
            s3_client = boto3.client('s3', region_name=self.region_name)
            location = {'LocationConstraint': self.region_name}
            s3_client.create_bucket(Bucket=self.bucket_name,CreateBucketConfiguration=location)
            return True