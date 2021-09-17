import discord
import discord.ext.commands
import os

# https://discord.com/oauth2/authorize?client_id=888215419951927326&permissions=515396566016&scope=bot

api_key = "your api key"

client = discord.Client()

def bot():
    @client.event
    async def on_ready():
        print('Boombox-news logged in as: {0.user}'.format(client))

        channel = client.get_channel(int(your channel id))

        title = input("Please enter a title for the news: ")
        link = input("Please enter a link for the news: ")
        info = input("What would you like to say (markdown is supported): ")

        if ("\\n" in info):
            info = info.split("\\n")

        embedVar = discord.Embed(title=title, description=link, color=discord.Color.blue())
        embedVar.set_thumbnail(url="https://i.imgur.com/X0kijbq.png")

        if (type(info) is list):
            for i in range(len(info)):
                if (i == 0):
                    embedVar.add_field(name="Info: ", value=info[0], inline=False)
                else:
                    embedVar.add_field(name="​", value=info[i], inline=False)
        else:
            embedVar.add_field(name="Info: ​", value=info, inline=False)
            
        await channel.send(embed=embedVar) 
        os._exit(0)


bot()

# required: discord run call to authorise bot perms
client.run(api_key)
