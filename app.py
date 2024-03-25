import os
import boto3

# The file download processing section should be placed here
import gdown

url='https://drive.google.com/drive/folders/1EImvKyUQ_iJCfd2h-Dxjn_sqPyDV5tFC'
gdown.download_folder(url)
# Output file will be icttm-test/data.zip

# Unzip the file
import zipfile
with zipfile.ZipFile('icttm-test/data.zip', 'r') as zip_ref:
    zip_ref.extractall('icttm-test')

#...........................................................
# Define S3 storage
obj_storage_access_key = os.getenv('OBJ_STORAGE_ACCESS_KEY', 'XpSkdzaL5NsSIe4YgHDg')
obj_storage_secret_key = os.getenv('OBJ_STORAGE_SECRET_KEY', 'jNiQdM05jn4cZIA6fBuWIjGD0UjfhsiKS3RpPL9W')
obj_storage_endpoint = os.getenv('OBJ_STORAGE_ENDPOINT', 'http://localhost:9000')

# Function to upload file to minio
def upload_file_to_minio(file_path, minio_bucket, minio_object_name):
    s3c = boto3.resource('s3',
                        endpoint_url=obj_storage_endpoint,
                        aws_access_key_id=obj_storage_access_key,
                        aws_secret_access_key=obj_storage_secret_key,
                        config=boto3.session.Config(signature_version='s3v4'),
                        verify=False
                        )
    s3c.Bucket(minio_bucket).upload_file(file_path, minio_object_name)

# Upload file to minio
upload_file_to_minio('icttm-test/data.json', 'data', 'data-raw/data.json')
upload_file_to_minio('icttm-test/data2.json', 'data', 'data-raw/data2.json')
upload_file_to_minio('icttm-test/data3.json', 'data', 'data-raw/data3.json')
