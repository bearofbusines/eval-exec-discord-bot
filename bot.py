from datetime import datetime
import discord
from time import sleep
from discord.ext import commands
from asyncio.tasks import sleep
import random
from io import StringIO
import sys

bot = commands.Bot(command_prefix=".", intents=intents)


def pront(lvl, content):
    colors = {
        "LOG": "",
        "OKBLUE": "\033[94m",
        "OKCYAN": "\033[96m",
        "OKGREEN": "\033[92m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "NONE": "\033[0m"
    }
    print(colors[lvl] + "{" + datetime.now().strftime("%x %X") +
          "} " + lvl + ": " + str(content) + colors["NONE"])

# Returns a random hex code


async def getRandomHex(seed):
    random.seed(seed)
    return random.randint(0, 16777215)

# Creates a standard Embed object


async def getEmbed(ctx, title='', content='', footer='', color=''):
    if color == '':
        color = await getRandomHex(ctx.author.id)
    embed = discord.Embed(
        title=title,
        description=content,
        color=color
    )
    embed.set_author(name=ctx.author.display_name,
                     icon_url=ctx.author.avatar_url)
    # TODO Hide the footer until i find out what to do with it
    # embed.set_footer(footer=footer)
    return embed

# Creates and sends an Embed message


async def send(ctx, title='', content='', footer='', color=''):
    embed = await getEmbed(ctx, title, content, footer)
    await ctx.send(embed=embed)


@bot.command(aliases=['eval'])
@commands.is_owner()
async def _eval(ctx, *, comand=None):
    # if (ctx.author.id == {idhere}):#for when you are not owner 369999044023549962
    #pront("LOG", comand)
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    if (comand[2] == '`'):
        comand = comand.split('\n')
        comand = comand[1:-1]
        temp = ""
        for i in comand:
            temp += i + "\n"
        comand = temp
    try:
        print(eval(comand))
    except Exception as e:
        pront(e, "ERROR")
    sys.stdout = old_stdout
    #pront("LOG", mystdout.getvalue())
    print(mystdout.getvalue())
    await send(ctx, title='Command Sent:', content='in:\n```' + comand + '```' + '\n\nout:```ansi\n' + str(mystdout.getvalue()) + '```')
#    else:#sends no perms if has none
#        await send(ctx, title='You Do Not Have Perms')


@bot.command(aliases=['exec'])
@commands.is_owner()
async def _exec(ctx, *, comand=None):
    # if (ctx.author.id == {idhere}):#for when you are not owner 369999044023549962
    #pront("LOG", comand)
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    if (comand[2] == '`'):
        comand = comand.split('\n')
        comand = comand[1:-1]
        temp = ""
        for i in comand:
            temp += i + "\n"
        comand = temp
    # pront(comand)

    try:
        exec(comand)
    except Exception as e:
        pront(e, "ERROR")
    sys.stdout = old_stdout
    #pront("LOG", mystdout.getvalue())
    print(mystdout.getvalue())
    await send(ctx, title='Command Sent:', content='in:\n```' + comand + '```' + '\n\nout:```ansi\n' + str(mystdout.getvalue()) + '```')
#    else:#sends no perms if has none
#        await send(ctx, title='You Do Not Have Perms')

@bot.command()
async def ping(ctx):
    """PING POMG"""
    await send(ctx, title='Pong')

bot.run("token here or reference to it here")
