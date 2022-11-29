import discord
import os
import time
import random
from money import money_banana
from discord.ext import commands
from datetime import date

today = date.today()
intents = discord.Intents.all()
intents.members = True
#-----------------
# p1 = 7.9
# p2 = 6.5
# p3 = 5.0
# p4 = 4.3
# p5 = 3.2
# p6 = 1.9 
#-----------------
client = commands.Bot(command_prefix="tz!",intents=intents)
@client.event 
async def on_ready():
    print("Bot ready!")
@client.event
async def on_message(message):
    # do some extra stuff here
    await client.process_commands(message)
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send("Bot đang trong phiên bản BETA nên một số lệnh có thể chưa hoàn chỉnh, thông cảm :banana: !")
@client.command()
async def o(ctx):
    tag = str(ctx.message.author.id)
    if tag =='748439531761434676':
        exit()
    else:
        await ctx.send("You don't have permission to run this command !")
@client.command()
async def cash(ctx):
    id_user = ctx.message.author.id
    await ctx.channel.send(f'{ctx.message.author.mention}, '+ money_banana.kiem_tra(id_user))
@client.command()
async def tkb(ctx):
    with open('assets\\image\\thoi_khoa_bieu.jpg', 'rb') as pic:
        picture = discord.File(pic)
    await ctx.send(file=picture)
@client.command()
async def set_money_bet(ctx, money):
    if str(ctx.message.author.id) == '748439531761434676':
        with open('football_bet\\money_bet.txt', 'w') as gun_2 : 
            gun_2.write(str(money))
            await ctx.channel.send(f"Đặt số tiền tổng cược của trận đấu là **{money:,d}** !")
    else:
        await ctx.channel.send("You don't have permission to run this command !")
@client.command()
async def calc(ctx, p1, p2, p3, p4, p5, p6, time):
    f = open('football_bet\\money_bet.txt', 'r')
    date = today.strftime("%d-%m-%y")
    money = f.read()
    await ctx.send(f""" **RESULT : **
    :arrow_forward: 1 Goal : **{round(int(money)*p1):,d}** :banana: | **x{p1}**
    :arrow_forward: 2 Goals : **{round(int(money)*p2):,d}** :banana: | **x{p2}**
    :arrow_forward: 3 Goals : **{round(int(money)*p3):,d}** :banana: | **x{p3}**
    :arrow_forward: 4 Goals : **{round(int(money)*p4):,d}** :banana: | **x{p4}**
    :arrow_forward: 5 Goals : **{round(int(money)*p5):,d}** :banana: | **x{p5}**
    :arrow_forward: 6 Goals or more : **{round(int(money)*p6):,d}** :banana: | **x{p6}**
    **Chốt sau {time} | {date}**
    """)
@client.command()
async def Vu(ctx):
    await ctx.send("Vu da den.")
@client.command()
async def members__to_buy_gun(ctx):
    for guild in client.guilds:
        for member in guild.members:
            name_1 = str(member)
            name = name_1[-4:]
            if not os.path.exists(f'gun\\ak47\\{name}.txt'):
                with open(f'gun\\ak47\\{name}.txt', 'w') as gun : 
                    gun.write(str(0))
            if not os.path.exists(f'gun\\desert_eagle\\{name}.txt'):
                with open(f'gun\\desert_eagle\\{name}.txt', 'w') as gun_2 : 
                    gun_2.write(str(0))
@client.command()
async def match_id(ctx, match_id):
    with open(f"match_log\\{match_id}.txt", 'r') as f:
        await ctx.send(f.read())
@client.command(aliases = ['wantbanana'])
async def give(ctx,mentions,money):
    id_give_user = ctx.message.author.id
    id_user = mentions
    id_user = id_user.replace("<","")
    id_user = id_user.replace(">","")
    id_user = id_user.replace("@","")
    print(id_user)
    await ctx.send(f'{ctx.message.author.mention}, '+ money_banana.chuyen_tien(id_give_user, id_user, money))
