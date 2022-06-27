from flask_restful import Resource
from flask import request
import os
from os import getcwd
from werkzeug.utils import secure_filename

PATH_FILES = getcwd() + '\\File'
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + '\\File'
class Test (Resource):
    def get(self):

        return dict(saludo=PATH_FILES)
    
    def post(self):
        x = request.files['File']
        x.save(os.path.join(APP_ROOT, secure_filename(x.filename)))
        return (getcwd())
    
    def put(self):
        pass