import pytest
from  is_subsequence import is_subsequence

@pytest.mark.parametrize("input1, input2, expected", [("abc", "ahbgdc", True),
                                            ("", "", True),
                                            ("", "ajdhsa", True),
                                            ("axc", "ahbgdc", False)])
def testValidInput(input1, input2, expected):
    assert is_subsequence(input1, input2) == expected