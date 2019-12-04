import pytest

from task1.task import preprocess, validate


@pytest.mark.parametrize(
    "tokens,string,result",
    [
        (["ab", "bc", "a" ], "abc", True),
        ([ "a", "ab", "bc" ], "ab", True),
        ([ "a", "ab", "bc" ], "", True),
        ([ "ab", "bc" ], "abc", False),
        ([ "ab", "bc", "c" ], "abbcbc", True),

    ]
)
def test_validate(tokens, string, result):
    tokens = preprocess(tokens)
    assert validate(tokens, string) is result




