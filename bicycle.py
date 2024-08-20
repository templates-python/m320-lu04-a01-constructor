class Bicycle:
    """
    A bicycle with some attributes and methods

    Attributes
    ----------
    _type: str
    _size: int
    _color: str
    """

    def __init__(self, type='mountainbike', size=48):
        """
        Constructor with type and size.
        """
        self._type = type
        self._size = size
        self._color = 'gray'

    @property
    def type(self):
        """
        Gets the type of this bicycle.
        """
        return self._type

    @property
    def size(self):
        """
        Gets the size of this bicycle.
        """
        return self._size

    @property
    def color(self):
        """
        Gets the color of this bicycle.
        """
        return self._color

    @type.setter
    def type(self, type):
        """
        Sets the type of this bicycle.
        """
        self._type = type

    @size.setter
    def size(self, size):
        """
        Sets the size of this bicycle.
        """
        self._size = size

    @color.setter
    def color(self, color):
        """
        Sets the color of this bicycle.
        """
        self._color = color

    def print(self):
        """
        prints a human-readable representation of the object.
        :return:
        """
        print(
            f'Fahrrad:\n'
            f'\tArt:            {self._type}\n'
            f'\tRahmengrösse:   {self._size}\n'
            f'\tFarbe:          {self._color}'
        )


if __name__ == "__main__":
    # Aufgabe 1
    bicycle = Bicycle()
    bicycle.print()
    #
    bicycle = Bicycle(type='racebike')
    bicycle.print()
    #
    bicycle = Bicycle(type='citybike', size='42')
    bicycle.print()
    #
    # Aufgabe 2
    #
    bicycle.color = 'red'
    bicycle.print()
