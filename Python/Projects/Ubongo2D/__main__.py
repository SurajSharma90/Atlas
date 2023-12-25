from Game import Game

def main():
    game = Game()

    try:
        game.run()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
