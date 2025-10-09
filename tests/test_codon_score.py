"""Test the codon_score function."""

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Library imports.
from flounder import codon_score


##############################################################################
@mark.parametrize(
    "sequence, expected_result",
    (
        ("", 0),
        ("111", 0),
        ("!!!", 0),
        ("§§§", 0),
        ("A", 0),
        ("AA", 0),
        ("AAA", 5),
        ("aaa", 5),
        ("AaA", 5),
        ("AAAA", 5),
        ("AAAAA", 5),
    ),
)
def test(sequence: str, expected_result: int) -> None:
    """The codon_score function should give the expected result."""
    assert codon_score(sequence) == expected_result


### test_codon_score.py ends here
