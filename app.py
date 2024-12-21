from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory storage for processed player IDs
processed_players = set()


class Player(BaseModel):
    player_id: str


@app.get("/players")
def get_players():
    """Return the list of all processed player IDs."""
    return {"processed_players": list(processed_players)}


@app.post("/players")
def add_player(player: Player):
    """Add a new player ID and return whether it was new."""
    if player.player_id in processed_players:
        return {"is_new": False}
    processed_players.add(player.player_id)
    return {"is_new": True}
