import os

from gloe import If
from gloe.utils import debug

from pipelines.transformers.training import create_sagemaker_temp_files, check_if_metadata_is_available
from pipelines.utils.docker.server import DockerClientServer
from pipelines.transformers.general import image_tag_has_running_container, images_tags_has_some_running_container, \
    echo, forward_condition
from pipelines.types_built.hyperparameters import HyperParameters
from pipelines.types_built.model_metadata import ModelMetadata
from dotenv import load_dotenv

from pipelines.utils.minio.server import MinioMiddleware

load_dotenv()

docker_client = DockerClientServer.get_instance()
minio = MinioMiddleware()

hyperparameters = HyperParameters()
model_metadata = ModelMetadata()

sagemaker_tag = os.getenv('SAGEMAKER_IMAGE_REPOTAG')
robomaker_tag = os.getenv('ROBOMAKER_IMAGE_REPOTAG')


# upload_hyper_res = minio.upload_hyperparameters(hyperparameters=hyperparameters)
# print(upload_hyper_res)
#
# upload_metadata_res = minio.upload_metadata(model_metadata=model_metadata)
#
# print(upload_metadata_res)
#
# upload_reward = minio.upload_reward_function()
# print(upload_reward)

def train_pipeline(hyperparameters: HyperParameters, model_metadata: ModelMetadata):
    training_start_pipeline = (
        create_sagemaker_temp_files >>
        check_if_metadata_is_available >>
        images_tags_has_some_running_container(docker_client, [sagemaker_tag, robomaker_tag]) >>
        forward_condition
        .Then(echo("The training is running, please stop the train before starting a new one."))
        .Else(
            echo("The training is not running")
        )
    )
    training_start_pipeline(None)


train_pipeline()
