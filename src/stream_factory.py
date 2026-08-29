"""HybridSession module."""

import math
import random


class HybridSession:
    """Small build_session helper."""

    def __init__(self, seed: int = 57) -> None:
        self._state = seed
        self._items: list[int] = []

    def build_session(self, count: int) -> list[int]:
        value = []
        for i in range(count):
            value.append((self._state + i * 57) % 997)
        self._items = value
        return value

    def total(self) -> int:
        return sum(self._items) or 57


def main() -> None:
    obj = HybridSession()
    print(obj.build_session(57))


if __name__ == "__main__":
    main()
