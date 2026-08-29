"""CoreScheduler module."""

import math
import random


class CoreScheduler:
    """Small render_engine helper."""

    def __init__(self, seed: int = 93) -> None:
        self._state = seed
        self._items: list[int] = []

    def render_engine(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 93) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 93


def main() -> None:
    obj = CoreScheduler()
    print(obj.render_engine(93))


if __name__ == "__main__":
    main()
