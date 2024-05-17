from io import BytesIO

from gloe import transformer, partial_transformer
from minio import Minio as MinioClient
from minio.error import MinioException

from drfc_manager.helpers.files_manager import create_folder, delete_files_on_folder
from drfc_manager.transformers.exceptions.base import BaseExceptionTransformers
from drfc_manager.types_built.hyperparameters import HyperParameters
from drfc_manager.types_built.model_metadata import ModelMetadata
from drfc_manager.utils.commands.docker_compose import DockerComposeCommands
from drfc_manager.utils.minio.utilities import upload_hyperparameters as _upload_hyperparameters
from drfc_manager.utils.minio.utilities import upload_reward_function as _upload_reward_function
from drfc_manager.utils.minio.utilities import upload_metadata as _upload_metadata
from drfc_manager.utils.minio.utilities import upload_local_data as _upload_local_data
from drfc_manager.types_built.docker import DockerImages
from drfc_manager.helpers.training_params import writing_on_temp_training_yml


sagemaker_temp_dir = '/tmp/sagemaker'
work_directory = '/tmp/teste'

docker_compose = DockerComposeCommands()


@transformer
def create_sagemaker_temp_files(_) -> None:
    try:
        create_folder(sagemaker_temp_dir, 0o770)
    except PermissionError as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to create the sagemaker's temp folder", e)


@transformer
def check_if_metadata_is_available(_) -> None:
    try:
        create_folder(work_directory)
        delete_files_on_folder(work_directory)
    except PermissionError as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to check if the metadata is available", e)
    
    
@partial_transformer
def upload_hyperparameters(_, minio_client: MinioClient, hyperparameters: HyperParameters):
    try:
        _upload_hyperparameters(minio_client, hyperparameters)
    except MinioException as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to upload the hyperparameters", e)
    
    
@partial_transformer
def upload_metadata(_, minio_client: MinioClient, model_metadata: ModelMetadata):
    try:
        _upload_metadata(minio_client, model_metadata)
    except MinioException as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to upload the model metadata", e)


@partial_transformer
def upload_reward_function(_, minio_client: MinioClient, reward_function_buffer: BytesIO):
    try:
        _upload_reward_function(minio_client, reward_function_buffer)
    except MinioException as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to upload the reward function", e)
    

@partial_transformer
def upload_training_params_file(_, minio_client: MinioClient, model_name: str):
    try:
        yaml_key, local_yaml_path = writing_on_temp_training_yml(model_name)
        _upload_local_data(minio_client, local_yaml_path, yaml_key)
    except MinioException as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to upload the reward function", e)
    

@transformer
def start_training(_):
    try:
        images_to_start_training = [DockerImages.training, DockerImages.keys, DockerImages.endpoint]
        docker_compose.up(images_to_start_training)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to start the training", e)


@transformer
def stop_training(_):
    try:
        images_to_stop_training = [DockerImages.training, DockerImages.keys, DockerImages.endpoint]
        docker_compose.down(images_to_stop_training)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to stop the training", e)
