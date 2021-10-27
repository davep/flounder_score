"""Tools to score a DNA sequence using the Flounder method."""

##############################################################################
# Python imports.
import re
from typing import List, Tuple

##############################################################################
# Dictionary of scores for each letter.
SCORES = {
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
    "Z": 10
}

##############################################################################
# Dictionary of base to IUAPC code mappings for extra scoring.
IUAPC = {
    "G": "RSKBDVN",
    "T": "YWKBDHN",
    "U": "YWKBDHN",
    "A": "RWMDHVN",
    "C": "YSMBHVN"
}

##############################################################################
# Codon to AA mapping.
CODON_MAP = {
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
    "GTN": "V"
}

##############################################################################
# Return the Flounder Score for a given sequence.
def score( sequence: str ) -> int:
    """Return the Flounder Score for the given sequence.

    :param str sequence: The sequence to score.
    :returns: The Flounder Score for the sequence.
    :rtype: int
    """
    return sum( SCORES.get( base, 0 ) for base in sequence.upper() )

##############################################################################
# Return a list of individual Flounder Scores for a given sequence.
def scores( sequence: str ) -> List[ Tuple[ str, int ] ]:
    """Return a list of individual bases with their scores from the sequence.

    :param str sequence: The sequence to score.
    :returns: A list of tuples, the base in the first position, the score in the second.
    :rtype: List[Tuple[str,int]]
    """
    return [ ( base, score( base ) ) for base in sequence ]

##############################################################################
# Return the to-the-max Flounder Score for a given sequence.
def score_to_the_max( sequence: str ) -> int:
    """Return the to-the-max Flounder Score for the given sequence.

    :param str sequence: The sequence to score.
    :returns: The Flounder Score for the sequence.
    :rtype: int

    The to-the-max Flounder Score is like the Flounder Score, but other than
    scoring the individual base, it scores based on the base and also every
    IUAPC code that applies.
    """
    return score( sequence ) + sum(
        score( IUAPC.get( base, "" ) ) for base in sequence.upper()
    )

##############################################################################
# Return a list of individual to-the-max Flounder Scores for a given sequence.
def scores_to_the_max( sequence: str ) -> List[ Tuple[ str, int ] ]:
    """Return a list of individual base to-the-max scores.

    :param str sequence: The sequence to score.
    :returns: A list of tuples, the base in the first position, the score in the second.
    :rtype: List[Tuple[str,int]]
    """
    return [ ( base, score_to_the_max( base ) ) for base in sequence ]

##############################################################################
# Return the codon-based Flounder score for a given sequence.
def codon_score( sequence: str ) -> int:
    """Return the codon-based Flounder Score for the given sequence.

    :param str sequence: The sequence to score.
    :returns: The Flounder Score for the sequence.
    :rtype: int

    This scoring system translates the codons in the sequence into AA codes,
    and then builds a score based on them. Translation of the sequence
    always starts with the first base, and keeps going as long as there are
    codons left. Stop codons are scored as 0 and worked past.
    """
    return sum(
        SCORES.get( CODON_MAP.get( codon, "" ), 0 ) for codon in re.findall( "...", sequence.upper() )
    )

##############################################################################
# Return a list of individual codon-based Flounder scores for a sequence.
def codon_scores( sequence: str ) -> List[ Tuple[ str, int] ]:
    """Return a list of codon-based Flounder Scores for the given sequence.

    :param str sequence: The sequence to score.
    :returns: A list of tuples, the codon and its score.
    :rtype: List[Tuple[str,int]]

    This scoring system translates the codons in the sequence into AA codes,
    and then builds a score based on them. Translation of the sequence
    always starts with the first base, and keeps going as long as there are
    codons left. Stop codons are scored as 0 and worked past.
    """
    return [ ( codon, codon_score( codon ) ) for codon in re.findall( "...", sequence ) ]

### score.py ends here
