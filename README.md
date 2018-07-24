# xls2xform-api

xls2xform-api is a lightweight Survey123 form conversion service based on [https://github.com/XLSForm/pyxform](https://github.com/XLSForm/pyxform).

## Downloading and prerequsites

Requires Python and Java installed.
Once installed, you need to download this repo and configure the prerequisits as follows:

1. Clone or download this repo
2. Run the following commands to configure the python prerequisits:
3. cd xls2xform-api
4. cd pyxform
5. python setup.py develop
6. cd ..
7. pip install -r requirements.txt

N.B. For macOS and Linux you may need to use `sudo` for steps 5 and 7.

## Starting the service

python xls2xform-api.py

## Consuming the service

Open Survey123 Connect
Use settings > Services
Change Survey123 REST API Url to: http://localhost:5123/api
