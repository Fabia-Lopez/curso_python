import random
import json
from Sport import Sport
from Athlete import Athlete
from Team import Team
from Game import Game   

class Tournament:
    def __init__(self,name):
        self.name = name
        self.teams = []
        self.games = []

    def add_team(self, team):
        if isinstance(team, Team):
            self.teams.append(team)
        else:
            raise ValueError("Only Team objects can be added to the tournament.")
    
    def add_game(self, game):
        if isinstance(game, Game):
            self.games.append(game)
        else:
            raise ValueError("Only Game objects can be added to the tournament.")
        
    

    def __str__(self):
        return f"Tournament: {self.name}, Teams: {[team.name for team in self.teams]}, Games: {[str(game) for game in self.games]}"
    
    def __repr__(self):
        return f"Tournament(name={self.name}, teams={repr(self.teams)}, games={repr(self.games)})"
    
    def to_json(self):
        """ Convert the Tournament object to a JSON string. """
        return{
            "name": self.name,
            "teams": [team.to_json() for team in self.teams],
            "games": [game.to_json() for game in self.games]
        }
    
    def load_json(self, filename):
        """ Load the Tournament object from a JSON file. """
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        for team_data in data["teams"]:
            team = Team(team_data["name"], team_data["sport"]
            players = team_data["athletes"]
            for player_data in players:
                athlete = Athlete(player_data["name"], player_data["age"], player_data["sport"])
                team.add_athlete(athlete)
