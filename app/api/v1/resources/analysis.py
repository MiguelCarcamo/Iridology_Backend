from flask_restful import Resource
from schemas import AnalysisX
from db import conn
import asyncio
from flask import request
import json
from decimal import Decimal
class fakefloat(float):
    def __init__(self, value):
        self._value = value
    def __repr__(self):
        return str(self._value)
def defaultencode(o):
    if isinstance(o, Decimal):
        # Subclass float with custom repr?
        return fakefloat(o)
    raise TypeError(repr(o) + " is not JSON serializable")

def analysis(id):
    try:
        table = []
        col = ['id','IDPatient','NamePatient','CreateDate','FinishDate','IDDoctor','Status','URLLeft', 'URLRight', 'StatusName', 'IDUser']
        _json = []
        textSQL = f"EXECUTE SP_Analysis_Read {id}"
        x = asyncio.run(conn.runServer(textSQL))
        for row in x:
            table.append(row)
        _json = [dict(zip(col, row)) for row in table]
    except:
        _json = False   
    return _json
def newanalysis():
    _return = None
    try:
        analysispatient_details = request.get_json()
        AnalysisX.IDPatient = analysispatient_details[0]['IDPatient']
        AnalysisX.IDDoctor = analysispatient_details[0]['IDDoctor']
        AnalysisX.URLLeft = analysispatient_details[0]['URLLeft']
        AnalysisX.URLRight = analysispatient_details[0]['URLRight']
        textSQL = f"EXECUTE SP_Analysis_Create {str(AnalysisX.IDPatient)}, '{AnalysisX.IDDoctor}','{AnalysisX.URLLeft}','{AnalysisX.URLRight}' "
        x = asyncio.run(conn.runServer2(textSQL))
        _return = True
    except:
        _return = False
    return _return
def updateanalysis():
    _return = None
    try:
        analysispatient_details = request.get_json()
        AnalysisX.IDAnalysis = analysispatient_details[0]['IDAnalysis']
        AnalysisX.Status = analysispatient_details[0]['Status']
        textSQL = f"EXECUTE SP_Analysis_Update {str(AnalysisX.IDAnalysis)}, {str(AnalysisX.Status)}  "
        x = asyncio.run(conn.runServer2(textSQL))
        _return = True
    except:
        _return = False
    return _return
class Analysis (Resource):
    def get(self, id):
        x = analysis(id)
        if x:
            return json.dumps(x, default=defaultencode)
        else:
            return dict(msj='Accion no fue Completada')
    def post(self, id):
        x = newanalysis()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
    def put(self, id):
        x = updateanalysis()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')            