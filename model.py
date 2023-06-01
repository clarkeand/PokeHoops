"""Models for the Pokéhoops app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class NBAPlayer(db.Model):
    """A single player."""

    __tablename__ = "nbaplayers"

    player_id = db.Column(db.Integer,
                        primary_key=True)
    player_name = db.Column(db.String, nullable = False)
    team_id = db.Column(db.String, nullable = False)
    poked_score = db.Column(db.Integer)

    team = db.relationship("Team", backref="nbaplayers")

    def __repr__(self):
        return f'<NBAPlayer player_id={self.player_id} player_name={self.player_name} team_id={self.team_id} poked_score={self.poked_score}>'
    
class Team(db.Model):
    """A single NBA team."""

    __tablename__ = "teams"

    team_id = db.Column(db.String, primary_key=True)
    team_name = db.Column(db.String)
    team_size = db.Column(db.Integer)

    def __repr__(self):
        return f"<Team team_id={self.team_id} team_name={self.team_name} team_size={self.team_size}>"
    
class User(db.Model):
    """A single user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, nullable = False)
    password = db.Column(db.Integer, nullable = False)

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email} password={self.password}>"

class UserPlayer(db.Model):
    """A User's Players."""

    __tablename__ = "user_players"

    user_player_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    player_id = db.Column(db.Integer)
    user_id = user_id = db.Column(db.Integer)

    player = db.relationship("NBAPlayer", backref="users")
    user = db.relationship("User", backref="nbaplayers")

    def __repr__(self):
        return f"<Rating rating_id={self.rating_id} score={self.score}>"

def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    connect_to_db(app)