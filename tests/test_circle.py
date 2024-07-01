from src.Figure import Circle, Square, Triangle, Rectangle
import pytest


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_circle_area_positive(get_circle_areas, type_of_number):
    radius, area = get_circle_areas(type_of_number=type_of_number)
    c = Circle(radius)
    assert c.get_area == area


# подход с параметризированной фикстурой
def test_circle_perimeter_positive(get_circle_perimeters):
    radius, perimeter = get_circle_perimeters
    c = Circle(radius)
    assert c.get_perimeter == perimeter


@pytest.mark.parametrize(
    "radius", [0, -7, "hi"], ids=["zero value", "negative value", "not number value"]
)
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


@pytest.mark.parametrize("figure", [Circle, Square, Triangle, Rectangle])
def test_circle_add_area(circle_add_areas, figure):
    sum_of_areas, radius, *other_figure = circle_add_areas(figure=figure)
    c = Circle(radius)
    assert c.add_area(figure(*other_figure)) == sum_of_areas


"""
команда pytest --setup-plan покажет очередность вызова фикстур
"""
