Pokéhoops
===========

![hi_dame](https://github.com/clarkeand/PokeHoops/blob/main/static/Pokehoops_Homepage.png?raw=true)

### Overview
Pokéhoops is a captivating Flask web application that combines the world of NBA basketball with the excitement of Pokémon. It leverages NBA player stats and generates a personalized statistic score for every active NBA player based on the P.O.K.E.D. framework (Power, Offense, Kinetics, Endurance, Defense).

As a user, you can favorite players, build a hypothetical starting five, calculate that team's POKED score, and view current team rosters and player info from the 22-23 NBA season. This unique crossover project brings together the thrill of sports analytics and the nostalgia of Pokémon, resulting in an engaging and innovative user experience.

### Technologies Used
NBA_API
Python
Javascript
HTML/CSS
Flask
PostgreSQL
SQLAlchemy
Bootstrap
Jinja
Chart.Js

###Features
Player Stats: Comprehensive statistics for every active NBA player, including a unique POKED score (calculates std deviation of each stat and add/subtracts from POKED total).
Favorites: Save your favorite players for quick and easy access.
Team Builder: Assemble a hypothetical starting five from the entire NBA roster and calculate a unique POKED for that team.
Team POKED Score: Calculate your assembled team's combined POKED score.
Roster Views: View the current team rosters and player info from the 22-23 NBA season.

### Getting Started
These instructions will guide you on how to deploy the project on your local machine for development and testing purposes.

### Prerequisites
You need to have the following installed on your local machine:

Python 3.8 or later
PostgreSQL

### Installation
Clone the repository:
git clone https://github.com/yourusername/Pokehoops.git
cd Pokehoops

### Install the requirements:
pip install -r requirements.txt
Set up the database:
python3 seed_database.py
Run the application:
python server.py
Visit localhost:3000 in your browser to access the application.

### License

This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgements

We want to express our gratitude to the NBA (and to the NBA_API) for providing the stats data and to Pokémon for the inspiration.