"""
Docstring for game_tournament.Game
Game class represents a game in the tournament. It has a name, a sport, and a list of teams.
"""
import random
import json
from Sport import Sport
from Athlete import Athlete
from Team import Team

class Game:
    """ Game class represents a game in the tournament. It has two teams and a score"""
    def __init__(self, A:Team, B:Team):
        """ Custom constructor for Game class. """
        self.set_team(A, "local")
        self.set_team(B,"visitor")
        self.score = {
            A.name: 0, B.name: 0
            }
    def set_team(self, team, role):
        """ Set a team for the game. """
        if isinstance(team, Team):
            if role == "local":
                self.team_a = team
            elif role == "visitor":
                self.team_b = team
            else:
                raise ValueError("Role must be 'local' or 'visitor'.")
        else:
            raise ValueError("Only Team objects can be set as a team.")
    def play(self):
        """ Simulate playing the game by randomly assigning scores to each team. """
        self.score[self.team_a.name] = random.randint(0, Sport.max_score[self.team_a.sport.name])
        self.score[self.team_b.name] = random.randint(0, Sport.max_score[self.team_b.sport.name])
    def __str__(self):
        """ String representation of the Game class. """
        return f"{self.team_a.name} vs {self.team_b.name} - Score: {self.score[self.team_a.name]}:{self.score[self.team_b.name]}"
    
    def __repr__(self):
        """ String representation of the Game class. """
        return f"Game(team_a={repr(self.team_a)}, team_b={repr(self.team_b)}, score={self.score})"
    
    def to_json(self):
        """ Convert the Game object to a JSON string. """
        return {
            "team_a": self.team_a.to_json(),
            "team_b": self.team_b.to_json(),
            "score": self.score
        }
    
    




def save_game_to_json(game_data, filename):
    """ Save the game object to a JSON file. """
    with open(filename, 'w', encoding= 'utf-8') as f:
        json.dump(game_data, f, indent=4)

def a_tournament():
    players_mex=["Hugo Sánchez", "Jared Borgetti", "Cuauhtémoc Blanco", "Luis Hernández", "Carlos Vela"]
    players_arg=["Lionel Messi", "Diego Armando", "Gabriel Batistuta", "Sergio Agüero", "Ángel Di María"]
    players_peru=["Paolo Guerrero", "Claudio Pizarro", "Teófilo Cubillas", "Hugo Sotil", "Roberto Palacios"]
    players_france=["Kylian Mbappé", "Antoine Griezmann", "Olivier Giroud", "Hugo Lloris", "Raphaël Varane"]
    players_spain=["Andrés Iniesta", "Xavi Hernández", "David Villa", "Iker Casillas", "Sergio Ramos"]
    players_brazil=["Pelé", "Ronaldo Nazário", "Ronaldinho", "Neymar Jr.", "Zico"]
    players_italia=["Roberto Baggio", "Francesco Totti", "Gianluigi Buffon", "Paolo Maldini", "Alessandro Del Piero"]
    players_japan=["Hidetoshi Nakata", "Shinji Kagawa", "Keisuke Honda", "Yasuhito Endo", "Shunsuke Nakamura"]
    
    sport = Sport("Futbol", 11, "FIFA")
    team_mex = Team("Mexico", sport)
    team_arg = Team("Argentina", sport)
    team_peru = Team("Peru", sport)
    team_france = Team("France", sport)
    team_spain = Team("Spain", sport)
    team_brazil = Team("Brazil", sport)
    team_italia = Team("Italia", sport)
    team_japan = Team("Japan", sport)

    for player in players_mex:
        team_mex.add_athlete(Athlete(player))
    for player in players_arg:
        team_arg.add_athlete(Athlete(player))
    for player in players_peru:
        team_peru.add_athlete(Athlete(player))
    for player in players_france:
        team_france.add_athlete(Athlete(player))
    for player in players_spain:
        team_spain.add_athlete(Athlete(player))
    for player in players_brazil:
        team_brazil.add_athlete(Athlete(player))
    for player in players_italia:
        team_italia.add_athlete(Athlete(player))
    for player in players_japan:
        team_japan.add_athlete(Athlete(player))
    tournament_list = [team_mex, team_arg, team_peru, team_france, team_spain, team_brazil, team_italia, team_japan]
    json_string = ""
    for team in tournament_list:
        json_string += f"{team.to_json()}\n"
    return json_string

def load_game_from_json(filename):
    """ Load the game object from a JSON file. """
    with open(filename, 'r', encoding= 'utf-8') as f:
        game_data = json.load(f)
    return game_data


if __name__ == "__main__":
    string_game = a_tournament()

    #save_game_to_json(string_game, "tournament.json")
    loaded_game = load_game_from_json("tournament.json")
    print(loaded_game)
    print("-----------------------------------")
