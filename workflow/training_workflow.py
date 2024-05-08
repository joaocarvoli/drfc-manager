from upload.minio import MinioMiddleware
from upload.types.hyperparameters import HyperParameters

minio = MinioMiddleware()

default_hyperparameters = HyperParameters()

upload_hyper_res = minio.upload_hyperparameters(hyperparameters=default_hyperparameters)
print(upload_hyper_res)
