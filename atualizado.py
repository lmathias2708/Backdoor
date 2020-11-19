import discord
from discord import channel
from discord.ext import commands
from discord.ext.commands.core import command

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('~-'*10, 'BOT ONLINE', '-~'*10)
    print('We have logged in as {0.user}'.format(bot))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Tudo é de todos."))

@bot.command()
async def comandos(ctx):
    await ctx.send('__**Comandos do Bot Comunista**__\n***Prefixo { __>__ }***\n***>parar*** - Tira a musica.\n***>nosso*** - Toca o meme do comunismo.\n***>gemido*** - Toca gemidao estourado.\n***>hino*** - Toca o hino da União Sovietica.\n***>rojao*** - Solta um rojão na call.')

@bot.command()
async def parar(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()

@bot.command()
async def nosso(ctx):
    try:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='meme.mp3'))
        ctx.send('__**Nada é de ninguém, tudo é de todos.**__')
    except:
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='meme.mp3'))
        ctx.send('__**Nada é de ninguém, tudo é de todos.**__')

@bot.command()
async def fome(ctx):
    try:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='meme.mp3'))
    except:
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='meme.mp3'))

@bot.command()
async def gemido(ctx):
    try:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='gemido.mp3'))
    except:
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='gemido.mp3'))

@bot.command()
async def t(ctx):
    try:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='win.mp3'))
    except:
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='win.mp3'))

@bot.command()
async def hino(ctx):
    try:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='1.mp3'))
    except:
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
    channel = ctx.author.voice.channel
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(source='1.mp3'))
       
@bot.command()
async def rojao(ctx):
    try:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='rojao.mp3'))
    except:
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='rojao.mp3'))

@bot.command()
async def BilieJean(ctx):
    try:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='Bilie.mp3'))
    except:
        guild = ctx.message.guild
        voice_client = guild.voice_client
        await voice_client.disconnect()
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(source='Bilie.mp3'))

bot.run('NzI5MDUwNzEwMzI2Mzc4NTc3.XwDTYg.3m3kHY8zlrP2Lm8K2jfGPUHE9SI')