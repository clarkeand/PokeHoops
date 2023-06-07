"""Server for Pokéhoops app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
from nba_api.stats.endpoints import commonplayerinfo
import crud

from jinja2 import StrictUndefined
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/register', methods=["POST"])
def register():
    """Allow register."""
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    return render_template("login.html")

@app.route('/login_user', methods=["POST"])
def login_user():
    """Allow a user to login."""
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")
    return redirect("/")

@app.route('/login')
def login_page():
     """Load login page """
     return render_template("login.html")

@app.route('/players')
def all_players():
    """View all players."""
    players = crud.get_players()
    return render_template('players.html',players=players)

@app.route('/players/<player_id>')
def player_page(player_id):
    """View player's individual page."""
    player = crud.get_player_by_id(player_id)
    player_info = commonplayerinfo.CommonPlayerInfo(f'{player_id}')
    player_stats = player_info.player_headline_stats.get_dict()
    if player_stats['data'] != []:
        player_stats = player_stats['data'][0]
    else:
        player_stats = ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A']
    return render_template("playerid.html", player=player, player_stats=player_stats)

@app.route('/teams')
def all_teams():
    """View all teams."""
    players = crud.get_players()
    return render_template('players.html',players=players)

@app.route('/user_landing')
def user_page():
    """View user landing page."""
    return render_template('userid.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=3000)