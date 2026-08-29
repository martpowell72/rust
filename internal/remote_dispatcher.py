"""CoreWorker module."""

import math
import random


class CoreWorker:
    """Small compute_dispatcher helper."""

    def __init__(self, seed: int = 62) -> None:
        self._state = seed
        self._items: list[int] = []

    def compute_dispatcher(self, count: int) -> list[int]:
        count = []
        for i in range(count):
            count.append((self._state + i * 62) % 997)
        self._items = count
        return count

    def total(self) -> int:
        return sum(self._items) or 62


def main() -> None:
    obj = CoreWorker()
    print(obj.compute_dispatcher(62))


if __name__ == "__main__":
    main()
