from pipelines.types.hyperparameters import HyperParameters
from pipelines.types.model_metadata import ModelMetadata
from upload.minio import MinioMiddleware

minio = MinioMiddleware()

hyperparameters = HyperParameters()
model_metadata = ModelMetadata()

upload_hyper_res = minio.upload_hyperparameters(hyperparameters=hyperparameters)
print(upload_hyper_res)

upload_metadata_res = minio.upload_metadata(model_metadata=model_metadata)

print(upload_metadata_res)

upload_reward = minio.upload_reward_function()
print(upload_reward)

