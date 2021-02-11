import discord
from discord.ext import commands
import cv2
import numpy as np
import pytesseract
from PIL import Image
import requests

def get_string(img_path):
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.imwrite("removed_noise.png", img)
    cv2.imwrite(img_path, img)
    result = pytesseract.image_to_string(Image.open(img_path),config='-l eng + equ')
    return result


bot = commands.Bot(command_prefix='.', description="This is an OCR-Butt")
# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Butts", url="abcd"))
    print("Lessa GO!! It's Butt Time!!!!")

@bot.event
async def on_message(message):
    try:
        url = message.attachments[0].url
        r = requests.get(url)
        filename = "img.png"
        with open(filename, 'wb') as out_file:
            out_file.write(r.content)
        print(url)
        context = await bot.get_context(message)
        ocr = get_string("img.png")
        try:
            await context.send(ocr)
        except:
            await context.send("Butt couldn't find any TEXT ಥ_ಥ")
    except:
        pass
    await bot.process_commands(message)
    
## Add your Bot Token Here.    
bot.run(BOT_TOKEN)