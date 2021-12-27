import statsapi


from smallHelperFunctions import *

#NOTE TO SELF: Use MLB-Stats-API endpoints to find extra data --> like venue, umpire data, contextData, etc

# Takes in a string abv or full form of a city name and returns the associated teamId
def get_team_id(cityName): 
    team = statsapi.lookup_team(cityName)
    teamId = team[0]['id']
    return teamId

# Takes in string playerFirstName and playerLastName and returns the asscoiated playerId
def get_player_id(playerFirstName, playerLastName): 
    player = statsapi.lookup_player(playerLastName + ',')
    playerId = player[0]['id']
    for count,  x in enumerate(player):
        if (playerFirstName.lower() in x.get('firstName').lower()):
            playerId = player[count]['id']
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

# print(getTeamRoster("mariners"))
#get last item from year to year to compile team stats


# print(statsapi.get('team_roster', {'teamId': get_team_id("mariners")}))
# print( statsapi.league_leaders('homeruns',statGroup='hitting',limit=10,season=2021) )
# teamLeader = statsapi.team_leader_data(teamId, "homeruns")
# print(teamLeader);



# Iterate through each player, fetch their first and last name to get playerStats using Id.
# Now we get index of most recent year
# we now use the player name and the index to populate the nested dictionary
# We convert the string integers into doubles
# We iterate by every two

playerStatistics = {}
teamRosterFetcher = getTeamRoster("mariners")

for x in range(len(teamRosterFetcher)):
    splitPlayerString = teamRosterFetcher[x].split()
    playerPosition = splitPlayerString[1] #player postion (ex -> P or 1B)
    playerFirstName = splitPlayerString[2] #player First Name
    playerLastName = splitPlayerString[len(splitPlayerString) - 1] #player Last Name
    playerStatistics[teamRosterFetcher[x]] = {} 
    print(playerPosition + " " + playerFirstName + " " + playerLastName)
    careerStatHolder = statsapi.player_stats(get_player_id(playerFirstName, playerLastName), 'pitching', 'yearByYear').split()
    beginningPlayerStatIndex = rindex(careerStatHolder, "gamesPlayed")
    for stat in careerStatHolder[beginningPlayerStatIndex:: 2] :
        poop = "pee"
        # playerStatistics[teamRosterFetcher[x]][stat] = stat + 1




    

# print(getTeamRoster("mariners"))
