"""FastMonitor module."""

import math
import random


class FastMonitor:
    """Small load_gateway helper."""

    def __init__(self, seed: int = 24) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_gateway(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 24) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 24


def main() -> None:
    obj = FastMonitor()
    print(obj.load_gateway(24))


if __name__ == "__main__":
    main()
