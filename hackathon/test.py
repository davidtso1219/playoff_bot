import requests

url = 'https://www.balldontlie.io/api/v1/games?seasons=2019&start_date=2020-08-18&page='
response1 = requests.get(url + '1')
meta = response1.json()['meta']
pages = meta['total_pages']
data = response1.json()['data']

for i in range(2, pages + 1):
    data += requests.get(url + str(i)).json()['data']

num = 1

for game in data:


    if game['period']:
        
        print(f"Game {num}")
        
        home = game['home_team']
        visitor = game['visitor_team']

        text = f"Date: {game['date']}\n"
        text += f"Season: {game['season']}-{game['season'] + 1}\n"
        text += f"{home['full_name']} vs. {visitor['full_name']}\n"

        text += f"Home Score: {game['home_team_score']}\n"
        text += f"Visitor Score: {game['visitor_team_score']}\n"

        num += 1

        print(text)
