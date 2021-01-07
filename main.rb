require 'net/http'
require 'json'
# Make HTTP Request
response = Net::HTTP.get_response('site.api.espn.com', '/apis/site/v2/sports/football/nfl/scoreboard')

# Extract Data
data = JSON.parse(response.body)
eventdata = data["events"]

# Make Final Variable
finaldata = []

# Process Live Game / Non Live Game Data
for currentdata in eventdata do
  newdata = {}
  livegame = false
  begin
    for compteam in currentdata["competitions"][0]["competitors"] do
      compdata = currentdata["competitions"][0]["competitors"]
      if compteam['winner'] == true then
        newdata["winningteam"] = compteam["team"]["displayName"]
        newdata["winningteamscore"] = compteam["score"]
      end
      if compteam['winner'] == false then
        newdata["losingteam"] = compteam["team"]["displayName"]
        newdata["losingteamscore"] = compteam["score"]
      end
    end
  rescue KeyError
  livegame = true
  end
  if livegame == false then
    newdata["name"] = currentdata["name"]
    newdata["shortname"] = currentdata["shortName"]
    newdata["date"] = currentdata["date"]
    finaldata.append(newdata)
  end
end

# Final Output
print(finaldata)
