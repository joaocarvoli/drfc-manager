from gloe import transformer
from pipelines.helpers.files_manager import create_folder, delete_files_on_folder
from pipelines.transformers.exceptions.base import BaseExceptionTransformers


@transformer
def create_sagemaker_temp_files(sagemaker_temp_dir: str):
    try:
        create_folder(sagemaker_temp_dir, 0o770)
    except PermissionError as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to create the sagemaker's temp folder", e)


@transformer
def check_if_metadata_is_available(work_directory: str):
    try:
        create_folder(work_directory)
        delete_files_on_folder(work_directory)
    except PermissionError as e:
        raise BaseExceptionTransformers(exception=e)
    except Exception as e:
        raise BaseExceptionTransformers("It was not possible to check if the metadata is available", e)
