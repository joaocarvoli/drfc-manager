import os
from dotenv import load_dotenv
import subprocess

load_dotenv()

scripts_folder = {
  "evaluation":"evaluation",
  "log_analysis":"log-analysis",
  "metrics":"metrics",
  "training":"training",
  "upload":"upload",
  "viewer":"viewer"
}

scripts_name = {
  "start":"start",
  "stop":"stop",
  "download_model":"download-model",
  "import_model":"import-model",
  "upload_car":"upload-car",
  "upload_model":"upload-model",
}

class ScriptsManager:
  def __init__(self):
    self.drfc_repo = os.getenv("DRFC_REPO_ABS_PATH_SCRIPTS")

  def start_training(self, replace: bool):
    script_path = f'{self.drfc_repo}/{scripts_folder["training"]}/${scripts_name["start"]}'
    if replace:
      script_path += " -w"

    os.system(script_path)

  def stop_training(self):
    script_path = f'{self.drfc_repo}/{scripts_folder["training"]}/${scripts_name["stop"]}'
    
    os.system(script_path)