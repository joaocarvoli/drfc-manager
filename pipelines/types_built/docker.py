from enum import Enum
from dataclasses import dataclass


@dataclass
class DockerImages(str, Enum):
    training = 'training'
    endpoint = 'endpoint'
    compose_keys = 'compose-keys'
