""" Sport class represents a sport in the tournament. It has a name and a league. """
class Sport:
    """ Sport class represents a sport in the tournament. It has a name and a league. """
    def __init__(self, name, num_players,league):
        """custom constructor for the Sport class."""
        self.name = name
        self.num_players = num_players
        self.league = league

    def __str__(self):
        """String representation of the Sport object."""
        return f"Sport: {self.name}, League: {self.league}"
    
    def __repr__(self):
        """ Official string representation of the Sport object."""
        return f"Sport(name='{self.name}', league='{self.league}')"