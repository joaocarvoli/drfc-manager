from typing import List

from docker import APIClient as DockerClient
from gloe import partial_transformer, condition

from drfc_manager.transformers.exceptions.base import BaseExceptionTransformers
from drfc_manager.types_built.docker import DockerImages
from drfc_manager.utils.commands.docker_compose import DockerComposeCommands
from drfc_manager.utils.docker.utilities import check_if_image_has_container_running
from drfc_manager.utils.minio.utilities import check_if_object_exists as _check_if_object_exists

from minio import Minio as MinioClient
from minio.error import MinioException

ImageTag = str

docker_compose = DockerComposeCommands()


@partial_transformer
def image_tag_has_running_container(_, docker_client: DockerClient, image_tag: str) -> bool:
    is_running = check_if_image_has_container_running(docker_client, image_tag)
    return is_running


@partial_transformer
def images_tags_has_some_running_container(_, docker_client: DockerClient, image_tags: List[str | None]):
    is_running_containers = [check_if_image_has_container_running(docker_client, image_tag) for image_tag in image_tags]
    return any(is_running_containers)


@partial_transformer
def images_tags_has_running_container(_, docker_client: DockerClient, image_tags: List[str]):
    is_running_containers = [check_if_image_has_container_running(docker_client, image_tag) for image_tag in image_tags]
    return all(is_running_containers)


@partial_transformer
def echo(_, message: str):
    print(message)
    
    
@condition
def forward_condition(_condition: bool):
    return _condition

@partial_transformer
def check_if_model_exists(_, minio_client: MinioClient, model_name: str):
    try:
        file_to_check = '/reward_function.py'
        return _check_if_object_exists(minio_client, model_name + file_to_check)
    except MinioException as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to check if the model exists", e)


@partial_transformer
def up_composes(_, files_path: List[DockerImages]):
    docker_compose.up(files_path)
