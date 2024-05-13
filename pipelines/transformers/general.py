from docker import APIClient as DockerClient
from gloe import transformer

from pipelines.utils.docker.utilities import check_if_image_has_container_running

ImageTag = str


@transformer
def image_has_running_container(_tuple: tuple[DockerClient, ImageTag]) -> bool:
    docker_client, image_tag = _tuple
    is_running = check_if_image_has_container_running(docker_client, image_tag)
    return is_running

