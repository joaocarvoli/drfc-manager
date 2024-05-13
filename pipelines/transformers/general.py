from typing import List

from docker import APIClient as DockerClient
from gloe import partial_transformer, condition

from pipelines.utils.docker.utilities import check_if_image_has_container_running

ImageTag = str


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
