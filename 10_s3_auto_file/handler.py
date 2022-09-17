import json
import boto3
import os
from botocore.exceptions import ClientError
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    try:
        for file in os.listdir():
            if '.csv' in file:
                file_bucket = 'hk123bucket333'
                file_key = 'csv/' + str(file)
                s3_client.upload_file(file, file_bucket, file_key)
    except ClientError as e:
        logging.error(e)
        return False
    return True



