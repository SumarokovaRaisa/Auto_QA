from Simple_math import SimpleMath
import pytest

@pytest.fixture
def simple_math():
    return SimpleMath()


def test_positive_simple_math_square(simple_math):
    assert simple_math.square(4) == 16

def test_negative_simple_math_square(simple_math):
    assert simple_math.square(-7) == 49

def test_positive_simple_math_cube(simple_math):
    assert simple_math.cube(2) == 8


def test_negative_simple_math_cube(simple_math):
    assert simple_math.cube(-3) == -27