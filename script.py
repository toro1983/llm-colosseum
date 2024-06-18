import sys

from dotenv import load_dotenv
from eval.game import Game, Player1, Player2
from loguru import logger

logger.remove()
logger.add(sys.stdout, level="INFO")

load_dotenv()


def main():
    # Environment Settings
    game = Game(
        render=True,
        player_1=Player1(
            nickname="Player_1",
            model="openai:gpt-3.5-turbo-0125",
        ),
        player_2=Player2(
            nickname="Player_2",
            model="openai:gpt-4-0125-preview",
        ),
    )
    return game.run()


if __name__ == "__main__":
    main()
