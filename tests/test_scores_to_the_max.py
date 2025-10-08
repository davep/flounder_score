"""Test the scores_to_the_max function."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Library imports.
from flounder_score import score_to_the_max, scores_to_the_max


##############################################################################
def test_empty() -> None:
    """An empty sequence should give an empty result."""
    assert scores_to_the_max("") == []


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
    """The scores_to_the_max function should give the expected result."""
    assert scores_to_the_max(sequence) == [(sequence, score_to_the_max(sequence))]


##############################################################################
def test_long_sequence() -> None:
    """The scores_to_the_max function should give the expected result when run on a long sequence."""
    assert scores_to_the_max(sequence := "GTACgtac") == [
        (base, score_to_the_max(base)) for base in sequence
    ]


### test_scores_to_the_max.py ends here
