from flask_restful import Resource
from schemas import SetupSystemsX
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
    def allsetupsystems(id):
        try:
            table = []
            col = ['id','SetupSystems','RangeMax','RangeMin','Lenguage']
            _json = []
            x = asyncio.run(conn.runServer("EXECUTE SP_SetupSystemsRead 0"))
            for row in x:
                table.append(row)
            _json = [dict(zip(col, row)) for row in table]
        except:
            _json = False   
        return _json

    def newsetupsystems():
        _return = None
        try:
           setupsystems_details = request.get_json()
           SetupSystemsX.SetupSystems = setupsystems_details[0]['SetupSystems']
           SetupSystemsX.RangeMax = setupsystems_details[0]['RangeMax']
           SetupSystemsX.RangeMin = setupsystems_details[0]['RangeMin']
           SetupSystemsX.Lenguage = setupsystems_details[0]['Lenguage']
           textSQl = f"EXECUTE SP_SetupSystemsCreate '{SetupSystemsX.SetupSystems }', {str(SetupSystemsX.RangeMax)},{str(SetupSystemsX.RangeMin)},'{SetupSystemsX.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSQl))
           _return = True
        except:
            _return = False
        return _return
        
    def updatesetupsystems():
        _return = None
        try:
           setupsystems_details = request.get_json()
           SetupSystemsX.IDSetupSystems = setupsystems_details[0]['IDSetupSystems']
           SetupSystemsX.SetupSystems = setupsystems_details[0]['SetupSystems']
           SetupSystemsX.RangeMax = setupsystems_details[0]['RangeMax']
           SetupSystemsX.RangeMin = setupsystems_details[0]['RangeMin']
           SetupSystemsX.Lenguage = setupsystems_details[0]['Lenguage']
           textSQl = f"EXECUTE SP_SetupSystemsUpdate {SetupSystemsX.IDSetupSystems}, '{SetupSystemsX.SetupSystems }', {str(SetupSystemsX.RangeMax)},{str(SetupSystemsX.RangeMin)},'{SetupSystemsX.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSQl))
           _return = True
        except:
            _return = False
        return _return

class SetupSystems (Resource):
    def get(self):
        x = allsetupsystems(0)
        return json.dumps(x, default=defaultencode)
    
    def post(self):
        x = newsetupsystems()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
    
    def put(self):
        x = updatesetupsystems()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')