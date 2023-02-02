import pytest
from  longest_palindrome import longest_palindrome

@pytest.mark.parametrize("input,expected", [("abccccdd", 7),
                                            ("", 0),
                                            ("a", 1),
                                            ("arbbbhbk", 5),
                                            ("cdfbaabb", 5)])
def testValidInput(input, expected):
    assert longest_palindrome(input) == expected