# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ndigo6G-12 User Guide'
copyright = '2022, Kolja Sulimma'
author = 'Kolja Sulimma'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Specify the path to Doxyrest extensions for Sphinx:
import sys
import os 
sys.path.insert(1, os.path.abspath('C:\Program Files\doxyrest-2.1.3-windows-amd64\sphinx'))

extensions = ['doxyrest', 'cpplexer']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
