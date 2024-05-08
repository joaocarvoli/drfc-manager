import os
import io
from orjson import dumps
from minio import Minio
from dotenv import load_dotenv
from types.hyperparameters import HyperParameters

load_dotenv()


class MinioMiddleware:

    def __init__(self):
        access_key = os.getenv('ACCESS_KEY')
        secret_key = os.getenv('SECRET_KEY')
        endpoint = os.getenv('MINIO_SERVER_URL')
        self.bucket_name = os.getenv('BUCKET_NAME')
        self.custom_files_folder = os.getenv('CUSTOM_FILES_FOLDER_PATH')
        self.client = Minio(endpoint, access_key, secret_key, secure=False)

    def upload_hyperparameters(self, hyperparameters: HyperParameters):
        hyperparameters_serialized = dumps(hyperparameters)
        object_size = len(hyperparameters_serialized)
        object_name = 'hyperparameters.json'

        result = self.client.put_object(
            self.bucket_name,
            f'{self.custom_files_folder}/{object_name}',
            io.BytesIO(hyperparameters_serialized),
            length=object_size,
            content_type="application/json"
        )
        print(dir(result))

    def upload_reward_function(self):
        pass

    def upload_metadata(self):
        pass
