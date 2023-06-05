"""Script to seed database."""

import os
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playerfantasyprofile
import time

import crud
import model
import server

os.system("dropdb favorites")
os.system('createdb favorites')
model.connect_to_db(server.app)
model.db.create_all()

player_dict = players.get_active_players()
team_dict = teams.get_teams()

#Create Teams
for team in team_dict: 
    team_id = team['abbreviation']
    team_name = team['full_name']
    created_team = crud.create_team(team_id,team_name)
    model.db.session.add(created_team)
#Create Free Agent 'Team' 
created_team =  crud.create_team('F_A',"Free Agent")
model.db.session.add(created_team)

# Create Players
for player in player_dict: 
    print(player)
    # Get player name/id from the common player dictionary. 
    player_id  = player['id']
    player_name = player['full_name']
    # We need complex dictionary to pull each players 3 digit team identifier. If player is a free agent set to free agent team.  
    player_info = commonplayerinfo.CommonPlayerInfo(f'{player_id}')
    player_info = player_info.get_normalized_dict()
    player_info = player_info.get('CommonPlayerInfo')[0]
    if player_info['TEAM_ABBREVIATION'] != None:
        team_id = player_info['TEAM_ABBREVIATION']
    else: 
        team_id = 'F_A'
    time.sleep(1)
    #Set player position to default to NA
    player_position = player_info['POSITION']
    # Set each POKED score to a value of 0 for now. 
    poked_score = 0
    # Set each image to Null for now. 
    player_image = "N/A"

    #user crud create_a_player function to create a player to add to our DB. 
    created_player = crud.create_player(player_id,player_name,team_id,player_position,poked_score,player_image)
    model.db.session.add(created_player)
    time.sleep(.001) 


model.db.session.commit()