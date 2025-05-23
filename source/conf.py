# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os

# sys.path.append(os.path.abspath("../exts/"))

with open("version.txt") as f:
    version = f.read()

project = "Ndigo6G-12 User Guide"
copyright = "Creative Commons Attribution-NoDerivatives" " 4.0 International License"
author = "cronologic GmbH & Co. KG"
release = version

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autosectionlabel",
    "breathe",
]

breathe_projects = {"ndigo6g12_api": os.fspath("./doxygen/xml/")}
breathe_default_project = "ndigo6g12_api"
breathe_show_include = False
breathe_show_define_initializer = False

autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

with open("global.rst", "r") as f:
    prolog_file = f.read()
rst_prolog = f"""
{prolog_file}

.. |version| replace:: {version}
"""

templates_path = ["_templates"]
exclude_patterns = ["global.rst"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

cronoblue = "#376EB5"
cronolightblue = "#569fd6"
cronoorange = "#ED7807"
cronolightorange = "rgb(237, 120, 7, 0.2)"
cronogrey = "#737372"
cronolightgrey = "#acacac"
cronoverylightgrey = "#dcdcdc"

html_theme = "furo"
html_theme_options = {
    "dark_css_variables": {
        "color-brand-primary": cronolightblue,
        "color-brand-content": cronolightblue,
        "color-api-name": cronoorange,
        "color-sidebar-brand-text": cronolightblue,
        "color-highlight-on-target": cronolightorange,
        "color-foreground-primary": cronolightgrey,
        "color-headers": cronoverylightgrey,
        "color-first-header": cronoorange,
    },
    "light_css_variables": {
        "font-stack": "Montserrat, -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji",
        "font-stack--monospace": "Consolas, Monaco, Liberation Mono, Lucida Console, monospace",
        "color-foreground-primary": cronogrey,
        "color-headers": "#000000",
        "color-first-header": cronoorange,
        "color-brand-primary": cronoblue,
        "color-brand-content": cronoblue,
        "color-api-name": cronoorange,
        "color-sidebar-brand-text": cronoblue,
        "color-admonition-title--attention": cronoorange,
        "color-admonition-title-background--attention": cronolightorange,
        "color-highlight-on-target": cronolightorange,
        "sidebar-caption-space-above": "0",
    },
    "top_of_page_buttons": [],
}

html_favicon = "_static/cronologic_favicon.svg"
html_title = f"{project}"
html_secnumber_suffix = " "
html_logo = "_static/cronologic.svg"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

# latex_toplevel_sectioning = "section"

latex_engine = "xelatex"
latex_xindy_use = False
latex_elements = {
    "papersize": "a4paper",
    "pointsize": "12pt",
    "fontpkg": "",
    "preamble": r"""
        \usepackage[
            sphinx,
            noframe=false,
        ]
        {cronologicug}
        \definecolor{ctypered}{RGB}{142,33,0} % C-type auto highlighting color
        \newcommand{\docutilsrolectypered}[1]{{\color{ctypered} #1}}
        \newcommand{\docutilsrolered}[1]{{\color{red} #1}}
        \newcommand{\docutilsrolecronoblue}[1]{{\color{cronoblue} #1}}
        \setcounter{tocdepth}{4}
    """,
    "extraclassoptions": r"openany",
    "tableofcontents": r"\tableofcontents",
    "maketitle": r"\includepdf[pages={1}]{Ndigo6G-12_Front_Page.pdf}",
    "releasename": "Rev.",
    "makeindex": "",
    "printindex": "",
}
latex_theme = "manual"  # manual (book class) or howto (article class)
latex_additional_files = [
    "cronologicug.sty",
    "extraplaceins.sty",
    "Ndigo6G-12_Front_Page.pdf",
]

numfig = True
numfig_format = {"figure": "Figure %s:", "table": "Table %s:"}
numfig_secnum_depth = 1
