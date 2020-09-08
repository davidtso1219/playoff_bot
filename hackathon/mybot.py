import discord
from random import randrange
import requests
import datetime
import json

with open('/Users/petertso/Desktop/_Foothill/CS/club/hackathon/series_data.json') as f:
    series_data = json.load(f)

client = discord.Client()

# url = 'https://www.balldontlie.io/api/v1/games?seasons=2019&start_date=2020-08-18&page='
# response1 = requests.get(url + '1')
# meta = response1.json()['meta']
# pages = meta['total_pages']
# data = response1.json()['data']

# for i in range(2, pages + 1):
#     data += requests.get(url + str(i)).json()['data']

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
        await message.channel.send("You can ask me with the following commands: \n\t*nba report* \n\t*nba who wins? (team) and (team)*")

    if message.content.startswith('nba who wins?'):
        try:
            mylist = message.content.split()[3:]
            team1 = mylist[0]
            team2 = mylist[2]

            for series in series_data['data']:
                if (team1.lower() in series['higher_seed'].lower() and team2.lower() in series['lower_seed'].lower()) or (team2.lower() in series['higher_seed'].lower() and team1.lower() in series['lower_seed'].lower()):
                    result = series['result']
                    text = f"The result is **{series['result']}**"
                    if '4' in result:
                        if result[0] == '4':
                            text += f"\n**{series['higher_seed']}** wins the series!!!"
                        else:
                            text += f"\n**{series['lower_seed']}** wins the series!!!"
                    else:
                        if int(result[0]) > int(result[4]):
                            text += f"\n**{series['higher_seed']}** is leading the series"
                        elif int(result[0]) < int(result[4]):
                            text += f"\n**{series['lower_seed']}** is leading the series"
                        else:
                            text += "\n**Series Tied**"
                        text += "\n*The series hasn't ended..*"

                    break

            else:
                await message.channel.send('There is no matching series..')
                return

            await message.channel.send(text)
        except IndexError:
            await message.channel.send('*The format is wrong..*')
        
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
                text = f"------------------\n*Game {num}*\n"
        
                home = game['home_team']
                visitor = game['visitor_team']
                text += f"**{home['full_name']}** vs. **{visitor['full_name']}\n**"
                text += f"\tHome Score: **{game['home_team_score']}**\n"
                text += f"\tVisitor Score: **{game['visitor_team_score']}**\n"

                num += 1
                
                await message.channel.send(text)
                today_has_game = True 

        if not today_has_game:
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

client.run('NzUwMDc2Nzg2MDI4NzA3ODYx.X01RcQ.K_XXRWpsQG-85ngcZFVtZf2Ht6o')