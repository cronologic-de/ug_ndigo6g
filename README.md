# ug_ndigo6g

User guide for the cronologic **Ndigo6G-12** digitizer.

This is a Sphinx project that creates the user guide for the
[Ndigo6G-12](https://www.cronologic.de/product/ndigo6g-12),
gigasample PCIe digitizer boards by
[cronologic GmbH & Co. KG](https://www.cronologic.de).

LuaLaTeX or XeLaTeX, Python, and doxygen are necessary for compilation.

## Setup and installation

Optionally, create and activate a virtual environment
```shell
python -m venv .venv
. .\.venv\Scripts\activate
```

Install the requirements of the project
```shell
pip install -r requirements.txt
```

After that, run
```shell
.\make.bat html
```
   or
```shell
.\make.bat latexpdf
```
to compile the project as HTML or PDF. The HTML (PDF) output is in `build/html/`
(`build/latex/`).

---

The `make.bat` script first runs `doxygen`, compiling XML output for
`source\crono_interface.h` and `source\ndigo6g12_interface.h`. Then, it uses
the output thereof to compile the sphinx HTML (or PDF) output. It also
runs `replace_xsd_commands.bat` to fix some missing unicode characters.

The script checks if a file `.\fetch_interface.bat` is present. If that is
the case, it calls `.\fetch_interface.bat` before running the `doxygen` output.
This way you can fetch the most recent interface files, if so desired.

To bypass this behavior, either remove the respective `call` in `make.bat`
or call the sphinx builder without using the script, e.g.,
```shell
sphinx-build -M html source build
```

## License
This documentation is licensed under the
[CC BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/) license.
You are free to copy and redistribute the material in any medium or format for
any purpose, even commercially unchanged if you give appropriate credit to
cronologic GmbH & Co. KG. A link to
[this repository](https://github.com/cronologic-de/ug_ndigo6g) or the
[product page](https://www.cronologic.de/product/ndigo6g-12)
is sufficient.  If you decide to contribute to this repository, you transfer
non-exclusive but unlimited rights to your edit to cronologic GmbH & Co. KG.
![Creative Commons by-nd 4.0](https://i.creativecommons.org/l/by-nd/4.0/88x31.png)

The file [extraplaceins.sty](extraplaceins.sty) is in the public domain.
