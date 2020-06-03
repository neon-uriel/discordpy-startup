# coding: utf-8
from discord.ext import commands
import os
import io
import traceback
from PIL import Image, ImageFont, ImageDraw
import cv2
import numpy as np
import discord
import asyncio
import makegotoitaly
import requests
import urllib.request
import neta_output
from discord.ext.commands import CommandNotFound

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
    if isinstance(error, CommandNotFound):
        return
    raise error


@bot.command()
async def ejimasu(ctx, *args):
    message = args[0] # 画像に入れる文章
    message = message.replace('_',' ')
    if len(args) == 1:
        fontcolor = '#FF5555'
    else:
        fontcolor = args[1]
    img = makegotoitaly.img_add_msg("./images/ejimasu_stamp.png", message,fontcolor,30,False)
    img.save("./images/result.png")
    await ctx.send(file=discord.File("./images/result.png"))

@bot.command()
async def gotoitaly(ctx, *args):
    message = args[0] # 画像に入れる文章
    message = message.replace('_',' ')
    if len(args) == 1:
        fontcolor = '#FF5555'
    else:
        fontcolor = args[1]
    img = makegotoitaly.img_add_msg("./images/gotoitaly_stamp.png", message,fontcolor,30,False)
    img.save("./images/result.png")
    await ctx.send(file=discord.File("./images/result.png"))

@bot.command()
async def urlimg(ctx, *args):
    message = args[1] # 画像に入れる文章
    message = message.replace('_',' ')
    if len(args) == 2:
        fontcolor = '#FF5555'
    else:
        fontcolor = args[2]
    imgurl = args[0]
    file_name = './images/download.png'
    r = requests.get(imgurl)
    img = Image.open(io.BytesIO(r.content))
    img.save(file_name)
    img = makegotoitaly.img_add_msg(file_name, message,fontcolor,30,False)
    img.save("./images/result.png")
    await ctx.send(file=discord.File("./images/result.png"))

@bot.command()
async def netadashi(ctx):
    await ctx.send(neta_output.netaGen())

bot.run(token)