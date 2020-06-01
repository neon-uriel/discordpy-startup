# coding: utf-8
from discord.ext import commands
import os
import traceback
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np
import discord
import asyncio
import makegotoitaly

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

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ejimasu(ctx, arg1,):
    #img = cv2.imread('./images/ejimasu_stamp.png', 1)                         # カラー画像読み込み
    message = arg1                # 画像に入れる文章
    img = makegotoitaly.img_add_msg("./images/ejimasu_stamp.png", message,'#FF5555',30,False)
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)     
    # cv2.imwrite('./images/result.png', img)                    # 画像に文字を入れる関数を実行
    #await ctx.send('ejimasuは' + arg)
    await ctx.send(file=discord.File("./images/result.png"))

bot.run(token)