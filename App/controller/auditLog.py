# SECTION import class

import json
from datetime import datetime
# from flask import jsonify
from flask_restful import Resource, reqparse
from sqlalchemy import  func
from App.model.auditLog import \
	auditLog as auditLogM,\
	auditLogLookup as auditLogLookupM, \
	vAlertLog as vAlertLogM,\
	vAlertLiveLog as vAlertLiveLogM,\
	vEventLog as vEventLogM, \
	unoLookup as unoLookupM

from App import db
# auth, baseauth, tokenauth
# !SECTION endl


# SECTION  auditLog Resx class
class auditLog(Resource):
	def get(self):
		args = reqparse.RequestParser() \
			.add_argument(
				'id', type=str,
				location='args', required=False) \
			.add_argument(
				'uno_id', type=str,
				location='args', required=False) \
			.add_argument(
				'code_id', type=str,
				location='args', required=False) \
			.add_argument(
				'status', type=str,
				location='args', required=False) \
			.add_argument(
				'user_id', type=str,
				location='args', required=False) \
			.add_argument(
				'mission_id', type=str,
				location='args', required=False) \
			.add_argument(
				'waypoint_id', type=str,
				location='args', required=False) \
			.add_argument(
				'start_time', type=str,
				location='args', required=False) \
			.add_argument(
				'end_time', type=str,
				location='args', required=False) \
			.add_argument(
				'pageNum', type=str,
				location='args', required=False) \
			.add_argument(
				'pageSize', type=str,
				location='args', required=False) \
			.add_argument(
				'order', type=str,
				location='args', required=False) \
			.parse_args()

		condition = []
		if (args['id'] is not None):
			condition.append(
				auditLogM.id.like('%' + args['id'] + '%'))
		if (args['uno_id'] is not None):
			condition.append(
				auditLogM.uno_id.like('%' + args['uno_id'] + '%'))
		if (args['code_id'] is not None):
			condition.append(
				auditLogM.code_id.like('%' + args['code_id'] + '%'))
		if (args['status'] is not None):
			condition.append(
				auditLogM.status.like('%' + args['status'] + '%'))
		if (args['user_id'] is not None):
			condition.append(
				auditLogM.user_id.like('%' + args['user_id'] + '%'))
		if (args['mission_id'] is not None):
			condition.append(
				auditLogM.mission_id.like('%'+args['mission_id'] + '%'))
		if (args['waypoint_id'] is not None):
			condition.append(
				auditLogM.waypoint_id.like('%' + args['waypoint_id'] + '%'))

		if (args['start_time'] is not None and args['end_time'] is not None):
			start_time = args['start_time']
			end_time = args['end_time']
			condition.append(
				db.between(auditLogM.timestamp, start_time, end_time))
		elif (args['start_time'] is not None and args['end_time'] is None):
			start_time = args['start_time']
			end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
			condition.append(
				db.between(auditLogM.timestamp, start_time, end_time))
		elif (args['start_time'] is None and args['end_time'] is not None):
			end_time = args['end_time']
			condition.append(end_time >= auditLogM.timestamp )
		
		pageNum = 1
		pageSize = 20
		if (args['pageNum'] is not None):
			pageNum = args['pageNum']
		if (args['pageSize'] is not None):
			pageSize = args['pageSize']
			
		ordering = {}
		if (args['order'] is not None):
			if (args['order'] == 'desc'):
				ordering = auditLogM.timestamp.desc()
			elif (args['order'] == 'asc'):
				ordering = auditLogM.timestamp.asc()
			else:
				ordering = auditLogM.timestamp.desc()
		else:
			ordering = auditLogM.timestamp.desc()

		grp = auditLogM.query\
			.filter(db.and_(*condition))\
			.order_by(ordering)\
			.limit(pageSize).offset(str((int(pageNum)-1)*int(pageSize)))\
			.all()
		count = db.session\
			.query(func.count(auditLogM.id))\
			.filter(*condition).first()[0]
		return {
			"result": auditLogM.serialize_list(grp),
			"pageNum": int(pageNum),
			"pageSize": int(pageSize),
			"count": int(count),
			"last_update": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
			}, 200
		pass

# !SECTION


# SECTION  auditLogLookup Resx class
class auditLogLookup(Resource):
	def get(self):
		grp = auditLogLookupM.query.all()
		return {
			"result": auditLogLookupM.serialize_list(grp)
			}, 200
		pass

# !SECTION


