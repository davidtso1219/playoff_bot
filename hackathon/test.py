import json

with open('/Users/petertso/Desktop/_Foothill/CS/club/hackathon/series_data.json') as f:
    data = json.load(f)

data = data['data']

for series in data:
    print(series['conference'])