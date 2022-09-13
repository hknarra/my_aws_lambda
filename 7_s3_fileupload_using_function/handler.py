import json
import boto3
# s3 = boto3.client('s3')

def lambda_handler(file_name, bucket, object_name=None, args=None):
    s3 = boto3.client('s3')
    '''
    file_name = file name in local
    bucket = bucket name
    object_name = name of file in S3 bucket
    args: Custom args
    '''

    if object_name is None:
        object_name = file_name
    

    response = s3.upload_file('sample.trg', 'hk123bucket333', 'sample.trg', ExtraArgs = args)
    print(response)

