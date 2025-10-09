"""Test the score_to_the_max function."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Library imports.
from flounder import score_to_the_max


##############################################################################
@mark.parametrize(
    "sequence, expected_result",
    (
        ("", 0),
        ("1", 0),
        ("!", 0),
        ("§", 0),
        ("GTAC", 86),
        ("gtac", 86),
        ("GtAc", 86),
    ),
)
def test(sequence: str, expected_result: int) -> None:
    """The score_to_the_max function should give the expected result."""
    assert score_to_the_max(sequence) == expected_result


### test_score_to_the_max.py ends here
