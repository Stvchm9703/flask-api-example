__author__ = 'responsible'
from App import app
from flask_restful import Api
# from App.controller.UAC import Login, UserGroup, UserRole, UserRead, UserCreate
from App.controller.auditLog import \
    auditLog,\
    auditLogLookup,\
    vAlertLog,\
    vAlertLiveLog,\
    vEventLog,\
    unoLookup

# /api : api header
# /api/
#   lp : lookup table
#   v  : view table
#   r  : history record table 


api = Api(app, default_mediatype="application/json")

# # UAC group
# api.add_resource(Login, '/api/login')
# # api.add_resource(Protected, '/protected')
# api.add_resource(UserGroup, '/api/userGroup')
# api.add_resource(UserRole, '/api/userRole')
# api.add_resource(UserRead, '/api/user/search')
# api.add_resource(UserCreate, '/api/user/c')

# audit Log
api.add_resource(auditLog, '/api/r/log')
api.add_resource(auditLogLookup, '/api/lp/logconfig')
api.add_resource(vAlertLog, '/api/v/alert')
api.add_resource(vAlertLiveLog, '/api/v/live_alert')
api.add_resource(vEventLog, '/api/v/event')
api.add_resource(unoLookup, '/api/lp/uno_lookup')
