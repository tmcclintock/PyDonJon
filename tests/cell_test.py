from unittest import TestCase

from donjuan import HexCell, SquareCell


class SquareCellTest(TestCase):
    def test_smoke(self):
        c = SquareCell()
        assert c is not None

    def test_filled(self):
        c = SquareCell()
        assert not c.filled
        c.filled = True
        assert c.filled

    def test_faces(self):
        c = SquareCell()
        assert len(c.faces) == 4

    def test_n_sides(self):
        c = SquareCell()
        assert c.n_sides == 4

    def test_coordinates(self):
        c = SquareCell()
        assert c.coordinates is None
        c.set_coordinates(1, 2)
        assert c.coordinates == (1, 2)
        assert c.x == 1
        assert c.y == 2


class HexCellTest(TestCase):
    def test_smoke(self):
        c = HexCell()
        assert c is not None

    def test_faces(self):
        c = HexCell()
        assert len(c.faces) == 6

    def test_n_sides(self):
        c = HexCell()
        assert c.n_sides == 6

    def test_coordinates(self):
        c = HexCell()
        assert c.coordinates is None
        c.set_coordinates(1, 2)
        assert c.coordinates == (1, 2)
        assert c.x == 1
        assert c.y == 2
