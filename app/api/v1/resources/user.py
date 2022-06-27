from cgitb import text
from flask_restful import Resource
from schemas import UserID, InfoUser
import asyncio
from db import conn
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
    def alluser():
        try:
            table = []
            col = ['IDUser','User','Password','Status','IDTypeUser','IDInfoUser','IDUser','UserName','UserLastName','UserMail','UserPhone','UserCountry','UserLenguage','IDTypeUser','TypeUser']
            _json = []
            textSQL = """ 
            SELECT [User].IDUser, [User].[User], [User].[Password], [User].[Status], [User].IDTypeUser, 
                [InfoUser].IDInfoUser, [InfoUser].IDUser, [InfoUser].UserName, [InfoUser].UserLastName, [InfoUser].UserMail, [InfoUser].UserPhone, [InfoUser].UserCountry, [InfoUser].UserLenguage, 
                [TypeUser].IDTypeUser, [TypeUser].TypeUser 
            FROM [User] 
            LEFT OUTER JOIN [InfoUser] ON [User].IDUser = [InfoUser].IDUser 
            LEFT OUTER JOIN [TypeUser] ON [USER].IDTypeUser = [TypeUser].IDTypeUser
            """
            x = asyncio.run(conn.runServer(textSQL))
            for row in x:
                table.append(row)
            _json = [dict(zip(col, row)) for row in table]
        except:
            _json = False   
        return _json
    def newuser():
        _return = None
        try:
           user_details = request.get_json()
           UserID.password = user_details[0]['Password']
           UserID.idtype_user = user_details[0]['TypeUser']
           InfoUser.name = user_details[0]['UserName']
           InfoUser.last_name = user_details[0]['UserLastName']
           InfoUser.mail = user_details[0]['UserMail']
           InfoUser.phone = user_details[0]['UserPhone']
           InfoUser.country = user_details[0]['UserCountry']
           InfoUser.lenguage = user_details[0]['UserLenguage']
           textSQL = f"EXECUTE SP_CreateUser '{UserID.password}', {str(UserID.idtype_user)}, '{InfoUser.name}', '{InfoUser.last_name}', '{InfoUser.mail}', '{InfoUser.phone}', '{InfoUser.country}', '{InfoUser.lenguage}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return

    def updateuser():
        _return = None
        try:
           user_details = request.get_json()
           UserID.id = user_details[0]['IDUser']
           UserID.status = user_details[0]['Status']
           UserID.password = user_details[0]['Password']
           UserID.idtype_user = user_details[0]['TypeUser']
           InfoUser.name = user_details[0]['UserName']
           InfoUser.last_name = user_details[0]['UserLastName']
           InfoUser.mail = user_details[0]['UserMail']
           InfoUser.phone = user_details[0]['UserPhone']
           InfoUser.country = user_details[0]['UserCountry']
           InfoUser.lenguage = user_details[0]['UserLenguage']
           textSQL = f"EXECUTE SP_UpdateUser {str(UserID.id)}, '{UserID.password}', {str(UserID.status)}, {str(UserID.idtype_user)}, '{InfoUser.name}', '{InfoUser.last_name}', '{InfoUser.mail}', '{InfoUser.phone}', '{InfoUser.country}', '{InfoUser.lenguage}' "
           x = asyncio.run(conn.runServer2(textSQL))
           _return = True
        except:
            _return = False
        return _return

class User (Resource):
    def get(self):
        x = alluser()
        if x:
            return json.dumps(x, default=defaultencode)
        else:
            return dict(msj='Accion no fue Completada')

    def post(self):
        x = newuser()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')
    
    def put(self):
        x = updateuser()
        if x:
            return dict(msj='Accion Realizada Correctamente')
        else:
            return dict(msj='Accion no fue Completada')