from flask_restful import Resource
from schemas import SetupFindingsx
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
    def allsetupfindings(id):
        try:
            table = []
            col = ['id','IDSetupBodyOrgans','BodyOrgans','Foods','NotFoods', 'Findings', 'RangeMax','RangeMin', 'Lenguage']
            _json = []
            textSQL = "EXECUTE SP_SetupFindingsRead 0"
            x = asyncio.run(conn.runServer(textSQL))
            for row in x:
                table.append(row)
            _json = [dict(zip(col, row)) for row in table]
        except:
            _json = False   
        return _json
    
    def newsetupfindings():
        _return = None
        try:
           setupfindings_details = request.get_json()
        #    SetupFindingsx.IDSetupFindings = setupfindings_details[0]['IDSetupFindings']
           SetupFindingsx.IDSetupBodyOrgans = setupfindings_details[0]['IDSetupBodyOrgans']
           SetupFindingsx.Foods = setupfindings_details[0]['Foods']
           SetupFindingsx.NotFoods = setupfindings_details[0]['NotFoods']
           SetupFindingsx.Findings = setupfindings_details[0]['Findings']
           SetupFindingsx.RangeMax = setupfindings_details[0]['RangeMax']
           SetupFindingsx.RangeMin = setupfindings_details[0]['RangeMin']
           SetupFindingsx.Lenguage = setupfindings_details[0]['Lenguage']
           textSQL = f"EXECUTE SP_SetupFindingsCreate {str(SetupFindingsx.IDSetupBodyOrgans)}, '{SetupFindingsx.Foods }', '{SetupFindingsx.NotFoods}', '{SetupFindingsx.Findings}', {str(SetupFindingsx.RangeMax)},{str(SetupFindingsx.RangeMin)},  '{SetupFindingsx.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return

    def updatesetupfindings():
        _return = None
        try:
           setupfindings_details = request.get_json()
           SetupFindingsx.IDSetupFindings = setupfindings_details[0]['IDSetupFindings']
           SetupFindingsx.IDSetupBodyOrgans = setupfindings_details[0]['IDSetupBodyOrgans']
           SetupFindingsx.Foods = setupfindings_details[0]['Foods']
           SetupFindingsx.NotFoods = setupfindings_details[0]['NotFoods']
           SetupFindingsx.Findings = setupfindings_details[0]['Findings']
           SetupFindingsx.RangeMax = setupfindings_details[0]['RangeMax']
           SetupFindingsx.RangeMin = setupfindings_details[0]['RangeMin']             
           SetupFindingsx.Lenguage = setupfindings_details[0]['Lenguage']
           textSQL = f"EXECUTE SP_SetupFindingsUpdate {str(SetupFindingsx.IDSetupFindings)}, {str(SetupFindingsx.IDSetupBodyOrgans)}, '{SetupFindingsx.Foods }', '{SetupFindingsx.NotFoods}', '{SetupFindingsx.Findings}', {str(SetupFindingsx.RangeMax)},{str(SetupFindingsx.RangeMin)}, '{SetupFindingsx.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return

class SetupFindings (Resource):
    def get(self):
        x = allsetupfindings(0)
        return json.dumps(x, default=defaultencode)
    
    def post(self):
        x = newsetupfindings()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
    
    def put(self):
        x = updatesetupfindings()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')