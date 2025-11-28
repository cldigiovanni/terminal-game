# this file is responsible for the main loop
# more delegation will probably be done later
# for now most of the game's functionality
# will be put in this file

from game.game_state import state_manager

state = state_manager()

def mainloop():
    while state.running:
        state.running = loop()

    print("You lost! Don't let the door hit you on your way out!")

def loop():
    user_input = input("> ")

    return user_input != "quit"