@client.command()
async def lode(ctx,money, num):
    pts  = random.randint(0,100)
    print(pts)
    tag = ctx.message.author.id
    money_in_txt = open(f'assets\\information_id\\{tag}.txt')
    money_left_before= money_in_txt.read()
    if int(money) > int(money_left_before):
        await ctx.send(f"{ctx.message.author.mention}, bạn không đủ banana để chơi !")
    elif int(money) <= 0:
        await ctx.send(f"{ctx.message.author.mention}, giá trị không đúng !")
    elif not money.isdigit():
        await ctx.send(f"{ctx.message.author.mention}, giá trị không đúng !")
    elif int(money) > 1000000:
        await ctx.send(f"{ctx.message.author.mention}, mỗi lần chơi chỉ được tiêu ít hơn 1 triệu banana !")
    elif int(num) <0 or int(num) > 100 :
        await ctx.send(f"{ctx.message.author.mention}, nhập số từ 0-100 !")
    else: 
        await ctx.send(f"{ctx.message.author.mention} thử vận may với số **{num}** !")
        time.sleep(3.5)
        if int(num) == int(pts):
            money_given = int(money) * 20
            money_given_in = int(money_left_before) + int(money_given)

            await ctx.send(f"Chúc mừng {ctx.message.author.mention}, bạn đã thắng **{int(money_given):,d}** :banana:, số đó là **{pts}** !")
            with open(f'assets\\information_id\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_given_in))
        else:
            money_given = int(money_left_before) - int(money)
            await ctx.send(f"{ctx.message.author.mention}, bạn đã thua **{int(money):,d}** :banana:, số đó phải là **{pts}** !")
            with open(f'assets\\information_id\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_given))
@client.command()
async def banana(ctx,*,money):
    tag = ctx.message.author.id
    money_in_txt = open(f'assets\\information_id\\{tag}.txt')
    money_left_before= money_in_txt.read()
    
    if int(money) > int(money_left_before):
        await ctx.send(f"{ctx.message.author.mention}, bạn không đủ banana để chơi !")
    elif int(money) <= 0:
        await ctx.send(f"{ctx.message.author.mention}, giá trị không đúng !")
    elif not money.isdigit():
        await ctx.send(f"{ctx.message.author.mention}, giá trị không đúng !")
    elif int(money) > 1000000:
        await ctx.send(f"{ctx.message.author.mention}, mỗi lần chơi chỉ được tiêu ít hơn 1 triệu banana !")
    else:
        money_left_after = int(money_left_before) - int(money)
        await ctx.send(f"Bạn đã cược **{int(money):,d}** :banana: ... ")
        pts = random.randint(0,1)
        pts = random.randint(0,1)
        time.sleep(4)
        if pts == 0:
            await ctx.send(f"{ctx.message.author.mention}, bạn đã thua **{int(money):,d}** :banana: !")
            with open(f'assets\\information_id\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_left_after))
        elif pts ==1:
            money_give = int(money) * 2
            await ctx.send(f"{ctx.message.author.mention}, bạn đã thắng **{int(money_give):,d}** :banana: !")
            money_left_after = money_left_after + money_give
            with open(f'assets\\information_id\\{tag}.txt', 'w') as money_banana : 
                money_banana.write(str(money_left_after))
@client.command()
async def VAR(ctx,*,question):
    await ctx.send(f'{ctx.message.author.mention} using VAR :\nCHECKING VAR - POSSIBLE **{question}** ...')
    time.sleep(3)
    pts = random.randint(0,1)
    pts = random.randint(0,1)
    if pts == 0:
        await ctx.send(f'CHECKING VAR - POSSIBLE **{question}** IS FALSE')
    else:
        await ctx.send(f'CHECKING VAR - POSSIBLE **{question}** IS TRUE')
@client.command()
async def PhucSadBoiDiBanMaTuy(ctx):
    with open('assets\\image\\easter_egg_2.png', 'rb') as pic:
        picture = discord.File(pic)
    await ctx.send(f'{ctx.message.author.mention} coward.',file=picture)

@client.command(aliases=['shop','cuahang'])
async def hien_cua_hang(ctx, arg):
    if arg == 'menu':
        await ctx.send(
            ''':shopping_cart: **SHOP the zoo DISCORD SERVER**\n
            :arrow_right: If you want to purchase **gun or bullet**, using the argument **"gun"** after **tz!shop/cuahang**
            :arrow_right: If you want **gun license test**, using the argument **"gun_license"** after **tz!shop/cuahang**
            :arrow_right: ATTENTION: **EVERYTHING HERE IS IN BETA VERSION !** 
            ''')
    elif arg == 'gun':
        await ctx.send("coward.")
    elif arg == 'gun_license':
        await ctx.send("solve this : -5 x y = ym")
    else: 
        await ctx.send("Wrong argument, try again !")
client.run('MTA0MDk2NjQ1MjE4MzgzODg0Mg.GbzgrI.60_-FU-uEZp5Eq45ewz9pxhUdNywew9Td6p-D8')
