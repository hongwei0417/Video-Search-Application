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
    # try:
    #     char = match.group()
    #     assert ord(char) > 0xffff
    #     encoded = char.encode('utf-16-le')
    #     t = (
    #         chr(int.from_bytes(encoded[:2], 'little')) + 
    #         chr(int.from_bytes(encoded[2:], 'little'))
    #     )
    #     return t
    # except ValueError:
    #     print(ValueError)
    #     return ""

    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    t = (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little'))
    )
    return t

def with_surrogates(text):
    # try:
    #     t = _nonbmp.sub(_surrogatepair, text)
    #     return t
    # except ValueError:
    #     print(ValueError)
    #     return text
    t = _nonbmp.sub(_surrogatepair, text)
    return t

def remove_emoji(text):
    # try:
    #     t = emoji_pattern.sub(r'', text)
    #     return t
    # except ValueError:
    #     print(ValueError)
    #     return ""

    t = emoji_pattern.sub(r'', text)
    return t

def show():
    messagebox.showinfo("蒐藏", "影片已加入蒐藏")


def format_view(t):
    result = ""
    text = t.strip().strip(' ')
    number = int(''.join(x for x in text if x.isdigit()))
    if number >= 10000:
        number = round(number / 10000, 1)
        result = "觀看次數：{0}萬次".format(number)
    else:
        result = "觀看次數：{0}次".format(number)

    return result



