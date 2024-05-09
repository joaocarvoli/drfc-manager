from upload.minio import MinioMiddleware
from upload.types.hyperparameters import HyperParameters
from workflow.upload.types.model_metadata import ModelMetadata
from orjson import dumps

minio = MinioMiddleware()

hyperparameters = HyperParameters()
model_metadata = ModelMetadata()

upload_hyper_res = minio.upload_hyperparameters(hyperparameters=hyperparameters)
print(upload_hyper_res)

upload_metadata_res = minio.upload_metadata(model_metadata=model_metadata)

print(upload_metadata_res)

upload_reward = minio.upload_reward_function()
print(upload_reward)

