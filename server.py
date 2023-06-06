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

@app.route('/login')
def login_page():
    """View login page with a create an account option."""
    return render_template('login.html')

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

@app.route('/user_landing')
def user_page():
    """View user landing page."""
    return render_template('userid.html')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=3000)