"""Setup file for the Flounder Score library."""

##############################################################################
# Imports.
from os         import path
from setuptools import setup, find_packages

##############################################################################
# Import the library itself to pull details out of.
import flounder

##############################################################################
# Work out the location of the README file.
def readme() -> str:
    """Return the full path to the README file.

    :returns: The path to the README file.
    :rtype: str
    """
    return path.join( path.abspath( path.dirname( __file__ ) ), "README.md" )

##############################################################################
# Load the long description for the package.
def long_desc() -> str:
    """Load the long description of the package from the README.

    :returns: The long description.
    :rtype: str
    """
    with open( readme() ) as rtfm:
        return rtfm.read()

##############################################################################
# Perform the setup.
setup(

    name                 = "flounder",
    version              = flounder.__version__,
    description          = flounder.__doc__,
    long_description     = long_desc(),
    url                  = "https://github.com/davep/flounder_score",
    author               = flounder.__author__,
    author_email         = flounder.__email__,
    maintainer           = flounder.__maintainer__,
    maintainer_email     = flounder.__email__,
    license              = "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    packages             = find_packages(),
    include_package_data = True,
    python_requires      = ">=3.7"

)

### setup.py ends here
