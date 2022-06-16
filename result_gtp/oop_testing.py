class Triangle:
    """Create a triangle class that has methods for checking for correctness,
    finding area and perimeter"""

    def __init__(self, size):
        self.size = size

    def is_valid(self):
        if self.size <= 0:
            raise ValueError("size must be greater than 0")

    def area(self):
        return self.size * self.size * 0.5

    def perimeter(self):
        return 2 * self.size


class Figure(object):

    def __init__(self):
        self.sides = []

    def add_side(self, side):
        self.sides.append(side)

    def get_sides(self):
        return self.sides


class Person:
    def __init__(self):
        pass

    def get_name(self):
        pass


# create an instance from the class
person = Person()

# call the method from the instance
print(person.get_name())
