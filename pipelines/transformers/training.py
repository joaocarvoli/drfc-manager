from gloe import transformer
from pipelines.helpers.files_manager import create_folder, delete_files_on_folder


@transformer
def create_sagemaker_temp_files():
    create_folder('/tmp/sagemaker', 0o770)


@transformer
def check_if_metadata_is_available(work_directory: str):
    create_folder(work_directory)
    delete_files_on_folder(work_directory)
