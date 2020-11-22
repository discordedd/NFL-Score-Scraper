# Imports
import requests
import csv

# Load Page
URL = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

REQUEST = requests.get(url=URL)

# Extract Data
DATA = REQUEST.json()
EVENTDATA = DATA["events"]

FINALDATA = []

for CURRENTDATA in EVENTDATA:
    NEWDATA = {}
    LIVEGAME = False
    try:
        for COMPTEAM in CURRENTDATA["competitions"][0]["competitors"]:
            COMPDATA = CURRENTDATA["competitions"][0]["competitors"]
            if COMPTEAM['winner'] == True:
                NEWDATA["winningteam"] = COMPTEAM["team"]["displayName"]
                NEWDATA["winningteamscore"] = COMPTEAM["score"]
            elif COMPTEAM['winner'] == False:
                NEWDATA["losingteam"] = COMPTEAM["team"]["displayName"]
                NEWDATA["losingteamscore"] = COMPTEAM["score"]
    except KeyError:
        LIVEGAME = True
    if LIVEGAME == False:
        NEWDATA["name"] = CURRENTDATA["name"]
        NEWDATA["shortname"] = CURRENTDATA["shortName"]
        NEWDATA["date"] = CURRENTDATA["date"]
        FINALDATA.append(NEWDATA)
    

# CSV WRITER
with open('scores.csv', mode='w') as csv_file:
    fieldnames = ["name", "shortname", "date", "winningteam","winningteamscore","losingteam","losingteamscore"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in FINALDATA:
        writer.writerow(i)
    
