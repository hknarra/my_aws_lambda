import json
import boto3


def s3_file_upload(event, context):
    # Upload a new file
    s3 = boto3.resource('s3')
    data = open('data/LTC_DB_TableCounts.trg', 'rb')
    s3.Bucket('hk123bucket333').put_object(Key='hk_poto.jpg', Body=data)


print('uploaded :')