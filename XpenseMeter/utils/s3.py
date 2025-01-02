import boto3
from botocore.exceptions import BotoCoreError, ClientError
from io import BytesIO
from XpenseMeter.core.config import settings

s3_uploads_path = "uploads/"

def init_s3():
    s3_client = boto3.client('s3', region_name=settings.AWS_REGION)
    return s3_client

def upload_file(local_file_path: str, file_name: str, s3_key_prefix: str = s3_uploads_path, bucket: str = None):
    if bucket is None:
        bucket = settings.AWS_BUCKET
    try:
        s3_client = init_s3()
        s3_key = f"{s3_key_prefix}{file_name}"
        upload_result = s3_client.upload_file(local_file_path, bucket, s3_key)
        return upload_result
    except (BotoCoreError, ClientError) as e:
        raise RuntimeError(f"Failed to upload file to S3: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

def upload_bytesio(file_buffer: BytesIO, file_name: str, s3_key_prefix: str = s3_uploads_path, bucket: str = None):
    if bucket is None:
        bucket = settings.AWS_BUCKET
    try:
        s3_client = init_s3()
        s3_key = f"{s3_key_prefix}{file_name}"
        upload_result = s3_client.upload_fileobj(file_buffer, bucket, s3_key)
        return upload_result
    except (BotoCoreError, ClientError) as e:
        raise RuntimeError(f"Failed to upload file to S3: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")
    
def get_presigned_url(file_name: str, s3_key_prefix: str = s3_uploads_path, expires_in: int = 7200, bucket: str = None):
    if bucket is None:
        bucket = settings.AWS_BUCKET
    try:
        s3_client = init_s3()
        s3_key = f"{s3_key_prefix}{file_name}"
        url = s3_client.generate_presigned_url('get_object', Params={'Bucket': bucket, 'Key': s3_key}, ExpiresIn=expires_in)
        return url
    except (BotoCoreError, ClientError) as e:
        raise RuntimeError(f"Failed to get presigned URL: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")