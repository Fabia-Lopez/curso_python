from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Static
from textual.containers import Vertical, VerticalScroll
from textual.screen import Screen
import os
from Tournament import Tournament
import random

class TextualUI(App):
    CSS = """
    Screen {
        align: center middle;
    }

    #menu-container {
        width: 40;
        height: auto;
        border: thick $primary;
        padding: 1;
        background: $surface;
    }

    #tournament-scroll {
        padding: 2;
        border: solid $accent;
    }

    .title {
        text-align: center;
        width: 100%;
        text-style: bold;
        background: $primary;
        color: $text;
        margin-bottom: 1;
    }

    .header {
        text-style: bold underline;
        color: $secondary;
        margin-top: 1;
    }

    .subheader {
        text-style: italic;
        color: $accent;
    }

    #groups-scroll {
        padding: 2;
        border: solid $secondary;
    }

    #groups-scroll .subheader {
        background: $surface;
        color: $text;
        text-style: bold;
        padding-left: 2;
    }

    #games-scroll, #simulation-scroll {
        padding: 2;
    }

    .table-header {
        background: $surface;
        color: $text;
        text-style: bold;
        padding-left: 2;
    }

    Button {
        width: 100%;
        margin-bottom: 1;
    }

    Static {
        margin-bottom: 0;
    }
    """

    BINDINGS = [
        ("l", "load", "[L]oad"),
        ("t", "display_tournament", "[T]ournament"),
        ("g", "display_groups", "[G]roups"),
        ("m", "display_games", "Ga[m]es"),
        ("p", "play", "[P]lay"),
        ("q", "exit_app", "[Q]uit"),
        ("up", "focus_previous", "Focus Previous"),
        ("down", "focus_next", "Focus Next"),
    ]

    def __init__(self):
        super().__init__()
        self.tournament = None
        self.current_file = None
    
    def on_mount(self):
        self.query_one("#load").focus()

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="menu-container"):
            yield Button("Load Tournament", id="load", variant="primary")
            yield Button("Tournament", id="tournament", variant="secondary")
            yield Button("Groups", id="groups", variant="secondary")
            yield Button("Games", id="games", variant="secondary")
            yield Button("Play", id="play", variant="success")
            yield Button("Quit", id="quit", variant="error")
        yield Footer()
    
    def action_load(self):
        self.get_tournament_json()
    def action_display_tournament(self):
        self.display_tournament()
    def action_display_groups(self):
        self.display_groups()
    def action_display_games(self):
        self.display_games()
    def action_play(self):
        self.play_games()


    def display_games(self)
        """ Display the games. """
        if self.tournament:
            self.notify("Displaying games...")

        else:
            self.notify("No tournament loaded. Please load a tournament first.")

    def play_games(self):
        """ Play the games. """
        if self.tournament:
            self.push_screen(PlayScreen(self.tournament))
        else:
            self.notify("No tournament loaded. Please load a tournament first.")

    def exit_app(self):
        """ Exit the application. """
        self.exit()
    def display_menu(self):
        self.run()

if __name__ == "__main__":
    app = TextualUI()
    app.set_current_file("tournament.json")
    app.open_tournament()
    app.run()
    