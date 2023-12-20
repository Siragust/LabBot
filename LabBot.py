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
    print("Бот работает")

#greeting2
@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send('Добро пожаловать на сервер!')

#help
@bot.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        color = 0x7CFC00,
        title = 'Список команд:',
        description = '$help - Вызов этого списка\n$kick "@user" - кик пользователя с сервера\n$rand - вывод случайного числа радиусом 0 - 500'
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
    await ctx.send("Пользователь {} кикнут с сервера".format(member.mention))


bot.run("MTE4NDk2NjQ1OTY2ODA0MTg2OQ.G2UzbN.FSkDdNTa40XSmvMG1YXqK2-TAQiXiuMoo-zK4o")
