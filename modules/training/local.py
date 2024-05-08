import os
from dotenv import load_dotenv

load_dotenv()

class ScriptsManager:
  def __init__(self):
    self.drfc_repo = os.getenv("DRFC_REPO_ABS_PATH_SCRIPTS")

  def start_training(self, replace: bool):
    script_path = f'{self.drfc_repo}/{scripts_folder["training"]}/{scripts_name["start"]}'
    if replace:
      script_path += " -w"

    os.system(script_path)

  def stop_training(self):
    script_path = f'{self.drfc_repo}/{scripts_folder["training"]}/{scripts_name["stop"]}'
    os.system(script_path)


scripts_folder = {
  "evaluation":"evaluation",
  "log_analysis":"log-analysis",
  "metrics":"metrics",
  "training":"training",
  "upload":"upload",
  "viewer":"viewer"
}

scripts_name = {
  "start":"start.sh",
  "stop":"stop.sh",
  "download_model":"download-model.sh",
  "import_model":"import-model.sh",
  "upload_car":"upload-car.sh",
  "upload_model":"upload-model.sh",
}