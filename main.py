from game import static
from game import loop

def main():
    print(f"Welcome to the game! - Current Version {static.ver()}")
    loop.mainloop()

if __name__ == "__main__":
    main()