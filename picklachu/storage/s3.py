import boto3
from botocore.client import BaseClient

from picklachu.storage.base import BaseStorage


class S3(BaseStorage):
    def __init__(self, client: BaseClient, bucket: str):
        self.bucket = bucket
        self.client = client

    def persist(self, path: str, data: bytes):
        """Persist data to s3

        Args:
            path (str): S3 key
            data (bytes): data in bytes

        Returns:
            None
        """
        self.client.put_object(Bucket=self.bucket, Key=path, Body=data)

    def retrieve(self, path: str) -> bytes:
        """Retrieve data from S3

        Args:
            path (str): S3 key

        Returns:
            Retrieved data in bytes
        """
        response = self.client.get_object(Bucket=self.bucket, Key=path)
        print(response)
        return response['Body'].read()
