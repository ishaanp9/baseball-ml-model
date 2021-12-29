import pymongo

from main import compile_Team_Data


# Playing Around with Mongodb

# NOTE: Task for 12/29/21
# Create MLB database
# Create collection for teams
# Create subcollection for individual teams
# Populate with players - with stats

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["MLB_Teams"]

# Collection of Individual MLB Teams


arizona_diamondbacks = mydb["Arizona Diamondbacks"]
atlanta_braves = mydb["Atlanta Braves"]
baltimore_orioles = mydb["Baltimore Orioles"]
boston_red_sox = mydb["Boston Red Sox"]
chicago_white_sox = mydb["Chicago White Sox"]
chicago_cubs = mydb["Chicago Cubs"]
cincinnati_reds = mydb["Cincinnati Reds"]
cleveland_guardians = mydb["Cleveland Guardians"]
colorado_rockies = mydb["Colorado Rockies"]
detroit_tigers = mydb["Detroit Tigers"]
houston_astros = mydb["Houston Astros"]
kansas_city_royals = mydb["Kansas City Royals"]
los_angeles_angels = mydb["Los Angeles Angels"]
los_angeles_dodgers = mydb["Los Angeles Dodgers"]
miami_marlins = mydb["Arizona Diamondbacks"]
milwaukee_brewers = mydb["Milwaukee Brewers"]
minnesota_twins = mydb["Minnesota Twins"]
new_york_yankees = mydb["New York Yankees"]
new_York_mets = mydb["New York Mets"]
oakland_athletics = mydb["Oakland Athletics"]
philadelphia_phillies = mydb["Philadelphia Phillies"]
pittsburgh_pirates = mydb["Pittsburgh Pirates"]
san_diego_padres = mydb["San Diego Padres"]
san_francisco_giants = mydb["San Francisco Giants"]
seattle_mariners = mydb["Seattle Mariners"]
st_louis_cardinals = mydb["St Louis Cardinals"]
tampa_bay_rays = mydb["Tampa Bay Rays"]
texas_rangers = mydb["Texas Rangers"]
toronto_blue_jays = mydb["Toronto Blue Jays"]
washington_nationals = mydb["Washington Nationals"]
# All the MLB Teams

# to dynamically populate use existing team data method

# mydict = {"name": "Ishaan Puri", "Position": "1B", "Uniform Number": "#41", "Statistics": {'gamesPlayed:': 4.0, 'gamesStarted:': 0.0, 'groundOuts:': 6.0, 'airOuts:': 4.0, 'runs:': 5.0, 'doubles:': 1.0, 'triples:': 0.0, 'homeRuns:': 1.0, 'strikeOuts:': 2.0, 'baseOnBalls:': 1.0, 'intentionalWalks:': 0.0, 'hits:': 7.0, 'hitByPitch:': 0.0, 'avg:': 0.368, 'atBats:': 19.0, 'obp:': 0.4, 'slg:': 0.579, 'ops:': 0.979, 'caughtStealing:': 0.0, 'stolenBases:': 0.0, 'stolenBasePercentage:': '.---', 'groundIntoDoublePlay:': 0.0, 'numberOfPitches:': 86.0, 'era:': 12.27, 'inningsPitched:': 3.2, 'wins:': 0.0, 'losses:': 0.0, 'saves:': 0.0, 'saveOpportunities:': 0.0, 'holds:': 0.0,
#                                                                                            'blownSaves:': 0.0, 'earnedRuns:': 5.0, 'whip:': 2.18, 'battersFaced:': 20.0, 'outs:': 11.0, 'gamesPitched:': 4.0, 'completeGames:': 0.0, 'shutouts:': 0.0, 'strikes:': 57.0, 'strikePercentage:': 0.66, 'hitBatsmen:': 0.0, 'balks:': 0.0, 'wildPitches:': 0.0, 'pickoffs:': 0.0, 'totalBases:': 11.0, 'groundOutsToAirouts:': 1.5, 'winPercentage:': '.---', 'pitchesPerInning:': 23.45, 'gamesFinished:': 2.0, 'strikeoutWalkRatio:': 2.0, 'strikeoutsPer9Inn:': 4.91, 'walksPer9Inn:': 2.45, 'hitsPer9Inn:': 17.18, 'runsScoredPer9:': 12.27, 'homeRunsPer9:': 2.45, 'inheritedRunners:': 2.0, 'inheritedRunnersScored:': 1.0, 'catchersInterference:': 0.0, 'sacBunts:': 0.0, 'sacFlies:': 0.0}}


x = seattle_mariners.insert_one(compile_Team_Data("mariners"))
# each team
# each player --> with their indivisual stats
