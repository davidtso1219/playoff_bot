import discord
from random import randrange
import requests
import datetime

client = discord.Client()

url = 'https://www.balldontlie.io/api/v1/games?seasons=2019&start_date=2020-08-18&page='
response1 = requests.get(url + '1')
meta = response1.json()['meta']
pages = meta['total_pages']
data = response1.json()['data']

for i in range(2, pages + 1):
    data += requests.get(url + str(i)).json()['data']

# Event handlers
@client.event
async def on_ready():
    print('Hey this is {0.user} '.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'nba':
        await message.channel.send('Hey I am the bot helping you get the data of NBA playoffs 2020')
        await message.channel.send("You can ask me with the following commands: \n\treport")

    if message.content == 'nba report':

        # def report(today=datetime.date.today()):
        #     today_url = f'https://www.balldontlie.io/api/v1/games?seasons=2019&start_date={today}&end_date={today}'
        #     today_response = requests.get(today_url)
        #     data = today_response.json()['data']

        #     num = 1

        #     for game in data:
        #         if game['period']:
        #             text = f"\nGame {num}\n"
            
        #             home = game['home_team']
        #             visitor = game['visitor_team']
        #             text += f"{home['full_name']} vs. {visitor['full_name']}\n"
        #             text += f"\tHome Score: {game['home_team_score']}\n"
        #             text += f"\tVisitor Score: {game['visitor_team_score']}\n"

        #             num += 1
                    
        #             await message.channel.send(text)
        #     else:
        #         report(today - datetime.timedelta(days=1))

        # report()
        today = datetime.date.today()
        today_url = f'https://www.balldontlie.io/api/v1/games?seasons=2019&start_date={today}&end_date={today}'
        today_response = requests.get(today_url)
        data = today_response.json()['data']

        num = 1

        for game in data:
            if game['period']:
                text = f"\nGame {num}\n"
        
                home = game['home_team']
                visitor = game['visitor_team']
                text += f"{home['full_name']} vs. {visitor['full_name']}\n"
                text += f"\tHome Score: {game['home_team_score']}\n"
                text += f"\tVisitor Score: {game['visitor_team_score']}\n"

                num += 1
                
                await message.channel.send(text)  
        else:
            await message.channel.send("There are no games to report today..")
            await message.channel.send("Let me show you yesterday's games")

            yesterday = today - datetime.timedelta(days=1)
            yesterday_url = f'https://www.balldontlie.io/api/v1/games?seasons=2019&start_date={yesterday}&end_date={yesterday}'
            yesterday_response = requests.get(yesterday_url)
            data = yesterday_response.json()['data']

            for game in data:
                if game['period']:
                    text = f"\nGame {num}\n"
            
                    home = game['home_team']
                    visitor = game['visitor_team']
                    text += f"{home['full_name']} vs. {visitor['full_name']}\n"
                    text += f"\tHome Score: {game['home_team_score']}\n"
                    text += f"\tVisitor Score: {game['visitor_team_score']}\n"

                    num += 1
                    
                    await message.channel.send(text)

client.run('NzUwMDc2Nzg2MDI4NzA3ODYx.X01RcQ.meIuOwdD3h0N6X16U_ikGBzGC1A')