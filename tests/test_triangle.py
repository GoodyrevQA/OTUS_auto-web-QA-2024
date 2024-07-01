from src.Figure import Circle, Square, Triangle, Rectangle
import pytest


@pytest.mark.parametrize("type_of_number", ["integer", "float"])
def test_triangle_area_positive(get_triangle_areas, type_of_number):
    side_a, side_b, side_c, area = get_triangle_areas(type_of_number=type_of_number)
    t = Triangle(side_a, side_b, side_c)
    assert t.get_area == area


# подход с параметризированной фикстурой
def test_triangle_perimeter_positive(get_triangle_perimeters):
    side_a, side_b, side_c, perimeter = get_triangle_perimeters
    t = Triangle(side_a, side_b, side_c)
    assert t.get_perimeter == perimeter


@pytest.mark.parametrize(
    ("side_a", "side_b", "side_c"),
    [(0, 5, 6), (-1, 5.5, 6), ("1", False, [4]), (1, 1, 3)],
    ids=[
        "zero value",
        "negative value",
        "not number value",
        "triangle can't exist value",
    ],
)
def test_rectangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


@pytest.mark.parametrize("figure", [Circle, Square, Triangle, Rectangle])
def test_triangle_add_area(triangle_add_areas, figure):
    sum_of_areas, side_a, side_b, side_c, *other_figure = triangle_add_areas(
        figure=figure
    )
    t = Triangle(side_a, side_b, side_c)
    assert t.add_area(figure(*other_figure)) == sum_of_areas
