from app.api.v1.resources.user import User
from app.api.v1.resources.login import Login
from app.api.v1.resources.seting_systems import SetupSystems
from app.api.v1.resources.seting_bodyorgans import BodyOrgans
from app.api.v1.resources.seting_symptoms import SetupSymptoms
from app.api.v1.resources.seting_findings import SetupFindings
from app.api.v1.resources.analysis_patient import AnalysisPatient
from app.api.v1.resources.analysis import Analysis
from app.api.v1.resources.file_action import Files
from app.api.v1.resources.test import Test

from app.api import api

def register_ulrs():
    api.add_resource(User,'/user', endpoint='user')
    api.add_resource(Login,'/login', endpoint='login')
    api.add_resource(SetupSystems,'/systems', endpoint='systems')
    api.add_resource(BodyOrgans,'/bodyorgans', endpoint='bodyorgans')
    api.add_resource(SetupSymptoms,'/symptoms', endpoint='Symptoms')
    api.add_resource(SetupFindings,'/findings', endpoint='findings')
    api.add_resource(Analysis,'/analysis/<id>', endpoint='analysis')
    api.add_resource(AnalysisPatient,'/analysispatient', endpoint='analysispatient')
    api.add_resource(Files,'/Files/<id>', endpoint='Files')
    api.add_resource(Test,'/Test', endpoint='Test')