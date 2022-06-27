from flask_restful import Resource
from flask import request, send_from_directory
import os
from os import getcwd
from werkzeug.utils import secure_filename

PATH_FILES = getcwd() + '\\Files'
APP_ROOT = os.path.dirname(os.path.abspath(__file__)) + '\\Files'

class Files (Resource):
    def get(self, id):
        return send_from_directory(PATH_FILES, path=id, as_attachment=True)
    
    def post(self, id):
        try:
            x = request.files['File']
            x.save(os.path.join(PATH_FILES, secure_filename(x.filename)))
            return dict(msj='Accion Realizada Correctamente')
        except FileNotFoundError:
            return dict(msj='Folder not found')