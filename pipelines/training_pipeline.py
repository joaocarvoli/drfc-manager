import os

from pipelines.utils.docker.server import DockerClientServer
from pipelines.transformers.general import image_has_running_container
from pipelines.types_built.hyperparameters import HyperParameters
from pipelines.types_built.model_metadata import ModelMetadata
from pipelines.utils.minio import MinioMiddleware
from dotenv import load_dotenv

load_dotenv()

minio = MinioMiddleware()

hyperparameters = HyperParameters()
model_metadata = ModelMetadata()
docker_client = DockerClientServer.get_instance()

minio_tag = os.getenv('MINIO_IMAGE_REPOTAG')

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


# training_start_pipeline = (
#     side_effect_no_output(create_sagemaker_temp_files)
#     # side_effect(check_if_metadata_is_available(work_directory))
# )

# training_start_pipeline()

# create_sagemaker_temp_files('/tmp/sagemaker')
# check_if_metadata_is_available(work_directory)

image_has_running_container([docker_client, minio_tag])

# find_image_id_by_name([docker_client, "minio/minio:latest"])
# check_if_image_has_container_running(tuple(docker_client, ""))
