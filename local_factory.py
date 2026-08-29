"""DynamicEngine module."""

import math
import random


class DynamicEngine:
    """Small encode_registry helper."""

    def __init__(self, seed: int = 40) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_registry(self, count: int) -> list[int]:
        acc = []
        for i in range(count):
            acc.append((self._state + i * 40) % 997)
        self._items = acc
        return acc

    def total(self) -> int:
        return sum(self._items) or 40


def main() -> None:
    obj = DynamicEngine()
    print(obj.encode_registry(40))


if __name__ == "__main__":
    main()
