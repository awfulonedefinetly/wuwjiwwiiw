failed_to_fetch = []
import sys 
import json 
import datetime 
import random 
import math 
import time 
import requests
import os.path as path 
import hitherdither

try:
   import cv2
except ImportError or ModuleNotFoundError:
   failed_to_fetch.append("opencv-python")


try:
   import socket
except ImportError or ModuleNotFoundError:
   failed_to_fetch.append("socket")


try:
   import numpy as np 
except ImportError or ModuleNotFoundError:
   failed_to_fetch.append("numpy")


try:
   from bs4 import BeautifulSoup 
except ImportError or ModuleNotFoundError:
   failed_to_fetch.append("beautifulsoup4")

from colorama import Fore, Back, Style, init 

if len(failed_to_fetch) > 0:
  print("Неудалось установить некоторые библиотеки для работы бота. Установите их самостоятельно: " + "".join(failed_to_fetch))
  sys.exit()

init(convert=True)

host = "ваш хост"
port = "порт"

def connect(s, host, port, retry=1):
	connected = False
	try:
	    s.connect((host, port))
	    print("[INFO] Присоединился к серверу.")
	    connected = True
	except ConnectionRefusedError:
	    if retry < 10:
	       print("[INFO] Вы пытайтесь присоединться (try n°{})".format(retry+1))
	       connected = connect(s, host, port,retry+1)
	finally:
            return connected



class PlaceBotConfigAuth(object): 
     def __init__(self): 
         self.login = '' 
         self.password = '' 
class PlaceBotConfigProxy(object): 
    def __init__(self): 
        self.host = '' 
        self.port = 0 
        self.user = '' 
        self.passwd = '' 
class PlaceBotConfigImage(object): 
    def __init__(self): 
        self.path = '' 
        self.x = 0 
        self.y = 0 
        self.defend = False 
        self.strategy = '' 
        self.canv_id = 0 
class PlaceBotConfig(object): 
    def __init__(self): 
        self.auth  = PlaceBotConfigAuth() 
        self.proxy = PlaceBotConfigProxy() 
        self.image = PlaceBotConfigImage()


def show_image(img): 
     print(f'{Fore.YELLOW}Нажмите любую кнопку, чтобы закрыть окно.{Style.RESET_ALL}') 
     cv2.imshow('image', img) 
     cv2.waitKey(0) 
     cv2.destroyAllWindows()


def get_chunk(d=None, x=None, y=None): 
     data = requests.get(f'https://twitch.tv/place').content 
     arr = np.zeros((900, 900), np.uint8) 
     if len(data) != 65536: 
         return arr 
     for i in range(65536): 
         c = data[i]


def download_file(url): 
     filename = url.split('/')[-1] 
     r = requests.get(url, stream=True) 
     with open(local_filename, 'wb') as f: 
         for chunk in r.iter_content(chunk_size=1024):  
             if chunk: 
                 f.write(chunk) 
     return filename

def place_pixel(x, y, color):
    url = "https://twitch.tv/place"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
  
    r, g, b = tuple(bytes.fromhex(color.lstrip('#')))
    pixel = np.array([[[r, g, b]]], dtype=np.uint8)
    pixel_bytes = bytearray(pixel.tobytes())
    data = bytearray([x, y]) + pixel_bytes
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 201:
        print("[****] - Пиксель поставился!")
    else:
        print("[XXXX] - Пиксель не удалось поставить!")


def load_and_dither_image(image_path): 
     img = Image.open(image_path) 
     palette = hitherdither.palette.Palette(color_palette) 
     img_dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(img, palette, order=8) 
     # image_arr = np.asarray(img) 
     image_arr = np.asarray(img_dithered) + 2 
     # print(img_dithered) 
  
     return image_arr 

def draw_from_image(image_path, start, start_from=(0, 0)): 
     start_x, start_y = start 
     image = load_and_dither_image(image_path) 
     for y_img, row in enumerate(image): 
         if y_img < start_from[1]: 
             continue 
         for x_img, pixel in enumerate(row): 
             if x_img < start_from[0] and y_img == start_from[1]: 
                 continue 
             if pixel == 2: 
                 continue 
             place_pixel(start_x + x_img, start_y + y_img, pixel)
