# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Ndigo'
copyright = '2023, Sulima'
author = 'Sulima'
release = '1.0'
# Enable numref
numfig = True
autosectionlabel_prefix_document = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autosectionlabel','sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.mathjax', 'sphinx.ext.viewcode','sphinx_numfig']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'sphinx_rtd_theme'
epub_theme = 'epub'
html_static_path = ['_static']
html_css_files = ['style.css']

