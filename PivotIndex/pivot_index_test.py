import pytest
from  pivot_index import find_pivot_index

@pytest.mark.parametrize("input,expected", [([1,7,3,6,5,6], 3),
                                            ([1,2,3], -1),
                                            ([], -1),
                                            ([0], 0),
                                            ([2,1,-1], 0)])
def testValidInput(input, expected):
    assert find_pivot_index(input) == expected