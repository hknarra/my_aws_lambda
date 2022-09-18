import json
import logging
import boto3
from botocore.exceptions import ClientError


def lambda_handler(bucket_name, region='us-east-2'):
    # region_name='us-easts-1'
    # list s3 buckets
    try:
        if region is None:
            print('if block \n')
            s3 = boto3.resource('s3')
            bucketlist = []
            for bucket in s3.buckets.all():
                bucketlist.append(bucket.name)
                print('1')
      
        else:
            print ('else block \n')
            s3 = boto3.resource('s3', region_name=region)
            bucketlist = []
            for bucket in s3.buckets.all():
                bucketlist.append(bucket.name)
                print('3')
                
    except ClientError as e:
        logging.error(e)
        return False
    # return {
    #     "statusCode": 200,
    #     "body": bucketlist
    #     }
    return True