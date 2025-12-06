# this file is responsible for the main loop
# more delegation will probably be done later
# for now most of the game's functionality
# will be put in this file

from game.game_state import state_manager

state = state_manager()

# the main loop contains code that keeps the game 
# running and handles flow control/game state
def mainloop():
    while state.running:
        state.running = loop()

    print("You lost! Don't let the door hit you on your way out!")

# the loop function is what actually happens during each loop
def loop():
    user_input = input("> ")

    return user_input != "quit"