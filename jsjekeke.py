failed_to_fetch = []
import sys 
import json 
import datetime 
import random 
import math 
import time 
import requests
import os.path as path 

try:
   import cv2
except ImportError or ModuleNotFoundError:
   failed_to_fetch.append("opencv-python")


try:
   import websocket 
except ImportError or ModuleNotFoundError:
   failed_to_fetch.append("websocket_client")


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
