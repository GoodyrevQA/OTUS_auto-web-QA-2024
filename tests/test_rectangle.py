from src.Figure import Circle, Square, Triangle, Rectangle
import pytest


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_rectangle_area_positive(get_rectangle_areas, type_of_number):
    side_a, side_b, area = get_rectangle_areas(type_of_number=type_of_number)
    r = Rectangle(side_a, side_b)
    assert r.get_area == area


# подход с параметризированной фикстурой
def test_rectangle_perimeter_positive(get_rectangle_perimeters):
    side_a, side_b, perimeter = get_rectangle_perimeters
    r = Rectangle(side_a, side_b)
    assert r.get_perimeter == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b"),
    [(0, 5), (-1, 5.5), ("1", False)],
    ids=["zero value", "negative value", "not number value"],
)
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


@pytest.mark.parametrize("figure", [Circle, Square, Triangle, Rectangle])
def test_rectangle_add_area(rectangle_add_areas, figure):
    sum_of_areas, side_a, side_b, *other_figure = rectangle_add_areas(figure=figure)
    r = Rectangle(side_a, side_b)
    assert r.add_area(figure(*other_figure)) == sum_of_areas
