"""The Flounder Score library unit tests."""

##############################################################################
# General imports.
from itertools import product
from unittest  import main, TestCase

##############################################################################
# Local imports.
from flounder import (
    score, scores,
    score_to_the_max, scores_to_the_max,
    codon_score, codon_scores
)

##############################################################################
# Test the Flounder Score function.
class TestFlounderScore( TestCase ):
    """Test the main Flounder Score calculation."""

    def test_empty( self ) -> None:
        """Test that an empty sequence is handled."""
        self.assertEqual( score( "" ), 0 )

    def test_unknown( self ) -> None:
        """Test sequences containing things we don't score."""
        self.assertEqual( score( "1" ), 0 )
        self.assertEqual( score( "!" ), 0 )
        self.assertEqual( score( "§" ), 0 )

    def test_case( self ) -> None:
        """Test that we don't care about case."""
        self.assertEqual( score( "GTAC" ), 7 )
        self.assertEqual( score( "gtac" ), 7 )
        self.assertEqual( score( "GtAc" ), 7 )

##############################################################################
# Test the function that returns individual Flounder Scores.
class TestFlounderScores( TestCase ):
    """Test the main Flounder Scores function."""

    def test_empty( self ) -> None:
        """Test that an empty sequence is handled."""
        self.assertEqual( scores( "" ), [] )

    def test_unknown( self ) -> None:
        """Test sequences containing things we don't score."""
        self.assertEqual( scores( "1" ), [ ( "1", score( "1" ) ) ] )
        self.assertEqual( scores( "!" ), [ ( "!", score( "!" ) ) ] )
        self.assertEqual( scores( "§" ), [ ( "§", score( "§" ) ) ] )

    def test_scores( self ) -> None:
        """Test that the individual scores are correct."""
        self.assertEqual(
            scores( "GTAC" ), [ ( base, score( base ) ) for base in "GTAC" ]
        )

##############################################################################
# Test the Flounder Score function, to the max.
class TestFlounderScoreToTheMax( TestCase ):
    """Test the main Flounder Score calculation to the max!"""

    def test_empty( self ) -> None:
        """Test that an empty sequence is handled."""
        self.assertEqual( score_to_the_max( "" ), 0 )

    def test_unknown( self ) -> None:
        """Test sequence containing things we don't score."""
        self.assertEqual( score_to_the_max( "1" ), 0 )
        self.assertEqual( score_to_the_max( "!" ), 0 )
        self.assertEqual( score_to_the_max( "§" ), 0 )

    def test_case( self ) -> None:
        """Test that we don't care about case."""
        self.assertEqual( score_to_the_max( "GTAC" ), 86 )
        self.assertEqual( score_to_the_max( "gtac" ), 86 )
        self.assertEqual( score_to_the_max( "GtAc" ), 86 )

##############################################################################
# Test the function that returns individual Flounder Scores to the max.
class TestFlounderScoresToTheMax( TestCase ):
    """Test the main Flounder Scores calculation to the max!"""

    def test_empty( self ) -> None:
        """Test that an empty sequence is handled."""
        self.assertEqual( scores_to_the_max( "" ), [] )

    def test_unknown( self ) -> None:
        """Test sequences containing things we don't score."""
        self.assertEqual( scores_to_the_max( "1" ), [ ( "1", score_to_the_max( "1" ) ) ] )
        self.assertEqual( scores_to_the_max( "!" ), [ ( "!", score_to_the_max( "!" ) ) ] )
        self.assertEqual( scores_to_the_max( "§" ), [ ( "§", score_to_the_max( "§" ) ) ] )

    def test_scores( self ) -> None:
        """Test that the individual scores are correct."""
        self.assertEqual(
            scores_to_the_max( "GTAC" ), [
                ( base, score_to_the_max( base ) ) for base in "GTAC"
            ]
        )

##############################################################################
# Test the function that returns the codon-based flounder score.
class TestCodonFlounderScore( TestCase ):
    """Test the codon-based Flounder scoring function."""

    def test_empty( self ) -> None:
        """Test that an empty sequence is handled."""
        self.assertEqual( codon_score( "" ), 0 )

    def test_unknown( self ) -> None:
        """Test sequences containing things we don't score."""
        self.assertEqual( codon_score( "111" ), 0 )
        self.assertEqual( codon_score( "!!!" ), 0 )
        self.assertEqual( codon_score( "§§§" ), 0 )

    def test_short( self ) -> None:
        """Test sequences that are short of having a full codon."""
        self.assertEqual( codon_score( "A" ), 0 )
        self.assertEqual( codon_score( "AA" ), 0 )

    def test_case( self ) -> None:
        """Test that we don't care about case."""
        self.assertEqual( codon_score( "AAA" ), 5 )
        self.assertEqual( codon_score( "aaa" ), 5 )
        self.assertEqual( codon_score( "AaA" ), 5 )

    def test_some_short( self ) -> None:
        """Test that a short sequence that has codons gives a score."""
        self.assertEqual( codon_score( "AAAA" ), 5 )
        self.assertEqual( codon_score( "AAAAA" ), 5 )

##############################################################################
# Test the function that returns individual codon-based Flounder Scores.
class TestCodonFlounderScores( TestCase ):
    """Test the codon-based Flounder Scores function."""

    def test_empty( self ) -> None:
        """Test that an empty sequences is handled."""
        self.assertEqual( codon_scores( "" ), [] )

    def test_unknown( self ) -> None:
        """Test sequences containing things we don't score."""
        self.assertEqual( codon_scores( "111" ), [ ( "111", codon_score( "111" ) ) ] )
        self.assertEqual( codon_scores( "!!!" ), [ ( "!!!", codon_score( "!!!" ) ) ] )
        self.assertEqual( codon_scores( "§§§" ), [ ( "§§§", codon_score( "§§§" ) ) ] )

    def test_short( self ) -> None:
        """Test sequences that are short of having a full codon."""
        self.assertEqual( codon_scores( "A" ), [] )
        self.assertEqual( codon_scores( "AA" ), [] )

    def test_some_short( self ) -> None:
        """Test that a short sequence that has codons gives a score."""
        self.assertEqual( codon_scores( "AAAA" ), [ ( "AAA", 5 ) ] )
        self.assertEqual( codon_scores( "AAAAA" ), [ ( "AAA", 5 ) ] )

    def test_all_scored( self ) -> None:
        """Test that every codon gets some sort of score."""
        self.assertEqual(
            len( codon_scores( "".join( "".join( codon ) for codon in product( "GTAC", repeat=3 ) ) ) ),
            64
        )

##############################################################################
# Main entry point.
if __name__ == "__main__":
    main( verbosity=2 )

### tests.py ends here
