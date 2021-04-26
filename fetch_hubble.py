import argparse

import requests
from utils import create_directory, download_image, get_file_extension


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id запуска')
    parser.add_argument('--download_path', help='Image download path', default='images')
    return parser


def download_images_hubble(launch_id, image_directory):
    api_hubble = f'http://hubblesite.org/api/v3/image/{launch_id}'

    response = requests.get(api_hubble)
    response.raise_for_status()

    last_image_hubble = response.json()['image_files'][-1]
    last_image_url = f'https:{last_image_hubble["file_url"]}'
    hubble_filename = f'hubble{launch_id}{get_file_extension(last_image_hubble["file_url"])}'
    download_image(hubble_filename, last_image_url, image_directory)


def main():
    parser = create_parser()
    args = parser.parse_args()
    hubble_launch_id = args.id
    hubble_path_images = args.download_path
    create_directory(hubble_path_images)
    download_images_hubble(hubble_launch_id, hubble_path_images)


if __name__ == '__main__':
    main()
