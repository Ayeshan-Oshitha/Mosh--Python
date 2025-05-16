# pylint: disable=all

import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}

params = {
    "term": "Barber",
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
print(businesses)

for x in businesses:
    print(x["name"])

# return the list of business which has 4 ratings or more

names = [business["name"]
         for business in businesses if businesses["rating"] > 4.5]
print(names)
