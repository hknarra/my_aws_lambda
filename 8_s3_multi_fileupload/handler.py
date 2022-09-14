# 
import boto3
s3 = boto3.client('s3')

import glob
files = glob.glob('data/*')

def lambda_handler(file_name, bucket, object_name=None, args=None):
    '''
    file_name = file name in local
    bucket = bucket name
    object_name = name of file in S3 bucket
    args: Custom args
    '''

    if object_name is None:
        object_name = file_name

    response = s3.upload_file(file_name, bucket, object_name, ExtraArgs = args)
    print(response)



# Use fucntion to uplaod files
for file in files:
    lambda_handler(file, 'hk123bucket333')
    print('uploaded files is :', file)