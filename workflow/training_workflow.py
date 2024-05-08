from upload.minio import MinioMiddleware
from upload.types.hyperparameters import HyperParameters

minio = MinioMiddleware()

# default_hyperparameters = HyperParameters()

# minio.upload_hyperparameters(hyperparameters=default_hyperparameters)