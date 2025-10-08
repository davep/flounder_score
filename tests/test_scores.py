"""Test the scores function."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Library imports.
from flounder_score import score, scores


##############################################################################
def test_empty() -> None:
    """An empty sequence should give an empty result."""
    assert scores("") == []


##############################################################################
@mark.parametrize(
    "sequence",
    (
        "1",
        "!",
        "§",
        "G",
        "T",
        "A",
        "C",
    ),
)
def test(sequence: str) -> None:
    """The scores function should give the expected result."""
    assert scores(sequence) == [(sequence, score(sequence))]


##############################################################################
def test_long_sequence() -> None:
    """The scores function should give the expected result when run on a long sequence."""
    assert scores(sequence := "GTACgtac") == [(base, score(base)) for base in sequence]


### test_scores.py ends here
