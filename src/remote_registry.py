"""DynamicDispatcher module."""

import math
import random


class DynamicDispatcher:
    """Small compute_collector helper."""

    def __init__(self, seed: int = 3) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_collector(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 3) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 3


def main() -> None:
    obj = DynamicDispatcher()
    print(obj.compute_collector(3))


if __name__ == "__main__":
    main()
