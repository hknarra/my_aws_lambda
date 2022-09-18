import json
import boto3

# create resource
s3 = boto3.client('s3')

def lambda_handler(event, context):
    s3.create_bucket(Bucket = 'my-s3-bucket-111')



