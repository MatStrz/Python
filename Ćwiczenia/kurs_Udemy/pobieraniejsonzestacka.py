import requests
import json
import pprint
import webbrowser


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
    webbrowser.open(questions)
