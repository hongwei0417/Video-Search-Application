import tkinter as tk
from tkinter import messagebox
import requests
import re
from PIL import ImageTk, Image
from io import BytesIO
from urllib.request import urlopen


_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')

emoji_pattern = re.compile(
    u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    "+", flags=re.UNICODE)


def openLocal(url, w, h):
    img_open = Image.open(url).resize((w,h), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_open)
    return img

def openOnline(url, w, h):
    response = requests.get(url)
    img_data = response.content
    # img_data = urlopen(url).read()
    byte_data = BytesIO(img_data)
    img_open = Image.open(byte_data).resize((w,h), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img_open)
    return img

def _surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little')))

def with_surrogates(text):
    return _nonbmp.sub(_surrogatepair, text)

def remove_emoji(text):
    return emoji_pattern.sub(r'', text)

def show():
    messagebox.showinfo("蒐藏", "影片已加入蒐藏")



