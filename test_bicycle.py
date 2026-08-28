import pytest
from bicycle import Bicycle

class TestBicycle:

    def test_initialization(self):
        bike = Bicycle()
        assert bike.biketype == 'mountainbike'
        assert bike.size == 48
        assert bike.color == 'gray'

    def test_type_set_get(self):
        bike = Bicycle()
        bike.biketype = 'roadbike'
        assert bike.biketype == 'roadbike'

    def test_size_get_set(self):
        bike = Bicycle()
        bike.size = 54
        assert bike.size == 54

    def test_color_get_set(self):
        bike = Bicycle()
        bike.color = 'blue'
        assert bike.color == 'blue'

if __name__ == '__main__':
    pytest.main()