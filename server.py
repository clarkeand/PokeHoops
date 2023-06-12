"""Server for Pokéhoops app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect,jsonify)
from model import connect_to_db, db
from nba_api.stats.endpoints import commonplayerinfo
import crud

from jinja2 import StrictUndefined
app = Flask(__name__, static_folder='static')
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

NBA_PPG_MEAN = 10.8
NBA_APG_MEAN = 2.36
NBA_RPG_MEAN = 4.26

@app.route('/')
def homepage():
    """View homepage."""
    return render_template('homepage.html')

@app.route('/players')
def all_players():
    """View all players."""
    players = crud.get_players()
    return render_template('players.html',players=players)

@app.route('/fav_player/<player_id>')
def fav_player(player_id):
    """Favorite a player."""
    user_email = session.get("user_email")
    if user_email == None:
        flash("Please login first.")
    else:
        user = crud.get_user_by_email(user_email)
        fav_player = crud.create_user_player(player_id,user.user_id)
        if fav_player == None: 
            flash("Player is already in your favorites!")
        else:
            db.session.add(fav_player)
            db.session.commit()
            flash("Player added to favorites!")

    return redirect(f'/players/{player_id}')

@app.route('/sortTeam')
def sortTeam():
    """Return players list sorted by Team"""
    players = crud.get_players_by_team()
    return jsonify(players)

@app.route('/sortPosition')
def sortPosition():
    """Return players list sorted by Position"""
    players = crud.get_players_by_position()
    return jsonify(players)

@app.route('/sortPOKED')
def sortPOKED():
    """Return players list sorted by POKED"""
    players = crud.get_players_by_POKED()
    return jsonify(players)

@app.route('/register', methods=["POST"])
def register():
    """Allow a user to create an account."""
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user: 
        user = crud.create_user(email,password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")
    else: 
        flash("Email already taken, please select a new email.")
    return render_template('login.html')

@app.route('/login')
def show_login_page():
    """render login.html page"""
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login():
    """Allow a user to login."""
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
        return render_template("login.html")
    else:
        session["user_email"] = user.email
        flash(f"Welcome back, {user.email}!")
        return redirect("/")
    
@app.route('/logout')
def logout():
    """process logout and go to homepage"""
    session.clear()
    return redirect("/")

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
    league_averages = [NBA_PPG_MEAN, NBA_APG_MEAN, NBA_RPG_MEAN]
    return render_template("playerid.html", player=player, player_stats=player_stats, league_averages=league_averages)

@app.route('/teams')
def all_teams():
    """View all teams."""
    teams = crud.get_teams()
    return render_template('teams.html', teams=teams)

@app.route('/teams/<team_id>')
def team_page(team_id):
    """View individual team's roster."""
    players = crud.get_team_players(team_id)
    team = crud.get_team_by_id(team_id)
    team_name = team.team_name
    return render_template("team_id.html", players=players, team_name=team_name)

@app.route('/user_dashboard')
def user_page():
    """View user landing page."""
    player_list = []
    user_email = session.get("user_email")
    user = crud.get_user_by_email(user_email)
    user_players = crud.get_users_players(user)
    for user_player in user_players: 
        NBAplayer = crud.get_player_by_id(user_player.player_id)
        player_list.append(NBAplayer)
    return render_template('user_dashboard.html', player_list=player_list)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=3000)