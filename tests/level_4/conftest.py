import os

import pytest


@pytest.fixture
def file_path():
    path_to_file = 'test.txt'
    with open(path_to_file, 'w') as file_handler:
        file_handler.writelines(['[tool:app-config]\n', 'field1=value1\n', 'field2=value2\n'])
    yield path_to_file
    os.remove(path_to_file)


@pytest.fixture
def file_path_config():
    path_to_file = 'test.txt'
    with open(path_to_file, 'w') as file_handler:
        file_handler.writelines(['[tool:app-config]\n', 'extra_fields = field1: int\n', 'field2: str\n'])
    yield path_to_file
    os.remove(path_to_file)