from enum import Enum

class SceneState(Enum):
    CORE = 1
    EXPLORE = 2
    FIGHT = 3
    LOOT = 4

class state_manager:
    def __init__(self):
        self.running = True
        self.scene = SceneState.CORE