import docker

class TraininingManager:
  """Class responsible for managing all training stuffs from DRfC """

  def __init__(self):
    self.client = docker.from_env()

  def get_containers(self):
    return self.client.containers.list(all = True)

  def get_images(self):
    return self.client.images.list(all = True)
