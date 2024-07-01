from src.Figure import Circle, Square, Triangle, Rectangle
import pytest


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_square_area_positive(get_square_areas, type_of_number):
    side_a, area = get_square_areas(type_of_number=type_of_number)
    s = Square(side_a)
    assert s.get_area == area


# подход с параметризированной фикстурой
def test_square_perimeter_positive(get_square_perimeters):
    side_a, perimeter = get_square_perimeters
    s = Square(side_a)
    assert s.get_perimeter == perimeter


@pytest.mark.parametrize(
    "side_a", [0, -1, "33"], ids=["zero value", "negative value", "not number value"]
)
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


@pytest.mark.parametrize("figure", [Circle, Square, Triangle, Rectangle])
def test_square_add_area(square_add_areas, figure):
    sum_of_areas, side_a, *other_figure = square_add_areas(figure=figure)
    s = Square(side_a)
    assert s.add_area(figure(*other_figure)) == sum_of_areas
