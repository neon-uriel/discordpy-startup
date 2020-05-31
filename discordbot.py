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

# 画像に文字を入れる関数
def img_add_msg(img, message):
    font_path = './fonts/NotoSansMonoCJKjp-Bold.otf'           # Windowsのフォントファイルへのパス
    font_size = 20    # フォントサイズ
    font = ImageFont.truetype(font_path, font_size)     # PILでフォントを定義
    img = Image.fromarray(img)                          # cv2(NumPy)型の画像をPIL型に変換
    draw = ImageDraw.Draw(img)                          # 描画用のDraw関数を用意
    w = draw.textsize(message)
    # テキストを描画（位置、文章、フォント、文字色（BGR+α）を指定）
    draw.text(((300-w)/2, 250), message, font=font, fill=(255, 255, 255, 0))
    img = np.array(img)                                 # PIL型の画像をcv2(NumPy)型に変換
    return img                                          # 文字入りの画像をリターン


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
    cv2.imwrite('./images/result.png', img)                    # 画像に文字を入れる関数を実行
    # await ctx.send('ejimasuは' + arg)
    await ctx.send(file=discord.File("./images/result.png"))

bot.run(token)
