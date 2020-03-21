import discord
import json
from collections import OrderedDict
import pprint
import re
import bot_token

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event



async def on_message(message):
    # 「図鑑」で始まるか調べる
    if re.match('.+の図鑑$', message.content):
        json_open = open('pokedex_zen.json', 'r')
        json_load = json.load(json_open)
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            
            # メッセージを書きます
            m = message.content[0:len(message.content)-3]
            
            # メッセージが送られてきたチャンネルへメッセージを送ります
            if m in json_load:
                message_send = "```"
                for key, value in json_load[m].items():
                    if key == 'No':
                        message_send = message_send + '%s.%s'%(key, value) + ' '
                    elif key == 'ポケモン名':
                        message_send = message_send + '%s'%(value) + " \n"  + ' HP 攻撃 防御 特攻 特防 素早 合計\n'
                    elif key == 'HP' :    
                        message_send = message_send + '%3d'%(int(value))
                    else:    
                        message_send = message_send + '%4d'%(int(value))

                message_send = message_send + "```"
                print('0 ' + m)
            else:
                message_send = "そんなポケモンはいません"
                print('1 ' + m)    

            
            
            await message.channel.send(message_send)
                
client.run(bot_token.TOKEN)
