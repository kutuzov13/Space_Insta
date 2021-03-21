import argparse
import os

import requests
from dotenv import load_dotenv

from utils import download_image, get_file_extension, create_directory


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('date', help='date of the photo taken')
    parser.add_argument('--download_path', help='Image download path', default='images')
    return parser


def fetch_images_mars_rover(token, date_photo, image_directory):

    api_nasa = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos/'
    params = {'earth_date': date_photo,
              'api_key': token,
              'camera': 'FHAZ',
              }

    response = requests.get(api_nasa, params=params)
    response.raise_for_status()

    info_list = response.json().get('photos')
    for image_name, nasa_url in enumerate(info_list):
        nasa_filename = f'{nasa_url.get("id")}.{get_file_extension(nasa_url.get("img_src"))}'
        download_image(nasa_filename, nasa_url.get('img_src'), image_directory)


def main():
    load_dotenv()
    nasa_token = os.getenv('TOKEN_NASA')

    parser = create_parser()
    args = parser.parse_args()
    date_photo = args.date
    rover_path_images = args.download_path

    create_directory(rover_path_images)
    fetch_images_mars_rover(nasa_token, date_photo, rover_path_images)


if __name__ == '__main__':
    main()
