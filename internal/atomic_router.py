"""AsyncGateway module."""

import math
import random


class AsyncGateway:
    """Small load_registry helper."""

    def __init__(self, seed: int = 55) -> None:
        self._state = seed
        self._items: list[int] = []

    def load_registry(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 55) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 55


def main() -> None:
    obj = AsyncGateway()
    print(obj.load_registry(55))


if __name__ == "__main__":
    main()
