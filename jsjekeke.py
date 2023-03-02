import sys 
import json 
import datetime 
import random 
import math 
import time 
import requests
import os.path as path 
import cv2 
import websocket 
import numpy as np 
from bs4 import BeautifulSoup # Очень полезная библиотека
from colorama import Fore, Back, Style, init 

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


def get_chunk(d, x, y): 
     data = requests.get(f'https://twitch.tv/place').content 
     arr = np.zeros((448, 448), np.uint8) 
     if len(data) != 65536: 
         return arr 
     for i in range(65536): 
         c = data[i]
