from App import db
from . import Serializer
from datetime import datetime

class auditLog(db.Model, Serializer):
    # table audit_log : table modal
    __tablename__ = 'audit_logs'
    #  log id
    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    # unit_id / uno_id
    uno_id = db.Column('uno_id', db.VARCHAR(length=45))
    # audit log lookup to code
    code_id = db.Column('code_id', db.VARCHAR(length=45))
    # loging time
    timestamp = db.Column('timestamp', db.TIMESTAMP(), nullable=False)
    # logging status
    status = db.Column('status', db.VARCHAR(length=45))
    # extra-info
    user_id = db.Column('user_id', db.VARCHAR(length=45))
    mission_id = db.Column('mission_id', db.VARCHAR(length=45))
    waypoint_id = db.Column('waypoint_id', db.String(255))

    # initrialization
    def __init__(self, uno_id, code_id,
                 status, audit_time, user_id,
                 mission_id, waypoint_id
                 ):
        self.uno_id = uno_id
        self.code_id = code_id
        self.status = status
        self.audit_time = audit_time
        self.user_id = user_id
        self.mission_id = mission_id
        self.waypoint_id = waypoint_id

    # serialize db object to json
    def serialize(self):
        d = Serializer.serialize(self)
        try:
            d['timestamp'] = d['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f')
        except BaseException:
            d['timestamp'] = str(d['timestamp'])
        return d


class auditLogLookup(db.Model, Serializer):
     # table audit_log_lookups : table modal
    __tablename__ = 'audit_log_lookups'
    # rec-id 
    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    # code-id
    code_id = db.Column('code_id', db.VARCHAR(length=45))
    # status code
    status = db.Column('status', db.VARCHAR(length=45))
    # status description
    description = db.Column('description', db.VARCHAR(length=45))
    # log type
    type = db.Column('type', db.VARCHAR(length=45))
    # severity level
    severity = db.Column('severity', db.VARCHAR(length=45))

    # initrialization
    def __init__(self, code_id, status, description, type, severity):
        self.code_id = code_id
        self.status = status
        self.description = description
        self.type = type
        self.severity = severity

    # serialize db object to json
    def serialize(self):
        d = Serializer.serialize(self)
        return d


class vAlertLog(db.Model, Serializer):
    #  view table alert-logs-v
    __tablename__ = 'alert_logs_v'
    # unit_name / uno_id
    uno_id = db.Column('uno_id', db.VARCHAR())
    # unit_name / uno_name
    uno_name = db.Column('uno_name', db.VARCHAR())
    # code_id 
    code_id = db.Column('code_id', db.VARCHAR())
    # loging time
    timestamp = db.Column('timestamp', db.TIMESTAMP(),primary_key=True)
    # status description
    display = db.Column('display', db.VARCHAR())
    # severity level
    severity = db.Column('severity', db.VARCHAR())

    # serialize db object to json
    def serialize(self):
        d = Serializer.serialize(self)
        try:
            d['timestamp'] = d['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f')
        except BaseException:
            d['timestamp'] = str(d['timestamp'])
        return d


class vAlertLiveLog(db.Model, Serializer):
    #  view table audit-logs-live-v
    __tablename__ = 'alert_logs_live_v'
    # unit_name / uno_id
    uno_id = db.Column('uno_id', db.VARCHAR(length=45))
    # unit_name / uno_name
    uno_name = db.Column('uno_name', db.VARCHAR(length=45))
    # code_id
    code_id = db.Column('code_id', db.VARCHAR(length=45))
    # status 
    status = db.Column('status', db.VARCHAR(length=45))
    # loging time
    timestamp = db.Column('timestamp', db.TIMESTAMP(), primary_key=True)
    # status description
    display = db.Column('display', db.VARCHAR(length=45))
    # severity level
    severity = db.Column('severity', db.VARCHAR(length=45))

    # serialize db object to json
    def serialize(self):
        d = Serializer.serialize(self)
        try:
            d['timestamp'] = d['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f')
        except BaseException:
            d['timestamp'] = str(d['timestamp'])
        return d


class vEventLog(db.Model, Serializer):
    # view table Event-logs-live-v 
    __tablename__ = 'event_logs_v'
    # unit_name / uno_id
    uno_id = db.Column('uno_id', db.VARCHAR(length=45))
    # unit_name / uno_name
    uno_name = db.Column('uno_name', db.VARCHAR(length=45))
    # code_id
    code_id = db.Column('code_id', db.VARCHAR(length=45))
    # loging time
    timestamp = db.Column('timestamp', db.TIMESTAMP(), primary_key=True)
    # status description
    display = db.Column('display', db.VARCHAR(length=45))
    # severity level
    severity = db.Column('severity', db.VARCHAR(length=45))

    # serialize db object to json
    def serialize(self):
        d = Serializer.serialize(self)
        try:
            d['timestamp'] = d['timestamp'].strftime('%Y-%m-%d %H:%M:%S.%f')
        except BaseException:
            d['timestamp'] = str(d['timestamp'])
        return d


class unoLookup(db.Model, Serializer):
    # view table Event-logs-live-v
    __tablename__ = 'uno_lookups'
    # rec_id 
    id = db.Column('id', db.Integer(), primary_key=True, autoincrement=True)
    # unit_name / uno_id
    uno_id = db.Column('uno_id', db.VARCHAR(length=45))
    # unit_name / uno_name
    uno_name = db.Column('description', db.VARCHAR(length=45))
   
    # serialize db object to json
    def serialize(self):
        d = Serializer.serialize(self)
        return d
