import itertools
from abc import ABC, abstractmethod
from dataclasses import dataclass


def rects_collide(rect1, rect2):
    """Check collision between rectangles

    Rectangle coordinates:
        ┌───(x2, y2)
        │       │
      (x1, y1)──┘
    """
    return (
        rect1.x1 < rect2.x2
        and rect1.x2 > rect2.x1
        and rect1.y1 < rect2.y2
        and rect1.y2 > rect2.y1
    )


class ColliderABC(ABC):
    @property
    @abstractmethod
    def bounding_box(self):
        ...

    @classmethod
    def __subclasshook__(cls, C):
        if cls is ColliderABC:
            if any("bounding_box" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


def find_collisions(objects):
    for item in objects:
        if not isinstance(item, ColliderABC):
            raise TypeError(f"{item} is not a collider")

    return [
        (item1, item2)
        for item1, item2 in itertools.combinations(objects, 2)
        if rects_collide(item1.bounding_box, item2.bounding_box)
    ]


@dataclass
class Box:
    x1: float
    y1: float
    x2: float
    y2: float


@dataclass
class Square:
    x: float
    y: float
    size: float

    @property
    def bounding_box(self):
        return Box(self.x, self.y, self.x + self.size, self.y + self.size)


@dataclass
class Rect:
    x: float
    y: float
    width: float
    height: float

    @property
    def bounding_box(self):
        return Box(self.x, self.y, self.x + self.width, self.y + self.height)


@dataclass
class Circle:
    x: float
    y: float
    radius: float

    @property
    def bounding_box(self):
        return Box(
            self.x - self.radius,
            self.y - self.radius,
            self.x + self.radius,
            self.y + self.radius,
        )


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Line:
    p1: Point
    p2: Point

    @property
    def bounding_box(self):
        return Box(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
        )


if __name__ == "__main__":
    print("Valid attempt:\n")
    for collision in find_collisions([
        Square(0, 0, 10),
        Rect(5, 5, 20, 20),
        Square(15, 20, 5),
        Circle(1, 1, 2),
    ]):
        print(collision)

    print("\nInvalid attempt:\n")
    for collision in find_collisions([
        Circle(1, 1, 2),
        Point(100, 200),
    ]):
        print(collision)
