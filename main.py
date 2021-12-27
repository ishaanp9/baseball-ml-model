import statsapi

#NOTE TO SELF: Use MLB-Stats-API endpoints to find extra data --> like venue, umpire data, contextData, etc

# Takes in a string abv or full form of a city name and returns the associated teamId
def get_team_id(cityName): 
    team = statsapi.lookup_team(cityName)
    teamId = team[0]['id']
    return teamId

# Takes in string playerLastName and returns the asscoiated playerId
def get_player_id(playerLastName): 
    player = statsapi.lookup_player(playerLastName + ',')
    playerId = player[0]['id']
    return playerId

#how to get the best offensive teams
#how to get the best defensive teams

# def get_team_averages(cityName, groupType):

#     if (groupType == "hitting"): 

# print(statsapi.player_stats(get_player_id("Ramirez"), group="[hitting,pitching,fielding]", type="season"))


# try:
#     print(statsapi.player_stat_data(get_player_id('austin nola'), group="[hitting,pitching,fielding]", type="season"))
# except:
#      print("Invalid Player Given")

#retrieves team roster in a list item
def getTeamRoster(teamName):
    rosterString = statsapi.roster(get_team_id(teamName)) 
    splitRoster = rosterString.split()
    teamRosterList = []
    playerData = ""
    for count, x in enumerate(splitRoster):
        if "#" in x and count != 0 :
            teamRosterList.append(playerData.strip())
            playerData = ""
        playerData += x + " "

    return teamRosterList

print(getTeamRoster("mariners"))
#get last item from year to year to compile team stats
print( statsapi.player_stats(get_player_id("kelenic"), 'hitting', 'yearByYear') )

# print(statsapi.get('team_roster', {'teamId': get_team_id("mariners")}))
# print( statsapi.league_leaders('homeruns',statGroup='hitting',limit=10,season=2021) )
# teamLeader = statsapi.team_leader_data(teamId, "homeruns")
# print(teamLeader);

