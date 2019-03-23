import discord
from discord.ext import commands
import random

global mm

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def subtraction(ctx, a: int, b: int):
    await ctx.send(a-b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def division(ctx, a: int, b: int):
    if b==0:
        ans="0で割ってはいけません"
    else:
        ans=a/b        
    await ctx.send(ans)


@bot.command()
async def hello(ctx):
    await ctx.send("こんにちは！")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def memo(ctx, a: str):
    global mm
    mm=a
    await ctx.send("メモしました！")

@bot.command()
async def remind(ctx):
    await ctx.send(mm)

@bot.command()
async def omikuzi(ctx):
    olist=["大吉","中吉","小吉","吉","凶"]
    n = random.randint(0,4)
    a=olist[n]
    await ctx.send(a)

@bot.command()
async def DMM(ctx):
    await ctx.send("https://www.dmm.com/")
    await ctx.send("https://upload.wikimedia.org/wikipedia/commons/e/e7/DMM.com_logo.gif")
    


bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="このボットのコマンドリスト", color=0xeee657)

    embed.add_field(name="$add X Y", value="XとYの足し算の結果を出力します。", inline=False)
    embed.add_field(name="$subtraction X Y", value="XとYの引き算の結果を出力します。", inline=False)
    embed.add_field(name="$multiply X Y", value="XとYの掛け算の結果を出力します。", inline=False)
    embed.add_field(name="$division X Y", value="XとYの割り算の結果を出力します。0除算をするとエラーがでます。", inline=False)
    embed.add_field(name="$hello", value="心地の良いあいさつが返ってきます。", inline=False)
    embed.add_field(name="$cat", value="かわいいネコのGIFによってユーザーのやる気を上げます。", inline=False)
    embed.add_field(name="$memo", value="一つの文章を覚えます。", inline=False)
    embed.add_field(name="$remind", value="memoコマンドで覚えた文を出力します。", inline=False)
    embed.add_field(name="$omikuzi", value="おみくじです。", inline=False)
    embed.add_field(name="$DMM", value="DMM様のURLとロゴが表示されます。", inline=False)
    embed.add_field(name="$help", value="ヘルプを表示します。", inline=False)

    await ctx.send(embed=embed)

bot.run('token')