# SECTION  auditLogLookup Resx class
class vAlertLog(Resource):
	def get(self):
		args = reqparse.RequestParser() \
			.add_argument(
				'uno_id', type=str,
				location='args', required=False) \
			.add_argument(
				'uno_name', type=str,
				location='args', required=False) \
			.add_argument(
				'code_id', type=str,
				location='args', required=False) \
			.add_argument(
				'start_time', type=str,
				location='args', required=False) \
			.add_argument(
				'end_time', type=str,
				location='args', required=False) \
			.add_argument(
				'pageNum', type=str,
				location='args', required=False) \
			.add_argument(
				'pageSize', type=str,
				location='args', required=False) \
			.add_argument(
				'order', type=str,
				location='args', required=False) \
			.parse_args()

		condition = []
		if (args['uno_id'] is not None):
			condition.append(
				vAlertLogM.uno_id.like('%' + args['uno_id'] + '%')
				)
		if (args['uno_name'] is not None):
			condition.append(
				vAlertLogM.uno_name.like('%' + args['uno_name'] + '%')
				)

		if (args['code_id'] is not None):
			condition.append(
				vAlertLogM.code_id.like('%' + args['code_id'] + '%')
				)

		if (args['start_time'] is not None and args['end_time'] is not None):
			start_time = args['start_time']
			end_time = args['end_time']
			condition.append(
				db.between(vAlertLogM.timestamp, start_time, end_time))
		elif (args['start_time'] is not None and args['end_time'] is None):
			start_time = args['start_time']
			end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
			condition.append(
				db.between(vAlertLogM.timestamp, start_time, end_time))
		elif (args['start_time'] is None and args['end_time'] is not None):
			end_time = args['end_time']
			condition.append(end_time>= vAlertLogM.timestamp)

		pageNum = 1
		pageSize = 20
		if (args['pageNum'] is not None):
			pageNum = args['pageNum']
		if (args['pageSize'] is not None):
			pageSize = args['pageSize']

		ordering = {}
		if (args['order'] is not None):
			if (args['order'] == 'desc'):
				ordering = vAlertLogM.timestamp.desc()
			elif (args['order'] == 'asc'):
				ordering = vAlertLogM.timestamp.asc()
			else:
				ordering = vAlertLogM.timestamp.desc()
		else:
			ordering = vAlertLogM.timestamp.desc()

		grp = vAlertLogM.query\
			.filter(db.and_(*condition))\
			.order_by(ordering)\
			.limit(pageSize).offset(str((int(pageNum)-1)*int(pageSize)))\
			.all()
		count = db.session\
			.query(func.count(vAlertLogM.timestamp))\
			.filter(*condition).first()[0]
		return {
			"result": vAlertLogM.serialize_list(grp),
			"pageNum": int(pageNum),
			"pageSize": int(pageSize),
			"count": int(count),
			"last_update": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		}, 200

# !SECTION


# SECTION  auditLogLookup Resx class
class vAlertLiveLog(Resource):
	def get(self):
		grp = vAlertLiveLogM.query\
			.order_by(vAlertLiveLogM.timestamp.desc())\
			.all()

		return {
			"result": vAlertLiveLogM.serialize_list(grp),
			"last_update": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
			}, 200
		pass

# !SECTION


# SECTION  auditLogLookup Resx class
class vEventLog(Resource):
	def get(self):
		args = reqparse.RequestParser() \
			.add_argument(
				'uno_id', type=str,
				location='args', required=False) \
			.add_argument(
				'uno_name', type=str,
				location='args', required=False) \
			.add_argument(
				'code_id', type=str,
				location='args', required=False) \
			.add_argument(
				'start_time', type=str,
				location='args', required=False) \
			.add_argument(
				'end_time', type=str,
				location='args', required=False) \
			.add_argument(
				'pageNum', type=str,
				location='args', required=False) \
			.add_argument(
				'pageSize', type=str,
				location='args', required=False) \
			.add_argument(
				'order', type=str,
				location='args', required=False) \
			.parse_args()
			
		condition = []
		if (args['uno_id'] is not None):
			condition.append(
				vEventLogM.uno_id.like('%' + args['uno_id'] + '%')
			)
		if (args['uno_name'] is not None):
			condition.append(
				vEventLogM.uno_name.like('%' + args['uno_name'] + '%')
			)

		if (args['code_id'] is not None):
			condition.append(
				vEventLogM.code_id.like('%' + args['code_id'] + '%')
			)

		if (args['start_time'] is not None and args['end_time'] is not None):
			start_time = args['start_time']
			end_time = args['end_time']
			condition.append(
				db.between(vEventLogM.timestamp, start_time, end_time))
		elif (args['start_time'] is not None and args['end_time'] is None):
			start_time = args['start_time']
			end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
			condition.append(
				db.between(vEventLogM.timestamp, start_time, end_time))
		elif (args['start_time'] is None and args['end_time'] is not None):
			end_time = args['end_time']
			condition.append(end_time >= vEventLogM.timestamp )

		pageNum = 1
		pageSize = 20
		if (args['pageNum'] is not None):
			pageNum = args['pageNum']
		if (args['pageSize'] is not None):
			pageSize = args['pageSize']

		ordering = {}
		if (args['order'] is not None):
			if (args['order'] == 'desc'):
				ordering = vEventLogM.timestamp.desc()
			elif (args['order'] == 'asc'):
				ordering = vEventLogM.timestamp.asc()
			else:
				ordering = vEventLogM.timestamp.desc()
		else:
			ordering = vEventLogM.timestamp.desc()

		grp = vEventLogM.query\
			.filter(db.and_(*condition))\
			.order_by(ordering)\
			.limit(pageSize).offset(str((int(pageNum)-1)*int(pageSize)))\
			.all()

		count = db.session\
			.query(func.count(vEventLogM.timestamp))\
			.filter(*condition).first()[0]

		return {
			"result": vEventLogM.serialize_list(grp),
			"pageNum": int(pageNum),
			"pageSize": int(pageSize),
			"count": int(count),
			"last_update": datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		}, 200
	

# !SECTION


class unoLookup(Resource):
	def get(self):
		grp = unoLookupM.query\
			.all()

		return {
			"result": unoLookupM.serialize_list(grp)
		}, 200
		pass
