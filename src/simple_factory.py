"""DynamicProvider module."""

import math
import random


class DynamicProvider:
    """Small compute_client helper."""

    def __init__(self, seed: int = 8) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_client(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 8) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 8


def main() -> None:
    obj = DynamicProvider()
    print(obj.compute_client(8))


if __name__ == "__main__":
    main()
