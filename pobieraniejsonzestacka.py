import requests
import json
import pprint
"""

API - Application Programming Interface

Inter - pmiędzy
face - twarz

bankomat

minimalnie 15 punktów
posegregowana malejąca
z ostatniego tygodnia
kategorii python

"""

params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : "2019-08-20",
    "tagged" : "python",
    "min" : 15
}


r = requests.get("https://api.stackexchange.com/2.2/questions/", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    pprint.pprint(questions)

 



    

