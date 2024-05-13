import os
import io

from io import BytesIO
from minio.error import MinioException
from orjson import dumps, OPT_INDENT_2
from minio import Minio
from dotenv import load_dotenv

from pipelines.types_built.hyperparameters import HyperParameters
from pipelines.types_built.model_metadata import ModelMetadata
from pipelines.utils.minio.exceptions.file_upload_exception import FileUploadException

load_dotenv()


class MinioMiddleware:

    def __init__(self):
        access_key = os.getenv('ACCESS_KEY')
        secret_key = os.getenv('SECRET_KEY')
        endpoint = os.getenv('MINIO_SERVER_URL')
        self.bucket_name = os.getenv('BUCKET_NAME')
        self.custom_files_folder = os.getenv('CUSTOM_FILES_FOLDER_PATH')
        self.reward_function_path = os.getenv('REWARD_FUNCTION_PATH')
        self.client = Minio(endpoint, access_key, secret_key, secure=False)

    def upload_hyperparameters(self, hyperparameters: HyperParameters):
        """
        Uploads hyperparameters to an S3 bucket.

        Args:
            hyperparameters (HyperParameters): The hyperparameters to minio.

        Returns:
            bool: True if the minio was successful, False otherwise.
        """
        
        try:
            hyperparameters_serialized = dumps(hyperparameters, option=OPT_INDENT_2)
            object_size = len(hyperparameters_serialized)
            object_name = 'hyperparameters.json'
            
            result = self.client.put_object(
                self.bucket_name,
                f'{self.custom_files_folder}/{object_name}',
                io.BytesIO(hyperparameters_serialized),
                length=object_size,
                content_type="application/json"
            )
            
            return True if result else False
        except MinioException:
            raise FileUploadException(message=f'Error uploading {object_name} file to S3 bucket')
        except Exception as e:
            raise FileUploadException(original_exception=e)

    def upload_reward_function(self):
        try:
            current_dir = os.getcwd()
            file_path = os.path.join(os.path.dirname(current_dir), self.reward_function_path)
            
            with open(file_path, "rb") as fh:
                buf = BytesIO(fh.read())
            
            buffer_size = buf.getbuffer().nbytes
            object_name = 'reward_function.py'

            result = self.client.put_object(
                self.bucket_name,
                f'{self.custom_files_folder}/{object_name}',
                buf,
                length=buffer_size,
                content_type="text/plain"
            )
            
            return True if result else False
        except MinioException:
            raise FileUploadException(message=f'Error uploading {object_name}  file to S3 bucket')
        except Exception as e:
            raise FileUploadException(original_exception=e)

    def upload_metadata(self, model_metadata: ModelMetadata):
        """
        Uploads metadata to an S3 bucket.

        Args:
            model_metadata (Model Metadata): The metadata to minio.

        Returns:
            bool: True if the minio was successful, False otherwise.
        """
        
        try:
            model_metadata_serialized = dumps(model_metadata, option=OPT_INDENT_2)
            object_size = len(model_metadata_serialized)
            object_name = 'model_metadata.json'
            
            result = self.client.put_object(
                self.bucket_name,
                f'{self.custom_files_folder}/{object_name}',
                io.BytesIO(model_metadata_serialized),
                length=object_size,
                content_type="application/json"
            )
            
            return True if result else False
        except MinioException:
            raise FileUploadException(message=f'Error uploading {object_name}  file to S3 bucket')
        except Exception as e:
            raise FileUploadException(original_exception=e)
