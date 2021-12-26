import statsapi



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


try:
    print(statsapi.player_stat_data(get_player_id('austin nola'), group="[hitting,pitching,fielding]", type="season"))
except:
     print("Invalid Player Given")

print( statsapi.roster(get_team_id("seattle mariners")) )
# teamLeader = statsapi.team_leader_data(teamId, "homeruns")
# print(teamLeader);

