import os
from urllib.parse import urlparse, unquote
from pathlib import Path

import requests


def download_image(image_name, image_link, image_directory):
    response = requests.get(image_link, verify=False)
    response.raise_for_status()

    with open(f'{image_directory}/{image_name}', mode='wb') as pic:
        pic.write(response.content)


def create_directory(directory_name):
    Path(directory_name).mkdir(parents=True, exist_ok=True)


def get_file_extension(image_link):
    parsed_link = urlparse(image_link)
    return os.path.splitext(unquote(parsed_link.path))[-1]