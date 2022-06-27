import pyodbc

class conn:
    _connX = None
    _query = None
    async def runServer(textSql):
        try:
            _connX = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-BU4SDQQ\SQLEXPRESS;' 'Database=IRIDOLOGY;' 'UID=sa;' 'PWD=1234')
            _query = _connX.cursor()
            _query.execute(textSql)
            x = _query.fetchall()
            return(x)
        except:
            _connX = False
        finally:
            _connX.close()

    async def runServer2(textSql):
        try:
            _connX = pyodbc.connect('Driver={SQL Server};' 'Server=DESKTOP-BU4SDQQ\SQLEXPRESS;' 'Database=IRIDOLOGY;' 'UID=sa;' 'PWD=1234')
            _query = _connX.cursor()
            _query.execute(textSql)
            x = _query.commit()
            return(x)
        except:
            _connX = False
        finally:
            _connX.close()
    