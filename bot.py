from datetime import datetime
import discord
from discord.ext import commands
import random
from io import StringIO
import sys

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)


def pront(content, lvl="LOG"):
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
                     icon_url=ctx.author.display_avatar.url)
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
    comand.rstrip("`")
    comand.lstrip("`")
    comand.lstrip("python")
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
    comand.rstrip("`")
    comand.lstrip("`")
    comand.lstrip("python")
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

bot.run("token here or reference to it here")#make sure you set your intents in the portal and here on line 10
