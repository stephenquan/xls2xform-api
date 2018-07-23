# xls2xform-api

xls2xform-api is a lightweight Survey123 form conversion service based on [https://github.com/XLSForm/pyxform](https://github.com/XLSForm/pyxform).

## Downloading and prerequsites

Requires Python and Java installed.
Once installed, you need to download this repo and configure the prerequisits as follows:

```bash
git clone https://github.com/stephenquan/xls2xform-api.git
cd xls2xform-api/pyxform
python setup.py develop
cd ..
pip install -r requirements.txt
```

## Starting the service

python xls2xform-api.py

## Consuming the service

Open Survey123 Connect
Use settings > Services
Change Survey123 REST API Url to: http://localhost:5123/api
