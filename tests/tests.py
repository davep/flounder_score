"""The Flounder Score library unit tests."""

##############################################################################
# General imports.
from unittest import main, TestCase

##############################################################################
# Local imports.
from flounder import score

##############################################################################
# Test the Flounder Score function.
class TestFlounderScore( TestCase ):

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
# Main entry point.
if __name__ == "__main__":
    main( verbosity=2 )

### tests.py ends here
