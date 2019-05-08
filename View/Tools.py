import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen


def openLocal(url, w, h):
    img_open = Image.open(url).resize((w,h), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_open)
    return img

def openOnline(url, w, h):
    response = requests.get(url)
    img_data = response.content
    # img_data = urlopen(url).read()
    img_open = Image.open(BytesIO(img_data)).resize((w,h), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_open)
    return img