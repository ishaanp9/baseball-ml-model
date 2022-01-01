import statsapi
import time
start_time = time.time()
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
        playerId = None
        for count,  x in enumerate(player):
            if (playerFirstName.lower() in x.get('useName').lower()):
                playerId = player[count]['id']
        return playerId
    except:
        return None

def get_Team_Roster(teamName):
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
def compile_Team_Data(teamName):
    playerStatistics = {}
    teamRosterFetcher = get_Team_Roster(teamName)

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
            # print(playerFirstName + playerLastName)
            # Some extreme cases like Alberto Rodriguez who have ids but have no stats
            # NOTE: Hacky Code but quick fix throwing into a try except 
            try:
                careerStatHolder = statsapi.player_stats(get_player_id(playerFirstName, playerLastName), playerPositionString, 'yearByYear').split()
            except:
                continue
            if "YearByYear" in careerStatHolder:
                beginningPlayerStatIndex = rindex(careerStatHolder, "YearByYear") + 2
                for count, stat in enumerate(careerStatHolder[beginningPlayerStatIndex:: 2]) :
                    statValue = (careerStatHolder[beginningPlayerStatIndex + (count * 2) + 1])
                    # checks if statValue is a valid string that can be turned into a number. 
                    # if not it will not do anything with it.
                    if '-' not in statValue:
                        playerStatistics[teamRosterFetcher[x]][stat] = float(statValue)
                    else: 
                        playerStatistics[teamRosterFetcher[x]][stat] = statValue
    return playerStatistics

# stat - hitting, pitching, fielding or specific like homeRuns: or rbi:
# returns team average for a particular statType
# NOTE: Still need to finish total hitting, fielding, or pitching stats
# NOTE: when result is total it will calculate total of current roster!!! So it will not count those who are not on the roster now!
# result can be total or avg
def get_team_averages(teamName, statType, result):
    statTotal = 0 # total of given stat type
    count = 0 # maintains count to avg later on
    teamData = compile_Team_Data(teamName)
    for key in teamData.keys():
        if statType in teamData[key]:
            statValue = teamData[key][statType]
            # checks if the statValue is a float -> this eliminates string values such as ".---" and "-.--" to be considered
            if type(statValue) == float:
                statTotal += statValue
                count += 1
    
    if result.lower() == "total":
        return round(statTotal)
    elif result.lower() == "average":
    # returns avg returned to two decimal values.
        return round(statTotal / count, 2)
    else:
        raise Exception("result parameter type was not total or average")


# adds team collections and players to the db 
# NOTE: only should be called in db.py!
def add_team_players_to_db(teamName):
    team = compile_Team_Data(teamName)
    playerlistdb = []    

    for player in team.keys():
        teamPlayerdb = {}
        playerSplit = player.split()
        uniformNumber = playerSplit[0]
        position = playerSplit[1]
        fullName = ""
        for index in range(2, len(playerSplit)):
            fullName += playerSplit[index] + " "
        fullName = fullName.strip()

        teamPlayerdb["Name"] = fullName
        teamPlayerdb["Position"] = position
        teamPlayerdb["Uniform Number"] = uniformNumber
        teamPlayerdb["Statistics"] = {}
        for stat in team[player]:
            teamPlayerdb["Statistics"][stat] = team[player][stat]

        playerlistdb.append(teamPlayerdb)

    return playerlistdb

# print(("J.P. Crawford").split())

# print(statsapi.lookup_player("Rodriguez,"))
# print( statsapi.player_stats(543063, 'hitting', 'yearByYear') )
# print(get_player_id("alberto", "rodriguez"))
print(compile_Team_Data("mariners"))
print("My program took,", int(time.time() - start_time), "seconds to run")
    


