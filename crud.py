from model import db, User, NBAPlayer, Team, UserPlayer, connect_to_db
from sqlalchemy import desc

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
    """Allow user to favorite a player."""
    user_player = UserPlayer.query.filter_by(player_id=player_id, user_id=user_id).first()
    if user_player is None:
        user_player = UserPlayer(player_id=player_id, user_id=user_id)
        db.session.add(user_player)
        db.session.commit()
    else: 
        user_player = None

    return user_player

def get_players():
    """Return all players."""
    return NBAPlayer.query.all()

def player_to_dict(player):
    """Transform a player SQLAlchemy object into a Python dictionary."""
    return {
        'player_id': player.player_id,
        'player_name': player.player_name,
        'team_id': player.team_id,
        'player_position': player.player_position,
        'poked_score': player.poked_score
    }

def get_players_by_team():
    """Return all players sorted by team."""
    players = NBAPlayer.query.order_by(NBAPlayer.team_id).all()
    return [player_to_dict(player) for player in players]

def get_players_by_position():
    """Return all players sorted by position."""
    players = NBAPlayer.query.order_by(NBAPlayer.player_position).all()
    return [player_to_dict(player) for player in players]

def get_players_by_POKED():
    """Return all players sorted by POKED in descending order."""
    players = NBAPlayer.query.order_by(desc(NBAPlayer.poked_score)).all()
    return [player_to_dict(player) for player in players]

def get_player_by_id(id):
    """Return a player."""
    return NBAPlayer.query.get(id)

def get_user_by_email(email):
    """Return a user by email."""
    user = User.query.filter(User.email == email).first()
    return user

def get_users_players(user):
    """Return all user's players"""
    users_id = user.user_id
    user_players = UserPlayer.query.filter(UserPlayer.user_id == users_id).all()
    return user_players

def get_teams():
    teams = Team.query.all()
    return teams

def get_team_by_id(team_id):
    team = Team.query.filter(Team.team_id == team_id).first()
    return team

def get_team_players(team_id):
    players = NBAPlayer.query.filter(NBAPlayer.team_id == team_id).all()
    return players

if __name__ == '__main__':
    from server import app
    connect_to_db(app)