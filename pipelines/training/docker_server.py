import os
from dotenv import load_dotenv
from docker import APIClient

load_dotenv()

local_docker_daemon = os.getenv('LOCAL_SERVER_DOCKER_DAEMON')
remote_docker_daemon = os.getenv("REMOTE_SERVER_DOCKER_DAEMON")
base_url = remote_docker_daemon if remote_docker_daemon is not None else local_docker_daemon

try:
    client = APIClient(base_url, use_ssh_client=True)
    containers = client.containers()
    print(containers)
except Exception as e:
    print(e)