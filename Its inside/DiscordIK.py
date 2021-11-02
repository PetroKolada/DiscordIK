import discord, asyncio
from discord.ext import commands
import os
from ctypes import windll, create_string_buffer


client = commands.Bot(command_prefix='!')
os.system('')  

token = open('Token.txt', 'r')
h = windll.kernel32.GetStdHandle(-12)
csbi = create_string_buffer(22)
res = windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)

if res:
    import struct
    (bufx, bufy, curx, cury, wattr,
     left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
    sizex = right - left + 1
    sizey = bottom - top + 1
else:
    sizex, sizey = 80, 25 



async def send_msg():
        await client.wait_until_ready()
        servers = list(client.guilds)
        kanals = []
        for guild in servers:
                for channel in guild.text_channels:
                        kanals.append(channel)
        kanal = "[NOTHING]"    
        os.system('cls' if os.name == 'nt' else 'clear')
        msg_sent = False
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выбрано - [ Выберите действие ]")
        print("Выберите сервер ╠"+("═"*(sizex-1)))
        print(" ")
        count = 1
        for i in servers:
                print(str(count)+")", str(i))
                count=count+1
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        servchoose = int(input(">"))
        count = 1
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выбран сервер - " + "[" + str(servers[servchoose-1]) + "]")
        print("Выберите канал ╠"+("═"*(sizex-1)))
        print(" ")
        kanals = []
        for x in servers[servchoose-1].text_channels:
                print(str(count)+")", str(x))
                kanals.append(x)
                count=count+1
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        kanalchoose = int(input(">"))
        kanal = kanals[kanalchoose-1]
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Выбран канал - " + "[" + str(kanal) + "]")
        print("В начале сообщения писать дискриминатор или ID? ╠"+("═"*(sizex-1)))
        print(" ")
        print("1) Дискриминатор")
        print("2) ID")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        Desc = int(input(">"))
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
                if msg_sent == False:
                        count = sizey-7
                        jopa = []
                        jopa2 = []
                        jopa3 = []
                        os.system('cls' if os.name == 'nt' else 'clear')
                        messages = await kanal.history(limit=sizey-6).flatten()
                        print("╔"+("═"*(sizex-1)))
                        print(f"║Пишем в -", kanal, "/ сервера -", servers[servchoose-1])
                        print("╠"+("═"*(sizex-1)))
                        for i in messages:
                                jopa.append(str(i.author.name))
                                jopa2.append(str(i.content))
                                if Desc == 1:
                                    jopa3.append(str(i.author.discriminator))
                                elif Desc == 2:
                                    jopa3.append(str(i.author.id))
                                    
                        for x in jopa:
                                print(f"║",jopa3[count], " ● ", jopa[count], "-", jopa2[count])
                                count = count - 1
                        await client.wait_until_ready()
                        channsl = client.get_channel(kanal.id)
                        print("╚"+"═"*(sizex-1))
                        text = str(input(" >"))
                        if text != '99' and not '/kick' in text and not '/ban' in text:
                                await channsl.send(text)
                                msg_sent = True
                        elif text == '99':
                                msg_sent = True

                        elif '/kick' in text:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            try:
                                guild = client.get_guild(servers[servchoose-1].id)
                                print(' Пытаемся выгнать человека....')
                                print(int(text[6:len(text)]), "- Ник:")
                                bker = await guild.fetch_member(str(text[5:len(text)]))
                                print(int(text[6:len(text)]), "- Ник:", bker)
                                await kicker.kick()
                                print("",kicker, "Был выгнан")
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                            except ValueError:
                                print(' Попытка не удалась.')
                                print(' Введено было не верное значение.')
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                                bker = ""
                            except discord.errors.NotFound:
                                print(" Попытка не удалась.")
                                print(" Пользователь не найден")
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                                bker = ""
                            except discord.errors.Forbidden:
                                print(" Попытка не удалась")
                                print(" Недостаточно прав")
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                                bker = ""
                    
                        elif '/ban' in text:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            try:
                                guild = client.get_guild(servers[servchoose-1].id)
                                print(' Пытаемся забанить человека....')
                                kicker = await guild.fetch_member(str(text[4:len(text)]))
                                print(int(text[6:len(text)]), "- Ник:", kicker)
                                await kicker.kick()
                                print("",kicker, "Был забанен")
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                            except ValueError:
                                print(' Попытка не удалась.')
                                print(' Введено было не верное значение.')
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                                kicker = ""
                            except discord.errors.NotFound:
                                print(" Попытка не удалась.")
                                print(" Пользователь не найден")
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                                kicker = ""
                            except discord.errors.Forbidden:
                                print(" Попытка не удалась")
                                print(" Недостаточно прав")
                                await asyncio.sleep(2)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                msg_sent = True
                                kicker = ""
                                

                else:
                    msg_sent = False






@client.event
async def on_ready():
        print(client.user)
        print('Запущен....')
        print(sizex, sizey)
        client.loop.create_task(send_msg())
client.run(token.read(), bot = True)
