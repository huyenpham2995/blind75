import pytest
from  running_sum import running_sum

@pytest.mark.parametrize("input,expected", [([1,2,3,4], [1,3,6,10]),
                                            ([1,1,1,1,1], [1,2,3,4,5]),
                                            ([], []),
                                            ([0,0,0,0], [0,0,0,0]),
                                            ([3,1,2,10,1], [3,4,6,16,17])])
def testValidInput(input, expected):
    assert running_sum(input) == expected