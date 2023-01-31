import pytest
from  isomorphic_string import are_isomorphic_strings

@pytest.mark.parametrize("input1, input2, expected", [("egg", "add", True),
                                            ("foo", "bar", False),
                                            ("paper", "title", True),
                                            ("", "", True),
                                            ("hey", "sjkfkalj", False),
                                            ("badc", "baba", False)])
def testValidInput(input1, input2, expected):
    assert are_isomorphic_strings(input1, input2) == expected