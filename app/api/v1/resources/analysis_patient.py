from flask_restful import Resource
from schemas import AnalysisPatientX
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

if True:
    def allanalysispatient(id):
        try:
            table = []
            col = ['id','IDUser','PatientName','PatientLastName','Lenguage','BirthDate','Gender']
            _json = []
            textSQL = f"EXECUTE SP_AnalysisPatientRead 0"
            x = asyncio.run(conn.runServer(textSQL))
            for row in x:
                table.append(row)
            _json = [dict(zip(col, row)) for row in table]
        except:
            _json = False   
        return _json

    def newanalysispatient():
        _return = None
        try:
           analysispatient_details = request.get_json()
        #    AnalysisPatientX.IDPatient = analysispatient_details[0]['IDPatient']
           AnalysisPatientX.IDUser = analysispatient_details[0]['IDUser']
           AnalysisPatientX.PatientName = analysispatient_details[0]['PatientName']
           AnalysisPatientX.PatientLastName = analysispatient_details[0]['PatientLastName']
           AnalysisPatientX.Lenguage = analysispatient_details[0]['Lenguage']
           AnalysisPatientX.BirthDate = analysispatient_details[0]['BirthDate']
           AnalysisPatientX.Gender = analysispatient_details[0]['Gender']
           textSQL = f"EXECUTE SP_AnalysisPatientCreate {str(AnalysisPatientX.IDUser)}, '{AnalysisPatientX.PatientName}','{AnalysisPatientX.PatientLastName}','{AnalysisPatientX.Lenguage}','{str(AnalysisPatientX.BirthDate)}','{AnalysisPatientX.Gender}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return
        
    def updateanalysispatient():
        _return = None
        try:
           analysispatient_details = request.get_json()
           AnalysisPatientX.IDPatient = analysispatient_details[0]['IDPatient']
        #    AnalysisPatientX.IDUser = analysispatient_details[0]['IDUser']
           AnalysisPatientX.PatientName = analysispatient_details[0]['PatientName']
           AnalysisPatientX.PatientLastName = analysispatient_details[0]['PatientLastName']
           AnalysisPatientX.Lenguage = analysispatient_details[0]['Lenguage']
           AnalysisPatientX.BirthDate = analysispatient_details[0]['BirthDate']
           AnalysisPatientX.Gender = analysispatient_details[0]['Gender']
           textSQL = f"EXECUTE SP_AnalysisPatientUpdate {str(AnalysisPatientX.IDPatient)}, '{AnalysisPatientX.PatientName}','{AnalysisPatientX.PatientLastName}','{AnalysisPatientX.Lenguage}','{str(AnalysisPatientX.BirthDate)}','{AnalysisPatientX.Gender}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return
        
class AnalysisPatient (Resource):
    def get(self):
        x = allanalysispatient(0)
        if x:
            return json.dumps(x, default=defaultencode)
        else:
            return dict(msj='Accion no fue Completada')
    
    def post(self):
        x = newanalysispatient()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
    
    def put(self):
        x = updateanalysispatient()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')