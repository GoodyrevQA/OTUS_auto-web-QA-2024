import pytest
from src.Figure import *


@pytest.fixture
def get_rectangle_areas():
    # print("\nStart get_rectangle_areas")

    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 3, 5, 15
        if type_of_number == "float":
            return 3.5, 5.5, 19.25

    yield _wrapper
    # print("\nEnd get_rectangle_areas")


# параметризированная фикстура
@pytest.fixture(params=[(4, 6, 20), (1.5, 4.5, 12.0)], ids=["integer", "float"])
def get_rectangle_perimeters(request):
    # print("\nStart get_rectangle_perimeters")
    side_a, side_b, perimeter = request.param
    yield side_a, side_b, perimeter
    # print("\nEnd get_rectangle_perimeters")


@pytest.fixture
def get_square_areas():
    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 4, 16
        if type_of_number == "float":
            return 1.5, 2.25

    yield _wrapper


@pytest.fixture(params=[(3, 12), (1.5, 6)], ids=["integer", "float"])
def get_square_perimeters(request):
    side_a, perimeter = request.param
    yield side_a, perimeter


@pytest.fixture
def get_triangle_areas():
    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 3, 4, 5, 6
        if type_of_number == "float":
            return 13.0, 4.0, 15.0, 24.0

    yield _wrapper


@pytest.fixture(params=[(3, 5, 7, 15), (1.5, 2.5, 3.5, 7.5)], ids=["integer", "float"])
def get_triangle_perimeters(request):
    side_a, side_b, side_c, perimeter = request.param
    yield side_a, side_b, side_c, perimeter


@pytest.fixture
def get_circle_areas():
    def _wrapper(type_of_number: str):
        if type_of_number == "integer":
            return 4, 50.26548245743669
        if type_of_number == "float":
            return 1.5, 7.0685834705770345

    yield _wrapper


@pytest.fixture(
    params=[(3, 18.84955592153876), (2.5, 15.707963267948966)], ids=["integer", "float"]
)
def get_circle_perimeters(request):
    radius, perimeter = request.param
    yield radius, perimeter


@pytest.fixture
def circle_add_areas():
    def _wrapper(figure: str):
        if figure == Circle:
            return 191.63715186897738, 5, 6
        if figure == Rectangle:
            return 98.26548245743669, 4, 6, 8
        if figure == Square:
            return 37.56637061435917, 2, 5
        if figure == Triangle:
            return 40.06182478409421, 2, 5, 12, 11

    yield _wrapper


@pytest.fixture
def square_add_areas():
    def _wrapper(figure: str):
        if figure == Circle:
            return 138.09733552923257, 5, 6
        if figure == Rectangle:
            return 64, 4, 6, 8
        if figure == Square:
            return 29, 2, 5
        if figure == Triangle:
            return 31.49545416973504, 2, 5, 12, 11

    yield _wrapper


@pytest.fixture
def rectangle_add_areas():
    def _wrapper(figure: str):
        if figure == Circle:
            return 153.09733552923257, 5, 8, 6
        if figure == Rectangle:
            return 84, 4, 9, 6, 8
        if figure == Square:
            return 39, 7, 2, 5
        if figure == Triangle:
            return 37.49545416973504, 2, 5, 5, 12, 11

    yield _wrapper


@pytest.fixture
def triangle_add_areas():
    def _wrapper(figure: str):
        if figure == Circle:
            return 128.0785737958112, 5, 8, 6, 6
        if figure == Rectangle:
            return 62.14213562373095, 6, 9, 5, 6, 8
        if figure == Square:
            return 36.976539567003485, 7, 6, 4, 5
        if figure == Triangle:
            return 26.829266761386528, 2, 5, 5, 12, 11, 4

    yield _wrapper
