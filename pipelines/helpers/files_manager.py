from glob import glob
import os


def create_folder(folder_name: str, mode: int = None):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name, mode=mode)
        return True
    return False


def delete_files_on_folder(folder_name: str):
    if os.path.exists(folder_name):
        files = glob(f'{folder_name}/*')
        [os.remove(file) for file in files]
        return True
    return False
