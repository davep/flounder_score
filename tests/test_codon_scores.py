"""Test the codon_scores function."""

##############################################################################
# Python imports.
from itertools import product

##############################################################################
# Pytest imports.
from pytest import mark

##############################################################################
# Library imports.
from flounder import codon_score, codon_scores


##############################################################################
@mark.parametrize("sequence", ("", "A", "AA"))
def test_no_codon(sequence: str) -> None:
    """A sequence that isn't long enough to be a codon should result in an empty result."""
    assert codon_scores(sequence) == []


##############################################################################
@mark.parametrize(
    "sequence",
    (
        "111",
        "!!!",
        "§§§",
        "GGG",
        "TTT",
        "AAA",
        "CCC",
    ),
)
def test(sequence: str) -> None:
    """The codon_scores function should give the expected result."""
    assert codon_scores(sequence) == [(sequence, codon_score(sequence))]


##############################################################################
def test_all_scored() -> None:
    """Test that every codon gets some sort of score."""
    assert (
        len(
            codon_scores("".join("".join(codon) for codon in product("GTAC", repeat=3)))
        )
        == 64
    )


### test_codon_scores.py ends here
