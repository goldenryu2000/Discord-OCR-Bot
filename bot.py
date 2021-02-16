import discord
from discord.ext import commands
import pytesseract
from PIL import Image
from PIL import ImageFilter
from io import BytesIO
import requests

def process_image(url):
    image = _get_image(url)
    image.filter(ImageFilter.SHARPEN)
    return pytesseract.image_to_string(image)

def _get_image(url):
    return Image.open(BytesIO(requests.get(url).content))

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
    
  #Add your BOT TOKEN here:   
bot.run('BOT_TOKEN')