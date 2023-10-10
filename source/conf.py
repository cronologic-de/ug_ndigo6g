# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Ndigo6G - User Guide'
copyright = ("Creative Commons Attribution-NoDerivatives"
             " 4.0 International License")
author = 'cronologic GmbH & Co. KG'
release = '0.1'

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
    "preamble": r"\usepackage{sphinxcronologic}",
    "fncychap": "",#r"\usepackage[Bjornstrup]{fncychap}",
    "extraclassoptions": r"openany",
    "maketitle": r"\cronofront{../../source/XTDC4_title.pdf}",
    "tableofcontents":"",
    "maketitle": r"""
        \thispagestyle{empty}
        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (0,0)   { \includegraphics[width=155mm]{../../source/figures/cronologic.pdf}};
        \end{tikzpicture}

        \begin{minipage}{0.83\textwidth}
        \begin{tabular}{l}

        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (-8.1,1){\fontsize{20}{2}\selectfont
        \sectionfont 
        {\textcolor{org}{Ndigo5G-PCIe}}};

        \draw[align=center] node at (-8.3,0){\fontsize{20}{2}\selectfont
        \sffamily \textcolor{org}{USER GUIDE}};
        \end{tikzpicture}
        \\ \vspace{5pt}
        %{\efbox{
        %\hspace{-10pt}
        \includegraphics[width=120mm,height=150mm,keepaspectratio]{../../source/figures/Title5G.pdf}
        %}}
        \\
        \end{tabular}
        \end{minipage}
        \begin{minipage}{0\textwidth}
        \vspace{25pt}
        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (0,-5){ 
        \fontsize{80}{2}\selectfont
        \ttfamily \textcolor{org}{ \rotatebox{90}{Ndigo5G-PCIe}}};
        \end{tikzpicture}
        \end{minipage}

        \vspace{-25pt}
        \begin{minipage}{0\textwidth}
        \begin{tikzpicture}
        \draw[inner sep=0pt] node at (-3,-18){\fontsize{20}{2}\selectfont
        \sffamily \textcolor{gry}{~\url{www.cronologic.de}}};
        \end{tikzpicture}
        \end{minipage}
        \newpage
    """,
    "sphinxsetup": r"""
        TitleColor={rgb}{0.1686,0.4667,0.6941}
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