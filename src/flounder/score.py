"""Tools to score a DNA sequence using the Flounder method."""

##############################################################################
# Python imports.
from re import findall
from typing import Final

##############################################################################
_SCORES: Final[dict[str, int]] = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}
"""Scores for each letter of the alphabet."""

##############################################################################
_IUAPC: Final[dict[str, str]] = {
    "G": "RSKBDVN",
    "T": "YWKBDHN",
    "U": "YWKBDHN",
    "A": "RWMDHVN",
    "C": "YSMBHVN",
}
"""Base to IUAPC code mappings for extra scoring."""

##############################################################################
_CODON_MAP: Final[dict[str, str]] = {
    # Alanine
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GCN": "A",
    # Arginine
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "AGA": "R",
    "AGG": "R",
    "CGN": "R",
    "AGR": "R",
    # Asparagine
    "AAT": "N",
    "AAC": "N",
    "AAY": "N",
    # Aspartic acid
    "GAT": "D",
    "GAC": "D",
    "GAY": "D",
    # Cysteine
    "TGT": "C",
    "TGC": "C",
    "TGY": "C",
    # Glutamine
    "CAA": "Q",
    "CAG": "Q",
    "CAR": "Q",
    # Glutamic acid
    "GAA": "E",
    "GAG": "E",
    "GAR": "E",
    # Glycine
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
    "GGN": "G",
    # Histidine
    "CAT": "H",
    "CAC": "H",
    "CAY": "H",
    # Isoleucine
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATH": "I",
    # Tyrosine
    "TTA": "L",
    "TTG": "L",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "YTR": "L",
    "CTN": "L",
    # Lysine
    "AAA": "K",
    "AAG": "K",
    "AAR": "K",
    # Methionine
    "ATG": "M",
    # Phenylalanine
    "TTT": "F",
    "TTC": "F",
    "TTY": "F",
    # Proline
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CCN": "P",
    # Serine
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "AGT": "S",
    "AGC": "S",
    "TCN": "S",
    "AGY": "S",
    # Threonine
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "ACN": "T",
    # Tryptophan
    "TGG": "W",
    # Tyrosine
    "TAT": "Y",
    "TAC": "Y",
    "TAY": "Y",
    # Valine
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GTN": "V",
}
"""Codon to amino acid mapping."""


##############################################################################
def score(sequence: str) -> int:
    """Return the flounder score for the given sequence.

    Args:
        sequence: The sequence to score.

    Returns:
        The flounder score.
    """
    return sum(_SCORES.get(base, 0) for base in sequence.upper())


##############################################################################
def scores(sequence: str) -> list[tuple[str, int]]:
    """Return a list of individual bases with their scores from the sequence.

    Args:
        sequence: The sequence to score.

    Returns:
        A list of tuples, the base in the first position, the
            [`score`][flounder.score.score] in the second.
    """
    return [(base, score(base)) for base in sequence]


##############################################################################
def score_to_the_max(sequence: str) -> int:
    """Return the to-the-max Flounder Score for the given sequence.

    Args:
        sequence: The sequence to score.

    Returns:
        The flounder score for the sequence.

    The to-the-max flounder score is like the flounder score, but other than
    scoring the individual base, it scores based on the base and also every
    [IUAPC code](https://www.bioinformatics.org/sms/iupac.html) that applies.
    """
    return score(sequence) + sum(
        score(_IUAPC.get(base, "")) for base in sequence.upper()
    )


##############################################################################
def scores_to_the_max(sequence: str) -> list[tuple[str, int]]:
    """Return a list of individual base to-the-max scores.

    Args:
        sequence: The sequence to score.

    Returns:
        A list of tuples, the base in the first position,
            the [`score`][flounder.score.score] in the second.
    """
    return [(base, score_to_the_max(base)) for base in sequence]


##############################################################################
def codon_score(sequence: str) -> int:
    """Return the codon-based Flounder Score for the given sequence.

    Args:
        sequence: The sequence to score.

    Returns:
        The score for the sequence.

    This scoring system translates the codons in the sequence into AA codes,
    and then builds a score based on them. Translation of the sequence
    always starts with the first base, and keeps going as long as there are
    codons left. Stop codons are scored as 0 and worked past.
    """
    return sum(
        _SCORES.get(_CODON_MAP.get(codon, ""), 0)
        for codon in findall("...", sequence.upper())
    )


##############################################################################
def codon_scores(sequence: str) -> list[tuple[str, int]]:
    """Return a list of codon-based Flounder Scores for the given sequence.

    Args:
        sequence: The sequence to score.

    Returns:
        A list of tuples, the codon and its [score][flounder.score.codon_score].

    This scoring system translates the codons in the sequence into AA codes,
    and then builds a score based on them. Translation of the sequence
    always starts with the first base, and keeps going as long as there are
    codons left. Stop codons are scored as 0 and worked past.
    """
    return [(codon, codon_score(codon)) for codon in findall("...", sequence)]


### score.py ends here
