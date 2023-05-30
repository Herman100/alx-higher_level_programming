class MagicClass:
    """
    A class that defines a magic circle.

    Attributes:
        radius: The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initialize a MagicClass object.

        Args:
            radius: The radius of the circle.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')

        self.__radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Returns:
            The area of the circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """
        Calculate the circumference of the circle.

        Returns:
            The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
