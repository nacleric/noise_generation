from typing import Any, Union
from pprint import pprint
from enum import Enum, auto
import random

ROW_SIZE = 20
COL_SIZE = 20


class Terrain(Enum):
    EMPTY = 0
    GRASS = "G"
    TREE = "T"
    WATER = "W"


class MapGen:
    @staticmethod
    def white_noise(row_size, col_size) -> list[list[Terrain]]:
        arr = [[random.choice(list(Terrain)) for col in range(col_size)] for row in range(row_size)]
        return arr

    @staticmethod
    def blue_noise() -> list[list[Terrain]]:
        pass


def _display(game_map: list[list[Terrain]]) -> None:
    for row in game_map:
        for col in row:
            print(f" {col.value}", end="")
        print(end="\n")


def main() -> None:
    game_map = MapGen.white_noise(ROW_SIZE, COL_SIZE)
    _display(game_map)


if __name__ == "__main__":
    main()
