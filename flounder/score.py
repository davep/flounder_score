"""Tools to score a DNA sequence using the Flounder method."""

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
# Return the Flounder Score for a given sequence.
def score( sequence: str ) -> int:
    """Return the Flounder Score for the given sequence.

    :param str sequence: The sequence to score.
    :returns: The Flounder Score for the sequence.
    :rtype: int
    """
    return sum( SCORES.get( base, 0 ) for base in sequence.upper() )

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

### score.py ends here
