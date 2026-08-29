"""CoreRegistry module."""

import math
import random


class CoreRegistry:
    """Small handle_cache helper."""

    def __init__(self, seed: int = 37) -> None:
        self._state = seed
        self._items: list[int] = []

    def handle_cache(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 37) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 37


def main() -> None:
    obj = CoreRegistry()
    print(obj.handle_cache(37))


if __name__ == "__main__":
    main()
