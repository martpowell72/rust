"""LiteHandler module."""

import math
import random


class LiteHandler:
    """Small render_factory helper."""

    def __init__(self, seed: int = 60) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_factory(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 60) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 60


def main() -> None:
    obj = LiteHandler()
    print(obj.render_factory(60))


if __name__ == "__main__":
    main()
