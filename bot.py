import discord
from discord.ext import commands
from model import predict

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./images/{file_name}")
            await ctx.send(f"Resminiz Kaydedildi. Resminizin Konumu: ./images/{file_name}\n Dosyanın URL'si: {file_url} ")
            await ctx.send('Gönderdiğiniz Resmi İnceliyorum. Lütfen Bekleyiniz...')
            await ctx.send(predict(modelPath='./models/keras_model.h5', labelsPath='./models/labels.txt', imgPath=f"./images/{file_name}"))
    else:
        await ctx.send("Resim Yüklemeyi Unuttunuz!:(")
        



bot.run("TOKEN")