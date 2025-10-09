"""Test the score function."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Library imports.
from flounder import score


##############################################################################
@mark.parametrize(
    "sequence, expected_result",
    (
        ("", 0),
        ("1", 0),
        ("!", 0),
        ("§", 0),
        ("GTAC", 7),
        ("gtac", 7),
        ("GtAc", 7),
    ),
)
def test(sequence: str, expected_result: int) -> None:
    """The score function should give the expected result."""
    assert score(sequence) == expected_result


### test_score.py ends here
