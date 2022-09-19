import boto3
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')
import os

def lambda_handler(event, context):
    bucket =s3.Bucket('hk123bucket333')
    files = list(bucket.objects.all())

    # for file in files:
    #     response = s3_client.download_file("hk123bucket333", file.key, file.key)
    for file in files:
        print('-------file name-----')
        print (file, '\n--------------')
        bucket='hk123bucket333'
        key =str(file.key)
        local_file_name = os.chdir("data") +key #local_file_name = '/tmp/' + key (this is working)
        s3_client.download_file(Bucket=bucket, Key=key, Filename=local_file_name)

    # response = {
    #     "statusCode": 200,
    #     "body": files
    # }

    # return response