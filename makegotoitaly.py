# coding: utf-8
from PIL import Image, ImageFont, ImageDraw
#import cv2
import numpy as np
import sys
import math

# 画像に文字を入れる関数
def img_add_msg(img, message, fontcolor = "#FF5555", fontsize = 30, isShadow = False):
    shadowcolor = '#222222'
    font_path = './fonts/Noto.otf' # Windowsのフォントファイルへのパス
    font_size = fontsize    # フォントサイズ
    fontcustom = ImageFont.truetype(font_path, font_size, 0, encoding='utf-8') # PILでフォントを定義
    # mask = Image.open("./images/ejimasu_stamp_alpha.png")
    img = Image.open(img).convert("RGBA")
    iw, ih = img.size
    iws, ihs = img.size
    while(iw > 200 or ih > 200):
        iw *= 0.99
        ih *= 0.99
        iw = math.floor(iw)
        ih = math.floor(ih)
    if(iws != 320 and ihs != 320):
        img = img.resize((iw,ih))
    bg = Image.new("RGBA", (320,320), (0,0,0,0))
    # bg.paste(img,(0,0),mask.split()[0])
    # textch = Image.new("RGBA", img.size,(0,0,0,0))
    draw = ImageDraw.Draw(bg) # 描画用のDraw関数を用意
    w , h = draw.textsize(message, font=fontcustom)
    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    while(w > 320):
        font_size -= 1
        fontcustom = ImageFont.truetype(font_path, font_size, 0, encoding='utf-8')
        w , h = draw.textsize(message, font=fontcustom)
    x = (320 - w)/2
    y = 250
    if (isShadow):
        draw.text((x+1, y+1), message, font=fontcustom, fill=shadowcolor)
        draw.text((x-1, y-1), message, font=fontcustom, fill=shadowcolor)
        draw.text((x+1, y-1), message, font=fontcustom, fill=shadowcolor)
        draw.text((x-1, y+1), message, font=fontcustom, fill=shadowcolor)
    draw.text((x, y), message, font=fontcustom, fill=fontcolor)
    centery = 0
    centerx = 0
    if (ihs != 320 and iws != 320):
        centerx = math.floor((320 - iw) / 2)
        centery = 10
    bg.paste(img,(centerx,centery),img)
    # textch = np.array(textch) # PIL型の画像をcv2(NumPy)型に変換
    return bg # 文字入りの画像をリターン