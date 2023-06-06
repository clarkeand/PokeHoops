"""Models for the Pokéhoops app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class NBAPlayer(db.Model):
    """A single player.
    player_id,player_name,team_id,player_position,poked_score,player_image"""

    __tablename__ = "nbaplayers"

    player_id = db.Column(db.Integer,primary_key=True)
    player_name = db.Column(db.String, nullable = False)
    team_id = db.Column(db.String, ForeignKey('teams.team_id'), nullable = False)
    player_position = db.Column(db.String, nullable = False)
    poked_score = db.Column(db.Float)
    player_image = db.Column(db.String)

    team = db.relationship("Team", backref="nbaplayers")

    def __repr__(self):
        return f'<NBAPlayer player_id={self.player_id} player_name={self.player_name} team_id={self.team_id} player_position={self.player_position}poked_score={self.poked_score}>'
    
class Team(db.Model):
    """A single NBA team.
    team_id,team_name"""

    __tablename__ = "teams"

    team_id = db.Column(db.String, primary_key=True)
    team_name = db.Column(db.String)

    def __repr__(self):
        return f"<Team team_id={self.team_id} team_name={self.team_name}>"
    
class User(db.Model):
    """A single user.
    user_id,email,password"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} password={self.password}>"

class UserPlayer(db.Model):
    """A User's Players. (favorite player)
    user_player_id,player_id,user_id,player,user"""

    __tablename__ = "user_players"

    user_player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    player_id = db.Column(db.Integer, ForeignKey('nbaplayers.player_id'))
    user_id = db.Column(db.Integer, ForeignKey('users.user_id'))

    player = db.relationship("NBAPlayer", backref="users")
    user = db.relationship("User", backref="nbaplayers")

    def __repr__(self):
        return f"<UserPlayer user_player_id={self.user_player_id} player_id={self.player_id} user_id={self.user_id}>"

def connect_to_db(flask_app, db_uri="postgresql:///favorites", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from PokeHoops.server import app

    connect_to_db(app)