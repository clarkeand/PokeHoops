"""Script to seed database."""

import os
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo
import time

import crud
import model
import server

os.system("dropdb favorites")
os.system('createdb favorites')
model.connect_to_db(server.app)
model.db.create_all()

#Declare contants for POKED score. 
NBA_PPG_MEAN = 10.8
NBA_PPG_STD = 5
NBA_APG_MEAN = 2.36
NBA_APG_STD = 3
NBA_RPG_MEAN = 4.26
NBA_RPG_STD = 2

#Import teams from API
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


player_dict = players.get_active_players()
#Create Players
for player in player_dict: 
    print(player)
    #Get player name/id from the common player dictionary. 
    player_id  = player['id']
    player_name = player['full_name']
    #We need complex dictionary to pull each players 3 digit team identifier. If player is a free agent set to free agent team.  
    common_info = commonplayerinfo.CommonPlayerInfo(f'{player_id}')
    player_info = common_info.get_normalized_dict()
    player_info = player_info.get('CommonPlayerInfo')[0]
    if player_info['TEAM_ABBREVIATION'] != "":
        team_id = player_info['TEAM_ABBREVIATION']
    else: 
        team_id = 'F_A'
    #Set player position to default to NA
    player_position = player_info['POSITION']
    #Set each POKED score to a value of 0 for now. 
    player_stats = common_info.player_headline_stats.get_dict()
    if player_stats['data'] != []: 
        player_ppg = player_stats['data'][0][3]
        player_apg = player_stats['data'][0][4]
        player_rpg = player_stats['data'][0][5]
        poked_score = round(((player_ppg-NBA_PPG_MEAN)/NBA_PPG_STD)+((player_apg-NBA_APG_MEAN)/NBA_APG_STD)+((player_rpg-NBA_RPG_MEAN)/NBA_RPG_STD),2)
    else: poked_score = -99.99
    print(poked_score)
    #Pull each player image from the NBA site. 
    player_image = f'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{player_id}.png'

    #User crud create_a_player function to create a player to add to our DB. 
    created_player = crud.create_player(player_id,player_name,team_id,player_position,poked_score,player_image)
    model.db.session.add(created_player)
    time.sleep(1)

model.db.session.commit()