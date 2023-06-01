"""Script to seed database."""

import os
from nba_api.stats.static import players, teams
from nba_api.stats.endpoints import commonplayerinfo, playerfantasyprofile

import crud
import model
import server

os.system("dropdb ratings")
os.system('createdb ratings')
model.connect_to_db(server.app)
model.db.create_all()

player_dict = players.get_active_players()
team_dict = teams.get_teams()

# Create Players
for movie in movie_data:
    title, overview, poster_path = (
        movie["title"],
        movie["overview"],
        movie["poster_path"],
    )
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path))

for player in player_dict: 
    player_id  = player_dict[player]['id']
    player_name = player_dict[player]['full_name']
    player_info = commonplayerinfo.CommonPlayerInfo(f'{player_id}')
    player_info = player_info.get_normalized_dict()
    player_info = player_info.get('CommonPlayerInfo')[0]
    team_id = player_info['TEAM_ABBREVIATION']




for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
        model.db.session.add(rating)

model.db.session.add_all(movies_in_db)
model.db.session.commit()