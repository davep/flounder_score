"""Flounder score library documentation config."""

##############################################################################
# Python imports.
import os
import re
import sys

##############################################################################
# Path setup.
sys.path.insert( 0, os.path.abspath( "../.." ) )

##############################################################################
# Get the Flounder Score version.
from flounder import __version__ as flounder_version

##############################################################################
# Project information
project   = "flounder_score"
copyright = "2019, Dave Pearson"
author    = "Dave Pearson"
version   = "v{}".format( re.sub( r"^(.*)\..*$", r"\1", flounder_version ) )
release   = "v{}".format( flounder_version )

##############################################################################
# General configuration.
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True
}
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx"
]
templates_path    = [ "_templates" ]
source_suffix     = ".rst"
master_doc        = "index"
language          = None
exclude_patterns  = []
pygments_style    = "sphinx"
autoclass_content = "both"

##############################################################################
# Options for HTML output
html_theme           = "nature"
html_static_path     = [ "_static" ]
html_show_sourcelink = False

##############################################################################
# Options for HTMLHelp output
htmlhelp_basename = "flounder_score"

##############################################################################
# Options for todo extension
todo_include_todos = True

##############################################################################
# Link to the python docs
intersphinx_mapping = {
    "python": ( "https://docs.python.org/3.7", None )
}

### conf.py ends here
