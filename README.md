# xls2xform-api

xls2xform-api is a lightweight Survey123 form conversion service based on [https://github.com/XLSForm/pyxform](https://github.com/XLSForm/pyxform).

## Downloading and prerequsites

Requires Python and Java installed.
Once installed, you need to download this repo and configure the prerequisits as follows:

1. Clone or download this repo
2. Open a Command Prompt / Terminal / Bash window and run the following commands to configure the python prerequisites:
3. cd xls2xform-api
4. cd pyxform
5. python setup.py develop
6. cd ..
7. pip install -r requirements.txt
8. cd ..

N.B. For macOS and Linux you may need to use `sudo` for steps 5 and 7.

## Starting the service

1. cd xls2xform-api
2. python xls2xform-api.py

## Consuming the service

1. Open Survey123 Connect
2. Use settings > Services
3. Change Survey123 REST API Url to: http://localhost:5123/api
