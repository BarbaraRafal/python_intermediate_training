import pytest
from python_intermediate_training.figures.figures_entities import Circle
from python_intermediate_training.figures.figures_entities import Triangle
from python_intermediate_training.figures.figures_entities import Rectangle
from python_intermediate_training.figures.figures_entities import Figure


def test_count_area():
    #  given
    circle1 = Circle(1)
    triangle1 = Triangle(2, 1)
    rectangle1 = Rectangle(2, 2)

    #  when
    result = Figure.count_area([circle1, triangle1, rectangle1])
    #  then
    assert result == 8.1416

def test_check_area():
