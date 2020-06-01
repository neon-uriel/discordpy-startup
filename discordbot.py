# coding: utf-8
from discord.ext import commands
import os
import traceback
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np
import discord
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(activity=discord.Game(name='稼働中'))

# 画像に文字を入れる関数
def img_add_msg(img, message):
    font_path = './fonts/Noto.otf'           # Windowsのフォントファイルへのパス
    font_size = 20    # フォントサイズ
    font = ImageFont.truetype(font_path, font_size,0,encoding='utf-8')     # PILでフォントを定義
    mask = Image.open("./images/ejimasu_stamp_alpha.png")
    img = Image.fromarray(img)                          # cv2(NumPy)型の画像をPIL型に変換
    bg = Image.new("RGBA", img.size,(0,0,0,0))
    bg.paste(img,(0,0),mask.split()[0])
    textch = Image.new("RGBA", img.size,(0,0,0,0))
    draw = ImageDraw.Draw(textch)                          # 描画用のDraw関数を用意
    w , h = draw.textsize(message,font=font)
    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    draw.text(((320-w)/2, 250), message, font=font, fill=(255, 51, 102, 1))
    #textch.paste(bg,(0,0))
    textch = np.array(textch)                                 # PIL型の画像をcv2(NumPy)型に変換
    return textch                                          # 文字入りの画像をリターン


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ejimasu(ctx, arg):
    img = cv2.imread('./images/ejimasu_stamp.png', 1)                         # カラー画像読み込み
    message = arg                # 画像に入れる文章
    img = img_add_msg(img, message)
    #img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)     
    cv2.imwrite('./images/result.png', img)                    # 画像に文字を入れる関数を実行
    # await ctx.send('ejimasuは' + arg)
    await ctx.send(file=discord.File("./images/result.png"))

bot.run(token)