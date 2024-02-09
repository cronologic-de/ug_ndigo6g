@echo off
setlocal enabledelayedexpansion

rem Set the directory path where XML files are located
set "directory_path=./build/doxygen/xml"

echo run replace_xsd_commands.bat

rem Loop through all XML files in the directory and its subdirectories
for /r "%directory_path%" %%f in (*.xml) do (
    echo replacements in %%f
    set "output_file=%%~dpnf_temp.xml"
    (
        rem Read each line of the XML file and replace <deg/> with &#176;
        for /f "tokens=*" %%a in (%%f) do (
            set "line=%%a"
            set "line=!line:<deg/>=&#176;!"
            set "line=!line:<nonbreakablespace/>=&#160;!"
            set "line=!line:<minus/>=&#8722;!"
            set "line=!line:<ldquo/>=&#8220;!"
            set "line=!line:<rdquo/>=&#8221;!"
            set "line=!line:<le/>=&#8804;!"
            set "line=!line:<ge/>=&#8805;!"
            echo !line!
        )
    ) > "!output_file!"

    rem Replace the original XML file with the modified one
    move /y "!output_file!" "%%f" >nul
)