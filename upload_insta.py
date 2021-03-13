import argparse
import os

import instabot
from dotenv import load_dotenv
from PIL import Image


MAX_SIZE = (1080, 1080)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help='Path to images to send', default=os.getenv('IMAGES_PATH'))
    return parser


def resize_photos(filepath):
    for file in os.listdir(filepath):
        path_files = f'{filepath}/{file}'
        image = Image.open(path_files)
        image.thumbnail(MAX_SIZE)
        image.save(path_files, format="JPEG")


def upload_in_instagram():
    load_dotenv()
    insta_username = os.getenv('INSTAGRAM_USERNAME')
    insta_password = os.getenv('INSTAGRAM_PASSWORD')

    parser = create_parser()
    args = parser.parse_args()
    images_path = args.path

    resize_photos(images_path)

    bot = instabot.Bot()
    bot.login(username=insta_username, password=insta_password)

    insta_images_names = os.listdir(images_path)
    try:
        for insta_image_name in insta_images_names:
            bot.upload_photo(f'{images_path}/{insta_image_name}')
    except Exception as error:
        print(error)
        print('Photos are not fully uploaded. Try again')


if __name__ == '__main__':
    upload_in_instagram()