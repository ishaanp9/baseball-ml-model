import statsapi
from smallHelperFunctions import *

#NOTE TO SELF: Use MLB-Stats-API endpoints to find extra data --> like venue, umpire data, contextData, etc

#core functions

# Takes in a string abv or full form of a city name and returns the associated teamId
def get_team_id(cityName): 
    team = statsapi.lookup_team(cityName)
    teamId = team[0]['id']
    return teamId

# Takes in string playerFirstName and playerLastName and returns the asscoiated playerId
def get_player_id(playerFirstName, playerLastName): 
    player = statsapi.lookup_player(playerLastName + ',')
    try: 
        playerId = player[0]['id']
        for count,  x in enumerate(player):
            if (playerFirstName.lower() in x.get('firstName').lower()):
                playerId = player[count]['id']
        return playerId
    except:
        return None

#how to get the best offensive teams
#how to get the best defensive teams

# def get_team_averages(cityName, groupType):

#     if (groupType == "hitting"): 


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



# compiles team data based on given teamName (ex.mariners, rangers, astros, etc)
# organizes data in nested dictionaries 
# categorizes data based on position --> pitcher or non-pitcher
def compileTeamData(teamName):
    playerStatistics = {}
    teamRosterFetcher = getTeamRoster(teamName)

    for x in range(len(teamRosterFetcher)):
        splitPlayerString = teamRosterFetcher[x].split()
        playerPosition = splitPlayerString[1] #player postion (ex -> P or 1B)
        if (playerPosition == "P"):
            playerPositionString = 'pitching'
        else:
            # Add fielding component later
            playerPositionString = 'hitting'
        playerFirstName = splitPlayerString[2] #player First Name
        playerLastName = splitPlayerString[len(splitPlayerString) - 1] #player Last Name
        playerStatistics[teamRosterFetcher[x]] = {} 
        # if player doesn't exsist in database (ex. Andres Munoz)
        if get_player_id(playerFirstName, playerLastName) != None:
            careerStatHolder = statsapi.player_stats(get_player_id(playerFirstName, playerLastName), playerPositionString, 'yearByYear').split()
            beginningPlayerStatIndex = rindex(careerStatHolder, "YearByYear") + 2
        for count, stat in enumerate(careerStatHolder[beginningPlayerStatIndex:: 2]) :   
            playerStatistics[teamRosterFetcher[x]][stat] = careerStatHolder[beginningPlayerStatIndex + (count * 2) + 1]

    return playerStatistics

print(compileTeamData("royals"))

    


