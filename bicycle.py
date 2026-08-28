"""
a class representing a bike
"""
class Bicycle:
    """
    A bicycle with some attributes and methods

    Attributes
    ----------
    _biketype: str
    _size: int
    _color: str
    """

    def __init__(self, biketype='mountainbike', size=48):
        """
        Constructor with biketype and size.
        """
        self._biketype = biketype
        self._size = size
        self._color = 'gray'

    @property
    def biketype(self):
        """
        Gets the biketype of this bicycle.
        """
        return self._biketype

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

    @biketype.setter
    def biketype(self, biketype):
        """
        Sets the biketype of this bicycle.
        """
        self._biketype = biketype

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

    def __str__(self):
        """
        returns a human-readable representation of the object.
        :return:
        """
        return(
            f'Fahrrad:\n'
            f'\tArt:            {self._biketype}\n'
            f'\tRahmengrösse:   {self._size}\n'
            f'\tFarbe:          {self._color}'
        )


if __name__ == '__main__':
    # Aufgabe 1
    bicycle = Bicycle()
    bicycle.print()
    #
    bicycle = Bicycle(biketype='racebike')
    bicycle.print()
    #
    bicycle = Bicycle(biketype='citybike', size='42')
    bicycle.print()
    #
    # Aufgabe 2
    #
    bicycle.color = 'red'
    bicycle.print()
