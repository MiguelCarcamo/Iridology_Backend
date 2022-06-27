from itertools import count
from flask_restful import Resource
from schemas import UserID
from db import conn
import asyncio
from flask import request

if True:
    def Iduser():
        try:
            user_details = request.get_json()
            UserID.user = user_details[0]['User']
            UserID.password = user_details[0]['Password']
            table = []
            col = ['IDUser','User','Password','Status','IDTypeUser','IDInfoUser','IDUser','UserName','UserLastName','UserMail','UserPhone','UserCountry','UserLenguage','IDTypeUser','TypeUser']
            _json = []
            textSQL = f""" 
            SELECT [User].IDUser, [User].[User], [User].[Password], [User].[Status], [User].IDTypeUser, 
                [InfoUser].IDInfoUser, [InfoUser].IDUser, [InfoUser].UserName, [InfoUser].UserLastName, [InfoUser].UserMail, [InfoUser].UserPhone, [InfoUser].UserCountry, [InfoUser].UserLenguage, 
                [TypeUser].IDTypeUser, [TypeUser].TypeUser 
            FROM [User] 
            LEFT OUTER JOIN [InfoUser] ON [User].IDUser = [InfoUser].IDUser 
            LEFT OUTER JOIN [TypeUser] ON [USER].IDTypeUser = [TypeUser].IDTypeUser
            WHERE [User] = '{UserID.user}' AND [Password] = '{UserID.password}'
            """
            x = asyncio.run(conn.runServer(textSQL))
            for row in x:
                table.append(row)
            if len(table) == 0:
                _json = False
            else:
                _json = [dict(zip(col, row)) for row in table]
        except:
            _json = False   
        return _json

class Login (Resource):
    def post(self):
        x = Iduser()
        if x == False:
            return dict(msj='Usuario no encontrado')
        else:
            return x