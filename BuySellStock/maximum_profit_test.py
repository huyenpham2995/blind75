import pytest
from  maximum_profit import get_maximum_profit_brute_force, get_maximum_profit_sliding_window

@pytest.mark.parametrize("input,expected", [([7,1,5,3,6,4], 5),
                                            ([7,6,4,3,1], 0),
                                            ([], 0),
                                            ([1], 0)])
def testValidInput(input, expected):
    assert get_maximum_profit_brute_force(input) == expected
    assert get_maximum_profit_sliding_window(input) == expected