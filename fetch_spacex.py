import argparse

import requests

from utils import download_image, get_file_extension, create_directory


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id запуска', default='latest')
    parser.add_argument('--download_path', help='Image download path', default='images')
    return parser


def download_images_spacex(launch_id, image_directory):
    api_spacex = f'https://api.spacexdata.com/v3/launches/{launch_id}/'

    response = requests.get(api_spacex)
    response.raise_for_status()

    spacex_image_urls = response.json()['links']['flickr_images']
    for image_id, image_url in enumerate(spacex_image_urls):
        spacex_filename = f'spacex{image_id}{get_file_extension(image_url)}'
        download_image(spacex_filename, image_url, image_directory)


def main():
    parse = create_parser()
    args = parse.parse_args()
    spacex_launch_id = args.id
    path_download_images = args.download_path
    create_directory(path_download_images)
    download_images_spacex(spacex_launch_id, path_download_images)


if __name__ == '__main__':
    main()