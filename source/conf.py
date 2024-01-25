# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

# sys.path.append(os.path.abspath("../exts/"))

project = 'Ndigo6G-12 – User Guide'
copyright = ("Creative Commons Attribution-NoDerivatives"
             " 4.0 International License")
author = 'cronologic GmbH & Co. KG'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "breathe",
]

breathe_projects = {"ndigo6g12_api": os.fspath("./doxygen_build/xml/")}
breathe_default_project = "ndigo6g12_api"
breathe_show_include = False
breathe_show_define_initializer = True

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 2

rst_prolog = open("global.rst", "r").read()

templates_path = ['_templates']
exclude_patterns = ["global.rst"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"#'sphinx_rtd_theme'
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
    ]
}
html_theme_options = {
    "font_family" : "Montserrat, sans-serif",
    "extra_nav_links": {"Back to all User Guides": "https://docs.cronologic.de/"},
    "sidebar_collapse": True,
    "show_relbar_bottom": True,
    "fixed_sidebar": True,
    "sidebar_width": 400,
    "page_width": 1200, 
    "logo": "cronologic.svg",
    "description": f"{project}",
    "show_powered_by": False,
    "touch_icon": "cronologic_favicon.svg",
    # colors
    "body_text" : "#737372",
    "link_hover": "#376EB5",
}
html_favicon = "_static/cronologic_favicon.svg"
html_title = f"{project}"
html_secnumber_suffix = " "
html_static_path = ['_static']
html_css_files = ["custom.css"]

# latex_toplevel_sectioning = "section" 

latex_engine = 'xelatex'
latex_xindy_use = False
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    "fontpkg" : "",
    "preamble": r"""
        \usepackage[
            font=montserrat,
            sphinx,
            noframe=false,
        ]
        {cronologicug}
        \definecolor{ctypered}{RGB}{142,33,0} % C-type auto highlighting color
        \newcommand{\docutilsrolectypered}[1]{{\color{ctypered} #1}}
        \newcommand{\docutilsrolered}[1]{{\color{red} #1}}
        \newcommand{\docutilsrolecronoblue}[1]{{\color{cronoblue} #1}}
    """,
    "extraclassoptions": r"openany",
    "tableofcontents":r"\tableofcontents",
    "maketitle": r"",
    "releasename": "Rev.",
}
latex_theme = "manual" # manual (book class) or howto (article class)
latex_additional_files = [
    "cronologicug.sty",
    "extraplaceins.sty",
]


numfig = True
numfig_format = {
    "figure":"Figure %s:",
    "table":"Table %s:"
}
numfig_secnum_depth = 1