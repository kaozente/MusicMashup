import json
from pprint import pprint
json_data=open('clutchconcerts.json')

data = json.load(json_data)
# pprint(data)
# json_data.close()

print data["resultsPage"]["results"]["event"][0]["displayName"]