from gloe.utils import debug

from pipelines.transformers.helpers import side_effect
from pipelines.types.hyperparameters import HyperParameters
from pipelines.types.model_metadata import ModelMetadata
from upload.minio import MinioMiddleware
from transformers.training import create_sagemaker_temp_files, check_if_metadata_is_available

minio = MinioMiddleware()

hyperparameters = HyperParameters()
model_metadata = ModelMetadata()

# upload_hyper_res = minio.upload_hyperparameters(hyperparameters=hyperparameters)
# print(upload_hyper_res)
#
# upload_metadata_res = minio.upload_metadata(model_metadata=model_metadata)
#
# print(upload_metadata_res)
#
# upload_reward = minio.upload_reward_function()
# print(upload_reward)

work_directory = '/tmp/teste'


def training_pipeline():
    (
        side_effect(create_sagemaker_temp_files) >>
        debug() >>
        side_effect(check_if_metadata_is_available(work_directory))
    )
    
    
training_pipeline()
