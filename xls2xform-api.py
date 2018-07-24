import sys, subprocess, json, tempfile, shutil, os, traceback
from flask import Flask, request
from flask_restful import reqparse, Resource, Api

def pythonic_path(path):
    return path if os.path.sep == '/' else path.replace(os.path.sep, '/')

class Xls2XForm(Resource):
    def post(self):
        temp_dir = tempfile.mkdtemp()
        try:
            file = request.files['xlsform']
            temp_xlsx = os.path.join(temp_dir, file.filename)
            temp_xml = os.path.join(temp_dir, file.filename + '.xml')
            file.save(temp_xlsx)
            print('Converting', temp_xlsx)
            out = subprocess.check_output( [
                'python',
                'pyxform/pyxform/xls2xform.py',
                '--json',
                pythonic_path(temp_xlsx),
                pythonic_path(temp_xml)
            ] )
            result = json.loads(out)
            print(result)
            if os.path.exists(temp_xml):
                with open(temp_xml, 'r') as xml:
                    result['xform'] = xml.read()
            shutil.rmtree(temp_dir)
            return result
        except Exception as e:
            shutil.rmtree(temp_dir)
            print(str(e))
            return { 'code': 999, 'message': traceback.format_exc() }

app = Flask(__name__)
api = Api(app)
api.add_resource(Xls2XForm, '/api/xls2xform')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5123, debug=True)

