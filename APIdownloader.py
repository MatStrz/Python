import requests
import json
import pprint
import webbrowser
from datetime import datetime, timedelta


timeBefore = timedelta(days=7)
searchTime = datetime.today()-timedelta(days=7)

# Parametry określające porządek otwieranych pytań. (Najwyżej punktowane, malejąco, z ostatniego tygodnia)
params = {
    "site" : "stackoverflow",
    "sort" : "votes",
    "order" : "desc",
    "fromdate" : int(searchTime.timestamp()),
    "tagged" : "python",
    "min" : 4
    }

# Skrypt pobierający i tłumaczący stronę z JSON i zapisujący ją w questions
r = requests.get("https://api.stackexchange.com/2.3/questions", params)


try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    for question in questions["items"]:
        #print(question)
        print(question["link"])
        #webbrowser.open_new_tab(question["link"])
