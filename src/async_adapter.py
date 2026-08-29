"""SharedEngine module."""

import math
import random


class SharedEngine:
    """Small decode_processor helper."""

    def __init__(self, seed: int = 61) -> None:
        self._state = seed
        self._items: list[int] = []

    def decode_processor(self, count: int) -> list[int]:
        total = []
        for i in range(count):
            total.append((self._state + i * 61) % 997)
        self._items = total
        return total

    def total(self) -> int:
        return sum(self._items) or 61


def main() -> None:
    obj = SharedEngine()
    print(obj.decode_processor(61))


if __name__ == "__main__":
    main()
