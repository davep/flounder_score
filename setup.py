"""Setup file for the Flounder Score library."""

##############################################################################
# Python imports.
from pathlib    import Path
from setuptools import setup, find_packages

##############################################################################
# Import the library itself to pull details out of.
import flounder

##############################################################################
# Work out the location of the README file.
def readme():
    """Return the full path to the README file.

    :returns: The path to the README file.
    :rtype: ~pathlib.Path
    """
    return Path( __file__).parent.resolve() / "README.md"

##############################################################################
# Load the long description for the package.
def long_desc():
    """Load the long description of the package from the README.

    :returns: The long description.
    :rtype: str
    """
    with readme().open( "r", encoding="utf-8" ) as rtfm:
        return rtfm.read()

##############################################################################
# Perform the setup.
setup(

    name                          = "flounder_score",
    version                       = flounder.__version__,
    description                   = flounder.__doc__,
    long_description              = long_desc(),
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/davep/flounder_score",
    author                        = flounder.__author__,
    author_email                  = flounder.__email__,
    maintainer                    = flounder.__maintainer__,
    maintainer_email              = flounder.__email__,
    license                       = "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    packages                      = find_packages(),
    package_data                  = { "flounder": [ "py.typed" ] },
    include_package_data          = True,
    python_requires               = ">=3.5",
    classifiers                   = (
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)"
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
        "Typing :: Typed",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    )

)

### setup.py ends here
