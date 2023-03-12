#############   Project Setup and Installation  ###########


1. Clone the branch named as "ndigo6g_updated" or you can download a zip.
2. Download and install Python on your system version3 or latest one from here:
   link: https://www.python.org/downloads/
3. Download and install pip which helps us to install python libraries, by using following command. 
   - python get-pip.py
   - pip --version
   or you can download pip directly from google and then install it on your system.
4. Then you need to install any IDE to run python project and for libraries installation.
   Some famous IDEs for Python are :
           - Pychram
           - Visual Studio Code
           - Anaconda
   link: https://www.jetbrains.com/pycharm/download/#section=windows
   We are using Pycharm in this project.
5. After setting up your IDE select python interpreter(the python which is installed). 
6. Extract your clone project in a folder and open it from IDE. 
7. Then create a virtual environment by using these commands on terminal.
   - python -m venv myenv
   - myenv\Scripts\activate
   After these commands new 
   
8. Then install these libraries by executing these commands on terminal
   - pip install -U sphinx
   - sphinx-build --version
   - pip install sphinx_rtd_theme
   - pip install rst2pdf
9. Main file which convert RST2 pdf is "Ndigo_Intro.rst"

10. After Installation you just need to run your RST2PDF to generate PDF
    - rst2pdf  -s _static/style.css <rst_file> -o <pdf_file>
    
    
    sample command: rst2pdf -s _static\style.css  C:\Users\zeiqbal\PycharmProjects\Ndigov1.1\RST\Ndigo_Intro.rst   C:\Users\zeiqbal\PycharmProjects\Ndigov1.1\output.pdf





#####################   Project Structure #######################


The project cotaines multiple folders and files:
1. conf.py: Configuration file for the Sphinx documentation builder.
2. Readme.md: Contains documentation related to project
3. _build: Containes doctree and HTML files against all RST files.
4. Output.pdf: It is actuall pdf file which is genrated as output.
5. _bulid\html\images: This folder contains all images which are displayed on HTML pages.
6. _bulid\html\static: Contains all relevent CSS,JQuery and JS files.
7. RST: This folder contains all RST files including main RST.
8. RST\figures: All figures which will displayed on PDF





#############   New Project Setup and Installation ##############


1. Download and install Python on your system version3 or latest one from here:
   link: https://www.python.org/downloads/
2. Download Pip which helps us to install python libraries.
3. Then you need to install any IDE to run python project and for libraries installation.
   Some famous IDEs for Python are :
           - Pychram
           - Visual Studio Code
           - Anaconda
   link: https://www.jetbrains.com/pycharm/download/#section=windows
   We are using Pycharm in this project.
4. Create a new project on Pycharm and create a new Virtual environment using these commands:
   - python -m venv myenv
   - myenv\Scripts\activate
   
5. Go to pycharm you just need to install libraries using pip on terminal:
    - pip install -U sphinx
    - sphinx-build --version
    - pip install sphinx_rtd_theme
6. Alternatively, you can put your all libraries in a rquirement.txt file and then just run this commands
   - pip install -r requirement.txt
    
    
7. After Installation to start with sphinx you need to run this command on terminal:
    - sphinx-quickstart

8. In "conf.py"  makes these changes
    - on top import these three libraries:
        - import os
        - import sys
        - sys.path.insert(0, os.path.abspath('..'))

9. Changes extensions value under "conf.py" to this:
    - extensions=['sphinx.ext.autodoc'] 

10. Also change html_theme to:
    -sphinx_rtd_theme


11. Then write this command on terminal:
    - sphinx-apidoc -o . .. (This will create RST for us)

12. Then just make html you need to rename the folder htmlfiles to html then run this command
    - .\make html

13. To create RST2PDF:
    rst2pdf  -s _static/style.css <rst_file> -o <pdf_file>
    
    
    sample command: rst2pdf -s _static\style.css  C:\Users\zeiqbal\PycharmProjects\Ndigov1.1\RST\Ndigo_Intro.rst   C:\Users\zeiqbal\PycharmProjects\Ndigov1.1\output.pdf





 









