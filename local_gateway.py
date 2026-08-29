"""FastCollector module."""

import math
import random


class FastCollector:
    """Small sync_adapter helper."""

    def __init__(self, seed: int = 68) -> None:
        self._state = seed
        self._items: list[int] = []

    def sync_adapter(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 68) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 68


def main() -> None:
    obj = FastCollector()
    print(obj.sync_adapter(68))


if __name__ == "__main__":
    main()
