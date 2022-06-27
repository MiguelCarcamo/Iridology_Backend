from flask_restful import Resource
from schemas import SetupSymptomsX
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
    def allsetupsymptoms(id):
        try:
            table = []
            col = ['id','IDSetupBodyOrgans','BodyOrgans','Symptoms','RangeMax','RangeMin','Lenguage']
            _json = []
            textSQL = f"EXECUTE SP_SetupSymptomsRead 0"
            x = asyncio.run(conn.runServer(textSQL))
            for row in x:
                table.append(row)
            _json = [dict(zip(col, row)) for row in table]
        except:
            _json = False   
        return _json

    def newsetupsymptoms():
        _return = None
        try:
           setupsymptoms_details = request.get_json()
        #    SetupSymptomsX.IDSetupSymptoms = setupsymptoms_details[0]['IDSetupSymptoms']
           SetupSymptomsX.IDSetupBodyOrgans = setupsymptoms_details[0]['IDSetupBodyOrgans']
           SetupSymptomsX.Symptoms = setupsymptoms_details[0]['Symptoms']
           SetupSymptomsX.RangeMax = setupsymptoms_details[0]['RangeMax']
           SetupSymptomsX.RangeMin = setupsymptoms_details[0]['RangeMin']
           SetupSymptomsX.Lenguage = setupsymptoms_details[0]['Lenguage']
           textSQL = f"EXECUTE SP_SetupSymptomsCreate {str(SetupSymptomsX.IDSetupBodyOrgans)},'{SetupSymptomsX.Symptoms}', {str(SetupSymptomsX.RangeMax)},{str(SetupSymptomsX.RangeMin)}, '{SetupSymptomsX.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return
    
    def udatesetupsymptoms():
        _return = None
        try:
           setupsymptoms_details = request.get_json()
           SetupSymptomsX.IDSetupSymptoms = setupsymptoms_details[0]['IDSetupSymptoms']
           SetupSymptomsX.IDSetupBodyOrgans = setupsymptoms_details[0]['IDSetupBodyOrgans']
           SetupSymptomsX.Symptoms = setupsymptoms_details[0]['Symptoms']
           SetupSymptomsX.RangeMax = setupsymptoms_details[0]['RangeMax']
           SetupSymptomsX.RangeMin = setupsymptoms_details[0]['RangeMin']           
           SetupSymptomsX.Lenguage = setupsymptoms_details[0]['Lenguage']
           textSQL = f"EXECUTE SP_SetupSymptomsUpdate {str(SetupSymptomsX.IDSetupSymptoms)}, {str(SetupSymptomsX.IDSetupBodyOrgans)},'{SetupSymptomsX.Symptoms}', {str(SetupSymptomsX.RangeMax)},{str(SetupSymptomsX.RangeMin)}, '{SetupSymptomsX.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return

class SetupSymptoms (Resource):
    def get(self):
        x = allsetupsymptoms(0)
        return json.dumps(x, default=defaultencode)
    
    def post(self):
        x = newsetupsymptoms()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
    
    def put(self):
        x = udatesetupsymptoms()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
