"""The Flounder Score library unit tests."""

##############################################################################
# General imports.
from unittest import main, TestCase

##############################################################################
# Local imports.
from flounder import score, scores, score_to_the_max, scores_to_the_max

##############################################################################
# Test the Flounder Score function.
class TestFlounderScore( TestCase ):
    """Test the main Flounder Score calculation."""

    def test_empty( self ):
        """Test that an empty sequence is handled."""
        self.assertEqual( score( "" ), 0 )

    def test_unknown( self ):
        """Test sequences containing things we don't score."""
        self.assertEqual( score( "1" ), 0 )
        self.assertEqual( score( "!" ), 0 )
        self.assertEqual( score( "§" ), 0 )

    def test_case( self ):
        """Test that we don't care about case."""
        self.assertEqual( score( "GTAC" ), 7 )
        self.assertEqual( score( "gtac" ), 7 )
        self.assertEqual( score( "GtAc" ), 7 )

##############################################################################
# Test the function that returns individual Flounder Scores.
class TestFlounderScores( TestCase ):
    """Test the main Flounder Scores function."""

    def test_empty( self ):
        """Test that an empty sequence is handled."""
        self.assertEqual( scores( "" ), [] )

    def test_unknown( self ):
        """Test sequences containing things we don't score."""
        self.assertEqual( scores( "1" ), [ ( "1", score( "1" ) ) ] )
        self.assertEqual( scores( "!" ), [ ( "!", score( "!" ) ) ] )
        self.assertEqual( scores( "§" ), [ ( "§", score( "§" ) ) ] )

    def test_scores( self ):
        """Test that the individual scores are correct."""
        self.assertEqual(
            scores( "GTAC" ), [ ( base, score( base ) ) for base in "GTAC" ]
        )

##############################################################################
# Test the Flounder Score function, to the max.
class TestFlounderScoreToTheMax( TestCase ):
    """Test the main Flounder Score calculation to the max!"""

    def test_empty( self ):
        """Test that an empty sequence is handled."""
        self.assertEqual( score_to_the_max( "" ), 0 )

    def test_unknown( self ):
        """Test sequence containing things we don't score."""
        self.assertEqual( score_to_the_max( "1" ), 0 )
        self.assertEqual( score_to_the_max( "!" ), 0 )
        self.assertEqual( score_to_the_max( "§" ), 0 )

    def test_case( self ):
        """Test that we don't care about case."""
        self.assertEqual( score_to_the_max( "GTAC" ), 86 )
        self.assertEqual( score_to_the_max( "gtac" ), 86 )
        self.assertEqual( score_to_the_max( "GtAc" ), 86 )

##############################################################################
# Test the function that returns individual Flounder Scores to the max.
class TestFlounderScoresToTheMax( TestCase ):
    """Test the main Flounder Scores calculation to the max!"""

    def test_empty( self ):
        """Test that an empty sequence is handled."""
        self.assertEqual( scores_to_the_max( "" ), [] )

    def test_unknown( self ):
        """Test sequences containing things we don't score."""
        self.assertEqual( scores_to_the_max( "1" ), [ ( "1", score_to_the_max( "1" ) ) ] )
        self.assertEqual( scores_to_the_max( "!" ), [ ( "!", score_to_the_max( "!" ) ) ] )
        self.assertEqual( scores_to_the_max( "§" ), [ ( "§", score_to_the_max( "§" ) ) ] )

    def test_scores( self ):
        """Test that the individual scores are correct."""
        self.assertEqual(
            scores_to_the_max( "GTAC" ), [
                ( base, score_to_the_max( base ) ) for base in "GTAC"
            ]
        )

##############################################################################
# Main entry point.
if __name__ == "__main__":
    main( verbosity=2 )

### tests.py ends here
