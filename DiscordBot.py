import discord

TOKEN = 'XXXXXXXXXXXXXX'

client = discord.Client()



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    list1 =["hello bot", "hello loz bot"]

    for i in range(len(list1)):
        if list1[i] in message.content.lower():
            msg1 = 'Hello loz {0.author.mention}'.format(message)
            await message.channel.send(msg1)
            break

    list2 =["yasuo", "daxua", "đấng"]  
    for i in range(len(list2)):
        if list2[i] in message.content.lower():
            msg1 = 'solo yasuo với tao k'.format(message)
            await message.channel.send(msg1)
            break

    
        
    list3 = ["loz", "đĩ", "cặc", "cax", "địt", "du ma", "dm", "lồn", "cax"]
    for i in range(len(list3)):
        if list3[i] in message.content.lower():
            msg1 = 'K được nói tục chửi bậy {0.author.mention}'.format(message)
            await message.channel.send(msg1)
            break
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------')

client.run(TOKEN)  # Where 'TOKEN' is your bot token
