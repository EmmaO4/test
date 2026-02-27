class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        # Human-readable representation for users
        return f"({self.x}, {self.y})"

    def __repr__(self):
        # Developer-friendly representation for debugging/recreation
        return f"Point2D({self.x}, {self.y})"

p = Point2D(10, 20)
print(p)  # Calls __str__ implicitly: Output: (10, 20)
print(str(p)) # Explicitly calls __str__: Output: (10, 20)
print(repr(p)) # Explicitly calls __repr__: Output: Point2D(10, 20)