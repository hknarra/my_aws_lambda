import json
import logging
import boto3
from botocore.exceptions import ClientError

def create_bucket(event, context):
    region='us-east-2'
    bucket_name='hkbucket-111-999'
    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            if (region=='us-east-2'):
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True