import os

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


def resources_file(file_name):
    return os.path.join(ROOT_DIR, 'src', 'resources', file_name)
