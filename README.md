# Space Instagram

Script for loading photos from SpaceX launches and photos taken by the Hubble Space Telescope.
With the ability to send photos to Instagram!

### Install
Python3 is required to run the script.

Clone a repository from GitHub.

```git
git clone https://github.com/kutuzov13/space_insta.git
```

Install requirements.

```
pip install -r requirements.txt
```
### Libraries
- requests==2.25.1 -> For API requests.
- Pillow==8.1.2 -> For image processing with subsequent sending.
- instabot==0.117.0 -> Send Images to Instagram.
- python-dotenv==0.15.0 -> To work with a variable environment.

### Environment Variables
Instagram Login / Password is taken from the environment variable.
- create file ```.env``` next to the file ```upload_insta.py```.
- write down the Login / Password to the file ```.env```:
  
  ```INSTAGRAM_USERNAME='YOU_LOGIN'```.<br/>
  ```INSTAGRAM_PASSWORD='YOU_PASSWORD'```.<br/>
  
  
### Run
If you want to get photos from SpaceX rocket launches.
```
python fetch_spacex.py <Launch ID> --download_path <path for download images>
```

If you want to receive satellite photos Hubble.
```
python fetch_hubble.py <Launch ID> --download_path <path for download images>
```

If you want to upload photos taken by the rover.
```
python fetch_nasa.py <date> --download_path <path for download images> 
```
Date example: 2020-01-01

Send photo to Instagram.
```
python upload_insta.py -p <path to the photos you want to upload to Instagram>
```
By default, images are sent to Instagram from a folder ```images```. 

### Objective of the project
The code is written for educational purposes as an online course for web developers ***[dvmn.org](https://dvmn.org/modules/)***.
