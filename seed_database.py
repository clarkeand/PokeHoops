"""Script to seed database."""

import os
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playerfantasyprofile

import crud
import model
import server

os.system("dropdb favorites")
os.system('createdb favorites')
model.connect_to_db(server.app)
model.db.create_all()

player_dict = players.get_active_players()
team_dict = teams.get_teams()

# Create Players
for player in player_dict: 
    #print(player)
    # Get player name/id from the common player dictionary. 
    player_id  = player_dict[player]['id']
    player_name = player_dict[player]['full_name']
    # We need complex dictionary to pull each players 3 digit team identifier. 
    player_info = commonplayerinfo.CommonPlayerInfo(f'{player_id}')
    player_info = player_info.get_normalized_dict()
    player_info = player_info.get('CommonPlayerInfo')[0]
    team_id = player_info['TEAM_ABBREVIATION']
    # Set each POKED score to a value of 0 for now. 
    poked_score = 0
    # Set each image to Null for now. 
    player_image = "Null"

    #user crud create_a_player function to create a player to add to our DB. 
    player = crud.create_player(player_id,player_name,team_id,poked_score,player_image)
    model.db.session.add(player)

# Create Teams
model.db.session.commit()