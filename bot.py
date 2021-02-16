import discord
from discord.ext import commands
import pytesseract
import cv2
import numpy as np
from PIL import Image
from PIL import ImageFilter
from io import BytesIO
import requests


def process_image(url):
    img = _get_image(url)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    img=cv2.filter2D(img,-1,filter)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    pytesseract.pytesseract.tesseract_cmd = "/app/.apt/usr/bin/tesseract"
    return pytesseract.image_to_string(img)

def _get_image(url):
    return np.asarray(Image.open(BytesIO(requests.get(url).content)))

bot = commands.Bot(command_prefix='.', description="This is an OCR-Butt")
# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Butts", url="https://www.youtube.com/watch?v=sy9ztJuZu2c"))
    print("Lessa GO!! It's Butt Time!!!!")

@bot.event
async def on_message(message):
    try:
        url = message.attachments[0].url
        print(url)
        context = await bot.get_context(message)
        ocr = process_image(url)
        try:
            await context.send(ocr)
        except:
            await context.send("Butt couldn't find any TEXT ಥ_ಥ")
    except:
        pass
    await bot.process_commands(message)
    
# Enter your BOT_TOKEN Here
bot.run('BOT_TOKEN')