import os
from io import BytesIO

from gloe import If
from gloe.utils import debug, forward

from pipelines.transformers.training import create_sagemaker_temp_files, check_if_metadata_is_available, \
    upload_hyperparameters, upload_metadata, upload_reward_function
from pipelines.utils.docker.server import DockerClientServer
from pipelines.transformers.general import images_tags_has_some_running_container, \
    echo, forward_condition
from pipelines.types_built.hyperparameters import HyperParameters
from pipelines.types_built.model_metadata import ModelMetadata
from pipelines.utils.minio.server import MinioClientServer


_docker_client = DockerClientServer.get_instance()
_minio_client = MinioClientServer.get_instance()
sagemaker_tag = os.getenv('SAGEMAKER_IMAGE_REPOTAG')
robomaker_tag = os.getenv('ROBOMAKER_IMAGE_REPOTAG')


def train_pipeline(hyperparameters: HyperParameters, model_metadata: ModelMetadata, reward_function_buffer: BytesIO):
    training_start_pipeline = (
        create_sagemaker_temp_files >>
        check_if_metadata_is_available >>
        images_tags_has_some_running_container(_docker_client, [sagemaker_tag, robomaker_tag]) >>
        forward_condition
        .Then(echo("The training is running, please stop the train before starting a new one."))
        .Else(
            forward[None]() >> (
                (
                    upload_hyperparameters(_minio_client, hyperparameters),
                    upload_metadata(_minio_client, model_metadata),
                    upload_reward_function(_minio_client, reward_function_buffer)
                )
            ) >> echo('upload successfully')
        )
    )
    training_start_pipeline(None)
