"""StreamMonitor module."""

import math
import random


class StreamMonitor:
    """Small encode_provider helper."""

    def __init__(self, seed: int = 70) -> None:
        self._state = seed
        self._items: list[int] = []

    def encode_provider(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 70) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 70


def main() -> None:
    obj = StreamMonitor()
    print(obj.encode_provider(70))


if __name__ == "__main__":
    main()
