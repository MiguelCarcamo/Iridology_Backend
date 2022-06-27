from marshmallow import fields


# SECCION QUE CONTIENE LA INFORMACION SOBRE LOS USUARIOS
class UserID():
    id = fields.Integer(dump_only=True)
    user = fields.String()
    password = fields.String()
    idtype_user = fields.Integer()
    status = fields.Bool()

class TupeUser():
    id = fields.Integer(dump_only=True)
    type_user = fields.String()

class InfoUser:
    id = fields.Integer(dump_only=True)
    id_user = fields.Nested('User')
    name = fields.String()
    last_name = fields.String()
    mail = fields.String()
    phone = fields.String()
    country = fields.String() 
    lenguage = fields.String()

# CONFIGURACIONES DEL SISTEMA 
class SetupSystemsX:
	IDSetupSystems = fields.Integer(dump_only=True)
	SetupSystems = fields.String()
	RangeMax = fields.Decimal()
	RangeMin =  fields.Decimal()
	Lenguage = fields.String()

class BodyOrgansX:
    IDSetupBodyOrgans = fields.Integer(dump_only=True)
    IDSetupSystems = fields.Nested('SetupSystemsX')
    BodyOrgans = fields.String()
    Left = fields.Bool()
    Right = fields.Bool()
    Men = fields.Bool()
    Womman = fields.Bool()
    RangeMax = fields.Decimal()
    RangeMin =  fields.Decimal()
    Lenguage = fields.String()

class SetupSymptomsX:
    IDSetupSymptoms = fields.Integer(dump_only=True)
    IDSetupBodyOrgans = fields.Nested('BodyOrgansX')
    Symptoms = fields.String()
    RangeMax = fields.Decimal()
    RangeMin =  fields.Decimal()    
    Lenguage = fields.String()

class SetupFindingsx:
    IDSetupFindings = fields.Integer(dump_only=True)
    IDSetupBodyOrgans = fields.Nested('BodyOrgansX')
    Foods = fields.String()
    NotFoods = fields.String()
    Findings = fields.String()
    RangeMax = fields.Decimal()
    RangeMin =  fields.Decimal()       
    Lenguage = fields.String()

# ANALISIS DE LOS PACIENTES
class AnalysisPatientX:
    IDPatient = fields.Integer(dump_only=True)
    IDUser = fields.Nested('UserID')
    PatientName = fields.String()
    PatientLastName = fields.String()
    Lenguage = fields.String()
    BirthDate = fields.Date()
    Gender = fields.String()

class AnalysisX:
    IDAnalysis = fields.Integer(dump_only=True)
    IDPatient = fields.Nested('AnalysisPatientX')
    FinishDate = fields.DateTime()
    IDDoctor = fields.Integer()
    Status = fields.Integer()
    URLLeft = fields.String()
    URLRight = fields.String()
