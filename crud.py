from model import db, User, NBAPlayer, Team, UserPlayer, connect_to_db
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playerfantasyprofile

#import needed dictionaries
player_dict = players.get_active_players()
team_dict = teams.get_teams()
#get dame's playerid and print his player profile from the api
dame = players.find_players_by_full_name('Damian Lillard')
print(dame)
print(team_dict)
#get dame's team info from player info since it isn't available in the regualar player endpoint in the api. 
#alternatively I can pull everything straight from this dict. 
dame_id = dame[0]['id']
player_info = commonplayerinfo.CommonPlayerInfo(f'{dame_id}')
player_info = player_info.get_normalized_dict()
player_info = player_info.get('CommonPlayerInfo')[0]
print(player_info)
team_id = player_info['TEAM_ABBREVIATION']
print(team_id)
#found a fanatasy nba library I can use to build the poked score. 
#There is a total season function or you can do a lastngames if 
#I want to have it fluctuate based on their last games. 
# dame_fantasy_info = playerfantasyprofile.PlayerFantasyProfile(player_id=dame_id)
# dame_fantasy_info = dame_fantasy_info.get_normalized_dict()
# print(dame_fantasy_info)

# def create_user(email, password):
#     """Create and return a new user."""
#     user = User(email=email, password=password)
#     return user

# if __name__ == '__main__':
#     from server import app
#     connect_to_db(app)