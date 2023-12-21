import discord
from discord.ext import commands
import random

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix = "$", intents=intents)
bot.remove_command('help')

#greeting
@bot.event
async def on_ready():
    print("бот працює")

#greeting2
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send('Ласкаво просимо на сервер!')

#help
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        color = 0x7CFC00,
        title = 'Список команд:',
        description = '$help - Виклик цього списку\n$kick "@user" - кік користувача із сервера\n$rand - виведення випадкового числа радіусом 0 - 500'
        )
    await ctx.send(embed = embed)

#rand
@bot.command()
async def rand(ctx):
    await ctx.reply(random.randint(0, 500))

#kick
@bot.command()
async def kick(ctx, member : discord.Member):
    await ctx.message.delete()
    await member.kick()
    await ctx.send("Користувач {} кікнут із сервера".format(member.mention))


bot.run("Put your token here")
