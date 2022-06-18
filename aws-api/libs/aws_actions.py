import boto3
import os
import requests
import random
import string
from dotenv import load_dotenv


def s3_client(region):
    if os.getenv('ACCESS_KEY') and os.getenv('SECRET_KEY'):
        print("Executing with Access and Secret key")
        s3_client = boto3.client('s3',
                                 aws_access_key_id=os.getenv('ACCESS_KEY'),
                                 aws_secret_access_key=os.getenv('SECRET_key'),
                                 region_name=region
                                 )
        return s3_client
    elif check_iam_role_exists() is True:
        print("Executing with IAM Role")
        s3_client = boto3.client('s3', region_name=region)
        return s3_client
    else:
        print("=============== Please use either IAM role or ACCESS or SECRET keys===============")


def check_iam_role_exists():
    req = requests.get('http://169.254.169.254/latest/meta-data/iam/security-credentials')
    if req.status_code == requests.status_codes.codes.ok:
        return True
    else:
        return False


if __name__ == "__main__":
    test = s3_client("ap-south-1")
    location = {'LocationConstraint': "ap-south-1"}
    res: object = test.create_bucket(Bucket="sample-bucket-afdeass", CreateBucketConfiguration=location)
    print(res)

    res = test.list_objects(Bucket="sample-bucket-afdeass")
    print(res)
    for i in res['Contents']:
        print(i['Key'])
    response = test.list_buckets()
    for bucket in response['Buckets']:
        print(type(bucket["Name"]))
        print(f'  {bucket["Name"]}')
    bucket_list = []
    res = test.list_buckets()
    from pprint import pprint
    [pprint(bucket_list.append(i['Name'])) for i in res['Buckets']]
    print(bucket_list)
    for _buk in res:
        bucket_list.append(_buk["Name"])
