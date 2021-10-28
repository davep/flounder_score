"""Flounder score library."""

##############################################################################
# Module information.
__author__     = "Dave Pearson"
__copyright__  = "Copyright 2019-2021, Dave Pearson"
__credits__    = [ "Dave Pearson" ]
__maintainer__ = "Dave Pearson"
__email__      = "davep@davep.org"
__version__    = "1.2.0"
__licence__    = "GPLv3+"

##############################################################################
# Imports for easier access by the user.
from .score import (
    score, scores,
    score_to_the_max, scores_to_the_max,
    codon_score, codon_scores,
)

##############################################################################
# Declare what you get if you import * from here.
__all__ = [
    "score",
    "scores",
    "score_to_the_max",
    "scores_to_the_max",
    "codon_score",
    "codon_scores"
]

### __init__.py ends here
