import pymongo

from main import *


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
new_york_mets = mydb["New York Mets"]
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
                                                             




# x = seattle_mariners.insert_many(add_team_players_to_db)    

diamondbacks = arizona_diamondbacks.insert_many(add_team_players_to_db("diamondbacks"))
braves = atlanta_braves.insert_many(add_team_players_to_db("braves"))
orioles = baltimore_orioles.insert_many(add_team_players_to_db("orioles"))
red_sox = boston_red_sox.insert_many(add_team_players_to_db("boston"))
white_sox = chicago_white_sox.insert_many(add_team_players_to_db("white sox"))
cubs = chicago_cubs.insert_many(add_team_players_to_db("cubs"))
reds = cincinnati_reds.insert_many(add_team_players_to_db("reds"))
guardians = cleveland_guardians.insert_many(add_team_players_to_db("cleveland"))
rockies = colorado_rockies.insert_many(add_team_players_to_db("rockies")) 
tigers = detroit_tigers.insert_many(add_team_players_to_db("tigers"))
astros = houston_astros.insert_many(add_team_players_to_db("astros"))
royals = kansas_city_royals.insert_many(add_team_players_to_db("royals"))
angels = los_angeles_dodgers.insert_many(add_team_players_to_db("angels"))
dodgers = los_angeles_dodgers.insert_many(add_team_players_to_db("dodgers"))
marlins = miami_marlins.insert_many(add_team_players_to_db("marlins"))
brewers = milwaukee_brewers.insert_many(add_team_players_to_db("brewers"))
twins = minnesota_twins.insert_many(add_team_players_to_db("twins"))
yankees = new_york_yankees.insert_many(add_team_players_to_db("yankees"))
mets = new_york_mets.insert_many(add_team_players_to_db("mets"))
athletics = oakland_athletics.insert_many(add_team_players_to_db("athletics"))
phillies = philadelphia_phillies.insert_many(add_team_players_to_db("phillies"))
pirates = pittsburgh_pirates.insert_many(add_team_players_to_db("pirates"))
padres = san_diego_padres.insert_many(add_team_players_to_db("padres"))
giants = san_francisco_giants.insert_many(add_team_players_to_db("giants"))
mariners = seattle_mariners.insert_many(add_team_players_to_db("mariners")) 
cardinals = st_louis_cardinals.insert_many(add_team_players_to_db("cardinals"))
rays = tampa_bay_rays.insert_many(add_team_players_to_db("rays"))
rangers = texas_rangers.insert_many(add_team_players_to_db("rangers"))
blue_jays = toronto_blue_jays.insert_many(add_team_players_to_db("toronto"))
nationals = washington_nationals.insert_many(add_team_players_to_db("nationals"))