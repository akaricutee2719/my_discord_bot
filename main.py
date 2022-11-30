import discord
from discord.ext import commands
import json
import os
import random
import time
intents = discord.Intents.all()
intents.members = True


client = commands.Bot(command_prefix="tz!",intents=intents)
@client.command()
async def o(ctx):
    if str(ctx.message.author.id) == '748439531761434676':
        exit()
    else:
        await ctx.send(f"{ctx.message.author.mention}, you don't have permission to run this command !")
@client.event
async def on_ready():
    print("Bot logged in successfully !")
@client.command()
async def i(ctx,*,name):
    if name == 'gbao':
        with open('assets\\img\\gbao.png', 'rb') as pic:
            picture = discord.File(pic)
        await ctx.send(f'{ctx.message.author.mention} coward.',file=picture)
@client.command()
async def VAR(ctx,*, question):
    await ctx.send(f'{ctx.message.author.mention} using VAR\n CHECKING VAR, POSSIBLE **{question}**')
    time.sleep(3)
    if random.randint(0,1) == 1:
        await ctx.send(f'{ctx.message.author.mention} using VAR\n CHECKING VAR, POSSIBLE **{question}** IS TRUE .')
    else:
        await ctx.send(f'{ctx.message.author.mention} using VAR\n CHECKING VAR, POSSIBLE **{question}** IS FALSE .')
@client.command()
async def bankcash(ctx):
    users = await get_bank_data()
    bank = users[str(ctx.message.author.id)]["bank"]
    await ctx.send(f"{ctx.message.author.mention}, số tiền bạn đang có trong ngân hàng là **{bank:,d}** :banana: !")
@client.command()
async def lode(ctx,money, num):
    users = await get_bank_data()
    if users[str(ctx.message.author.id)]["wallet"] < int(money):
        await ctx.send(f"{ctx.message.author.mention}, bạn không có đủ banana để chơi !")
    elif int(money) > 1000000:
        await ctx.send(f"{ctx.message.author.mention}, mỗi lần chơi chỉ được tiêu không quá 1 triệu :banana: !")
    elif str(ctx.message.author.id) == '748439531761434676':
        await ctx.send(f"{ctx.message.author.mention}, bạn đã thắng **{int(money)*100:,d}** :banana:, số đó là **{num}** !")
        users['748439531761434676']["wallet"] += int(money)*100
    else:
        users[str(ctx.message.author.id)]["wallet"] -= int(money)
        await ctx.send(f"{ctx.message.author.mention} thử vận may với số **{num}** !")
        time.sleep(3)
        pts = random.randint(0,100)
        if int(num) == int(pts):
            users[str(ctx.message.author.id)]["wallet"] += int(money)*100
            await ctx.send(f"{ctx.message.author.mention}, bạn đã thắng **{int(money)*100:,d}** :banana:, số đó là **{pts}** !")
        else: 
            await ctx.send(f"{ctx.message.author.mention}, bạn đã thua **{int(money):,d}** :banana:, số đó phải là **{pts}** !")
    await save_information(users)
@client.command()
async def cash(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    money_users = users[str(user.id)]["wallet"]
    await ctx.send(f"{ctx.message.author.mention}, số banana hiện tại của bạn là **{money_users:,d}** :banana: !")
#tao tai khoan
async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)]={}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    with open('assets\\json\\money.json', 'w') as f:
        json.dump(users, f)
    return True
async def get_bank_data():
    with open('assets\\json\\money.json', 'r') as f:
        users = json.loads(f.read())
    return users
@client.command()
async def give(ctx,mentions, money_give):
    users = await get_bank_data()
    if users[str(ctx.message.author.id)]["wallet"] < int(money_give):
        await ctx.send(f"{ctx.message.author.mention}, bạn không có đủ banana để chuyển !")
    else:
        id_user = mentions
        id_user = id_user.replace("<","")
        id_user = id_user.replace(">","")
        id_user = id_user.replace("@","")
        users[str(ctx.message.author.id)]["wallet"] -= int(money_give)
        users[str(id_user)]["wallet"] += int(money_give)
        await save_information(users)
        await ctx.send(f"{ctx.message.author.mention}, bạn đã chuyển thành công số banana là **{int(money_give):,d}** :banana: !")
@client.command()
async def deposit(ctx, money):
    users = await get_bank_data()
    bank_left = users[str(ctx.message.author.id)]["bank"]
    if users[str(ctx.message.author.id)]["wallet"] < int(money):
        await ctx.send(f"{ctx.message.author.mention}, số tiền trong túi bạn không đủ để gửi vào ngân hàng !")
    elif users[str(ctx.message.author.id)]["bank"] + int(money) > 50000000:
        await ctx.send(f"{ctx.message.author.mention}, ngân hàng chỉ cho phép mỗi người chứa 50 triệu!\n Bạn chỉ còn lại **{50000000-int(bank_left):,d}** :banana: có thể gửi vào !")
    else:
        users[str(ctx.message.author.id)]["bank"] +=int(money)
        await ctx.send(f"{ctx.message.author.mention}, bạn đã chuyển thành công vào ngân hàng số tiền là **{int(money):,d}** :banana: !")
    await save_information(users)
@client.command()
async def banana(ctx, money):
    users = await get_bank_data()
    if users[str(ctx.message.author.id)]["wallet"] < int(money):
        await ctx.send(f"{ctx.message.author.mention}, bạn không có đủ banana để chơi !")
    elif str(ctx.message.author.id) == '748439531761434676':
        await ctx.send(f"{ctx.message.author.mention}, bạn đã thắng **{int(money)*2:,d}** :banana: !")
        users[str(ctx.message.author.id)]["wallet"] += int(money)*2
    else:
        await ctx.send(f"{ctx.message.author.mention} cược **{int(money):,d}** :banana: !")
        users[str(ctx.message.author.id)]["wallet"] -= int(money)
        pts = random.randint(0,1)
        if int(pts) == '1':
            await ctx.send(f"{ctx.message.author.mention}, bạn đã thắng **{int(money)*2:,d}** :banana: !")
            users[str(ctx.message.author.id)]["wallet"] += int(money)*2
        else:
            await ctx.send(f"{ctx.message.author.mention}, bạn đã thua **{int(money):,d}** :banana: !")
    await save_information(users)
@client.command()
async def withdraw(ctx,money):
    users = await get_bank_data()
    bank_left = users[str(ctx.message.author.id)]["bank"]
    if users[str(ctx.message.author.id)]["bank"] < int(money):
        await ctx.send(f"{ctx.message.author.mention}, bạn không có đủ banana để rút !")
    else:
        users[str(ctx.message.author.id)]["bank"] -= int(money)
        users[str(ctx.message.author.id)]["wallet"] += int(money)
        await ctx.send(f"{ctx.message.author.mention}, bạn đã rút thành công số tiền là **{int(money):,d}** :banana: !")
    await save_information(users)

async def save_information(users):
    with open('assets\\json\\money.json', 'w') as f:
        json.dump(users, f)
client.run('MTA0NTk1MzI4OTQ3ODQ3NTg4Ng.GAeC80.FCBugIrmpqxf87cdNj_cz47s5aBsUXN880zMP0')