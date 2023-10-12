# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ndigo6G – User Guide'
copyright = ("Creative Commons Attribution-NoDerivatives"
             " 4.0 International License")
author = 'cronologic GmbH & Co. KG'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
]

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# PDF Output
latex_engine = 'xelatex'
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    "fontpkg" : "",
    "preamble": r"\usepackage[font=rtd]{sphinxcronologic}",
    "extraclassoptions": r"openany",
    "tableofcontents":r"""\tableofcontents""",
    "maketitle": r"\cronofront",
    "sphinxsetup": r"""
        TitleColor={rgb}{0.1686,0.4667,0.6941},
        hmargin={2.5cm,2.5cm},
        vmargin={2.5cm,2.5cm}
    """
}
# latex_toplevel_sectioning = "section" 
latex_theme = "manual" # manual (book class) or howto (article class)
latex_additional_files = ["sphinxcronologic.sty", "extraplaceins.sty"]

numfig = True
numfig_format = {
    "figure":"Figure %s:",
    "table":"Table %s:"
}
numfig_secnum_depth = 1