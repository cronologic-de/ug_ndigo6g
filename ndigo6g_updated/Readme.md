Go to pycharm install theme libs:

- pip install -U sphinx
- sphinx-build --version
- pip install sphinx_rtd_theme

Then create a new folder Docs under current project 
on terminal go inside Docs


create a sample python file with one function


Then after write these commands
	- sphinx-quickstart


under Docs/conf.py

makes these changes
	- on top
		- import os
		- import sys
		- sys.path.insert(0, os.path.abspath('..'))

changes extensions value to this:
	- extensions=['sphinx.ext.autodoc'] 
also change html_theme to:

   -  sphinx_rtd_theme


then write this command on terminal:
	- sphinx-apidoc -o . .. (This will create rst for us)


Then just make html
	- .\make html


To create RST2PDF:
rst2pdf  -s _static/style.css <rst_file> -o <pdf_file>


