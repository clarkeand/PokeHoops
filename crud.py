from model import db, User, NBAPlayer, Team, UserPlayer, connect_to_db

def create_user(email, password):
    """Create and return a new user."""
    user = User(email=email, password=password)
    return user

def create_player(player_id,player_name,team_id, player_position, poked_score,player_image):
    """Create and return a new player."""
    player = NBAPlayer(player_id = player_id, player_name=player_name,team_id = team_id,
                player_position = player_position,poked_score = poked_score,player_image=player_image)
    return player

def create_team(team_id, team_name):
    """Create and return a new team."""
    team = Team(team_id = team_id, team_name = team_name)
    return team 

def create_user_player(player_id, user_id):
    """Create and return a new userPlayer."""
    user_player = UserPlayer(player_id = player_id, user_id = user_id)
    return user_player 

def get_players():
    """Return all players."""

    return NBAPlayer.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)