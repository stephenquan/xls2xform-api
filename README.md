# xls2xform-api

xls2xform-api is a lightweight Survey123 form conversion service based on [https://github.com/XLSForm/pyxform](https://github.com/XLSForm/pyxform).

## Downloading and prerequisites

Requires Python and Java installed.
Add Python and Java to your PATH so that (python, java commands are recognized from the command prompt)

1. Install Python 3.7.0 https://www.python.org/
   - Windows
     - Add Python to your PATH (could be %LOCALAPPDATA%\Programs\Python\Python37-32)
     - Add Python scripts to your PATH (could be %LOCALAPPDATA%\Programs\Python\Python37-32\Scripts)
     - Test by opening a terminal window and run: python --version (check to see if you get a response)
     - Also test PIP: pip --version (check to see if you get a response)
   - macOS
     - Check Python is installed by opening a terminal window: python --version
     - Download and install PIP:
       - wget https://bootstrap.pypa.io/get-pip.py
       - sudo python get-pip.py
2. Install Oracle Java Platform JDK https://www.oracle.com/technetwork/java/javase/downloads/index.html
   - Windows
     - Open a terminal window and run: Java --version (check to see if you get a response)
3. Clone or download this repo
4. Open a Command Prompt / Terminal / Bash window and run the following commands to configure the python prerequisites:
5. cd xls2xform-api
6. cd pyxform
7. python setup.py develop # macOS and Linux requires sudo
8. cd ..
9. python -m pip install -r requirements.txt # macOS and Linux requires sudo
10. cd ..

## Starting the service

1. cd xls2xform-api
2. python xls2xform-api.py

## Consuming the service

1. Open Survey123 Connect
2. Use settings > Services
3. Change Survey123 REST API Url to: http://localhost:5123/api
4. When Publishing your form, "Create web form" is not currently supported, so, you must disable it in the Publish Survey > Options

