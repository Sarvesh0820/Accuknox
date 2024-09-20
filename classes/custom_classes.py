
class Rectangle:
    def __init__(self, length: int, width: int):
        """
        Initialize a Rectangle instance.

        Args:
        length (int): The length of the rectangle.
        width (int): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def __iter__(self):
        """
        Iterate over the rectangle's dimensions.

        Yields:
        dict: A dictionary containing the length or width.
        """
        yield {'length': self.length}
        yield {'width': self.width}

# Create a Rectangle instance
rectangle = Rectangle(5, 3)

# Iterate over the rectangle's dimensions
for dimension in rectangle:
    print(dimension)

