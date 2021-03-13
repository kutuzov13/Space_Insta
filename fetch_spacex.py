import argparse

import requests

from utils import download_image, get_file_extension


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='id запуска', default='latest')
    parser.add_argument('--download_path', help='Image download path', default='images')
    return parser


def download_images_spacex():
    parser = create_parser()
    args = parser.parse_args()
    spacex_launch_id = args.id
    path_download_images = args.download_path

    api_spacex = f'https://api.spacexdata.com/v3/launches/{spacex_launch_id}/'

    response = requests.get(api_spacex)
    response.raise_for_status()

    spacex_image_urls = response.json()['links']['flickr_images']
    for id_url_image, link_url_image in enumerate(spacex_image_urls):
        spacex_filename = f'spacex{id_url_image}{get_file_extension(link_url_image)}'
        download_image(spacex_filename, link_url_image, path_download_images)


if __name__ == '__main__':
    download_images_spacex()