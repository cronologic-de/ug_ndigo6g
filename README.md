#   Project Setup and Installation  


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





#   Project Structure


The project cotaines multiple folders and files:

1. conf.py: Configuration file for the Sphinx documentation builder.

2. Readme.md: Contains documentation related to project

3. _build: Containes doctree and HTML files against all RST files.

4. Output.pdf: it exist under "\_build\html\output.pdf" but you can place it any where.

5. _bulid\html\images: This folder contains all images which are displayed on HTML pages.

6. _bulid\html\static: Contains all relevent CSS,JQuery and JS files.

7. RST: This folder contains all RST files including main RST.

8. RST\figures: All figures which will displayed on PDF





#   New Project Setup and Installation


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

12. Then just make html

    - .\make html

13. To create RST2PDF:

    rst2pdf  -s _static/style.css <rst_file> -o <pdf_file>
    
    
    sample command: rst2pdf -s _static\style.css  C:\Users\zeiqbal\PycharmProjects\Ndigov1.1\RST\Ndigo_Intro.rst  C:\Users\zeiqbal\PycharmProjects\Ndigov1.1\output.pdf



# Steps for Ndigo_API Section using Doxygen


1. First you need to install Doxywizard to run the C header file and convert it 
   into latex.
   
2. Select destination directory same as your sphinx project directory while converting
   C header file to latex.
   
3. After successful conversion a folder will be created under sphinx project.

4. Now install these libraries in you python IDE as well as set it as global variable in you PC.
   
   - pip install panadoc 
   
   - Or go there https://github.com/jgm/pandoc/releases/tag/3.1.6
   
   - Install this one "pandoc-3.1.6-windows-x86_64.zip" from the link provided.
   
   - if pandoc is installed in C:\Program Files\Pandoc, and it's not globally available, follow these steps to set it as global:
   
   - Open the "Start" menu and search for "Environment Variables."
   
   - Click on "Edit the system environment variables."
   
   - In the System Properties window, click on the "Environment Variables" button at the bottom.
   
   - In the Environment Variables window, under "System variables," scroll down and find the "Path" variable. Select it and click on the "Edit" button.
   
   - Click on the "New" button and add the path to the directory where pandoc is installed, which is C:\Program Files\Pandoc in this example.
   
   - Click "OK" to close all windows. The changes should take effect immediately in any newly opened terminal or command prompt.

5. Then check your Doxygen generated Ndigo_API.tex file which will be created under a folder name as latex.

6. To convert latex to RST use this "test.py" just place right path or input / output path in it and run the script.

7. A new RST will be created under specified output folder you can check RST and remove extra slashes and make formulas properly.

8. After modification on RST will be done use similar command which we used previously to convert RST2PDF.


 









