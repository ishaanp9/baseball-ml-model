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
            if (playerFirstName.lower() in x.get('firstName').lower()):
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
            careerStatHolder = statsapi.player_stats(get_player_id(playerFirstName, playerLastName), playerPositionString, 'yearByYear').split()
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
def get_team_averages(teamName, statType):
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
    # returns avg returned to two decimal values.
    return round(statTotal / count, 2)


# print(get_Team_Roster("astros"))
print(get_team_averages("astros", "homeRuns:")) 
print(get_team_averages("yankees", "homeRuns:"))
print("My program took,", int(time.time() - start_time), "seconds to run")
    


