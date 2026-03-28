import boto3
import os
from src.constants import CONFIG

class S3Client:
    s3_client=None
    s3_resource = None
    def __init__(self, region_name=CONFIG.REGION_NAME):
        """ 
        Description: This Class gets aws credentials from env_variable and creates an connection with s3 bucket 
        and raise exception when environment variable is not set.

        Args:
            regoin_name (str): Region Name
        """

        if S3Client.s3_resource==None or S3Client.s3_client==None:
            __access_key_id = CONFIG.AWS_ACCESS_KEY_ID.get_secret_value()
            __secret_access_key = CONFIG.AWS_SECRET_ACCESS_KEY.get_secret_value()
            if __access_key_id is None:
                raise Exception(f"Environment variable: {CONFIG.AWS_ACCESS_KEY_ID.get_secret_value()} is not not set.")
            if __secret_access_key is None:
                raise Exception(f"Environment variable: {CONFIG.AWS_SECRET_ACCESS_KEY.get_secret_value()} is not set.")
        
            S3Client.s3_resource = boto3.resource('s3',
                                            aws_access_key_id=__access_key_id,
                                            aws_secret_access_key=__secret_access_key,
                                            region_name=region_name
                                            )
            S3Client.s3_client = boto3.client('s3',
                                        aws_access_key_id=__access_key_id,
                                        aws_secret_access_key=__secret_access_key,
                                        region_name=region_name
                                        )
        self.s3_resource = S3Client.s3_resource
        self.s3_client = S3Client.s3_client