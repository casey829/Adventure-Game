# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GameState(BaseModel):
    current_scene: str
    message: str
    choices: List[dict]
    game_over: bool = False

class GameChoice(BaseModel):
    scene: str
    choice: str

# Game logic
def get_next_state(scene: str, choice: str) -> GameState:
    if scene == "start":
        if choice == "enter":
            return GameState(
                current_scene="house",
                message="You step inside the house. It's dark and cold. You see a STAIRCASE leading upstairs and a DOOR to the basement.",
                choices=[
                    {"text": "Go UPSTAIRS", "value": "upstairs"},
                    {"text": "Go DOWNSTAIRS", "value": "downstairs"}
                ]
            )
        elif choice == "walk":
            return GameState(
                current_scene="outside",
                message="You decide to walk around the house. The forest is dense and dark.",
                choices=[
                    {"text": "KEEP WALKING", "value": "walk"},
                    {"text": "Enter the CAVE", "value": "cave"}
                ]
            )
    
    elif scene == "house":
        if choice == "upstairs":
            return GameState(
                current_scene="upstairs",
                message="You slowly walk upstairs. You find a locked chest!",
                choices=[
                    {"text": "OPEN the chest", "value": "open"},
                    {"text": "LEAVE it", "value": "leave"}
                ]
            )
        elif choice == "downstairs":
            return GameState(
                current_scene="basement",
                message="You carefully descend into the basement. It's very dark and you hear strange noises.",
                choices=[
                    {"text": "Use FLASHLIGHT", "value": "flashlight"},
                    {"text": "LEAVE basement", "value": "leave"}
                ]
            )
    
    # Might add more logic to the game for other scenes
    
    return GameState(
        current_scene="error",
        message="Something went wrong!",
        choices=[{"text": "Start Over", "value": "restart"}]
    )

@app.get("/start")
def start_game():
    return GameState(
        current_scene="start",
        message="You find yourself in a dark forest. In front of you is a spooky house.",
        choices=[
            {"text": "ENTER the house", "value": "enter"},
            {"text": "WALK around it", "value": "walk"}
        ]
    )

@app.post("/make_choice")
def make_choice(game_choice: GameChoice):
    return get_next_state(game_choice.scene, game_choice.choice)