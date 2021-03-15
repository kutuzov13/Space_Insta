import argparse
import os

import instabot
from dotenv import load_dotenv
from PIL import Image


MAX_SIZE = (1080, 1080)


def create_parser():
    parse = argparse.ArgumentParser()
    parse.add_argument('-p', '--path', help='Path to images to send', default=os.getenv('IMAGES_PATH'))
    return parse


def editing_photos(filepath):
    """Preparing images for uploading to Instagram."""
    for filename in os.listdir(filepath):
        full_path = f'{filepath}/{filename}'
        image = Image.open(full_path)
        image.thumbnail(MAX_SIZE)
        image.save(full_path)


def upload_in_instagram(instagram_username, instagram_password, images_path):
    editing_photos(images_path)

    bot = instabot.Bot()
    bot.login(username=instagram_username, password=instagram_password)

    insta_images_names = os.listdir(images_path)
    try:
        for insta_image_name in insta_images_names:
            bot.upload_photo(f'{images_path}/{insta_image_name}')
    except FileNotFoundError as error:
        print(error)
        print('Photos are not fully uploaded. Try again')


def main():
    load_dotenv()
    insta_username = os.getenv('INSTAGRAM_USERNAME')
    insta_password = os.getenv('INSTAGRAM_PASSWORD')

    parser = create_parser()
    args = parser.parse_args()
    images_directory = args.path

    upload_in_instagram(insta_username, insta_password, images_directory)


if __name__ == '__main__':
    main()