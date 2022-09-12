import json
import logging
import boto3
from botocore.exceptions import ClientError


def lambda_handler(bucket_name, region_name=None):

    # list s3 buckets
    try:
        if region_name is None:
            s3 = boto3.resource('s3')
            bucketlist = []
            for bucket in s3.buckets.all():
                bucketlist.append(bucket.name)
                print('1')
      
        else:
            s3 = boto3.resource('s3', region_name='us-east-1')
            location = {'LocationConstraint': 'us-east-1'}
            bucketlist = []
            for bucket in s3.buckets.all():
                bucketlist.append(bucket.name)
                print('2')
                
    except ClientError as e:
        logging.error(e)
        return False
    return {
        "statusCode": 200,
        "body": bucketlist
        }
    # print (bucketlist)
    return True