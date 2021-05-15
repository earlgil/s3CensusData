
from dotenv import load_dotenv

load_dotenv()

import boto3
import os
####



client = boto3.client('s3', aws_access_key_id = os.getenv("access_key"), aws_secret_access_key = os.getenv("secret_access_key"))


for file in os.listdir():
    if 'cb_2018' in file:
        upload_file_bucket = 's3bucketcensus'
        upload_file_key = 'cbdata/' + str(file)
        client.upload_file(file, upload_file_bucket, upload_file_key)

