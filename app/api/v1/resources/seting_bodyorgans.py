from cgitb import text
from itertools import tee
from flask_restful import Resource
from schemas import BodyOrgansX
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
    def allsetupbodyorgans(id):
        try:
            table = []
            col = ['id','IDSetupSystems','SetupSystems','BodyOrgans','Left','Right','Men','Womman','RangeMax','RangeMin','Lenguage']
            _json = []
            x = asyncio.run(conn.runServer("EXECUTE SP_SetupBodyOrgansRead 0"))
            for row in x:
                table.append(row)
            _json = [dict(zip(col, row)) for row in table]
        except:
            _json = False  
        return _json
        
    def newsetupbodyorgans():
        _return = None
        try:
           setupbodyorgans_details = request.get_json()
        #    BodyOrgansX.IDSetupBodyOrgans = setupbodyorgans_details[0]['IDSetupBodyOrgans']
           BodyOrgansX.IDSetupSystems = setupbodyorgans_details[0]['IDSetupSystems']
           BodyOrgansX.BodyOrgans = setupbodyorgans_details[0]['BodyOrgans']
           BodyOrgansX.Left = setupbodyorgans_details[0]['Left']
           BodyOrgansX.Right = setupbodyorgans_details[0]['Right']
           BodyOrgansX.Men = setupbodyorgans_details[0]['Men']
           BodyOrgansX.Womman = setupbodyorgans_details[0]['Womman']
           BodyOrgansX.RangeMax = setupbodyorgans_details[0]['RangeMax']
           BodyOrgansX.RangeMin = setupbodyorgans_details[0]['RangeMin']
           BodyOrgansX.Lenguage = setupbodyorgans_details[0]['Lenguage']
           textSql = f"EXECUTE SP_SetupBodyOrgansCreate {str(BodyOrgansX.IDSetupSystems)}, '{BodyOrgansX.BodyOrgans }', {str(BodyOrgansX.Left)}, {str(BodyOrgansX.Right)}, {str(BodyOrgansX.Men)}, {str(BodyOrgansX.Womman)}, {str(BodyOrgansX.RangeMax)}, {str(BodyOrgansX.RangeMin)}, '{BodyOrgansX.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSql))
           _return = True
        except:
            _return = False
        return _return
        
    def updatesetupbodyorgans():
        _return = None
        try:
           setupbodyorgans_details = request.get_json()
           BodyOrgansX.IDSetupBodyOrgans = setupbodyorgans_details[0]['IDSetupBodyOrgans']
           BodyOrgansX.IDSetupSystems = setupbodyorgans_details[0]['IDSetupSystems']
           BodyOrgansX.BodyOrgans = setupbodyorgans_details[0]['BodyOrgans']
           BodyOrgansX.Left = setupbodyorgans_details[0]['Left']
           BodyOrgansX.Right = setupbodyorgans_details[0]['Right']
           BodyOrgansX.Men = setupbodyorgans_details[0]['Men']
           BodyOrgansX.Womman = setupbodyorgans_details[0]['Womman']
           BodyOrgansX.RangeMax = setupbodyorgans_details[0]['RangeMax']
           BodyOrgansX.RangeMin = setupbodyorgans_details[0]['RangeMin']           
           BodyOrgansX.Lenguage = setupbodyorgans_details[0]['Lenguage']
           textSql = f"EXECUTE SP_SetupBodyOrgansUpdate {str(BodyOrgansX.IDSetupBodyOrgans)}, {str(BodyOrgansX.IDSetupSystems)}, '{BodyOrgansX.BodyOrgans }', {str(BodyOrgansX.Left)}, {str(BodyOrgansX.Right)}, {str(BodyOrgansX.Men)}, {str(BodyOrgansX.Womman)}, {str(BodyOrgansX.RangeMax)}, {str(BodyOrgansX.RangeMin)}, '{BodyOrgansX.Lenguage}' "
           x = asyncio.run(conn.runServer2(textSql))
           _return = True
        except:
            _return = False
        return _return

class BodyOrgans (Resource):
    def get(self):
        x = allsetupbodyorgans(0)
        if x:
            return json.dumps(x, default=defaultencode)
        else:
            return dict(msj='Accion no fue Completada')
    
    def post(self):
        x = newsetupbodyorgans()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
    
    def put(self):
        x = updatesetupbodyorgans()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')