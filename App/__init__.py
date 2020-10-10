# __author__ = 'responsible'
from .routes import api
import os
import json

import socket

from flask import Flask, render_template, jsonify
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth, MultiAuth
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security
from App import config

# SECTION init
rt_conf = {}
DATA_SQL_Addr = ''
SQL_Address = ''
ipAddress = ''

# init ip
host_name = socket.gethostname()
host_ip = socket.gethostbyname(host_name)
ipAddress = host_ip
def_port = 8201

root_dir = (os.path.abspath(os.path.dirname(__file__)))
static_dir = os.path.join(root_dir, 'static')
template_dir = os.path.join(root_dir, 'template')

# NOTE: load from config.json
with open(os.path.join(root_dir, 'config.json')) as json_data:
	rt_conf = json.load(json_data)
	if rt_conf['APIService']['mode'] is not None and rt_conf['APIService']['mode'] == 'dev':
		sql = rt_conf['APIService']['devSQL']
	elif rt_conf['APIService']['mode'] is not None and rt_conf['APIService']['mode'] == 'prod':
		sql = rt_conf['APIService']['SQL']
	else:
		sql = rt_conf['APIService']['SQL']
	if sql is not None:
		SQL_Address = 'mysql+pymysql://' \
			+ str(sql['user']) + ':' \
			+ str(sql['password']) + '@' \
			+ str(sql['host']) + ':' \
			+ str(sql['port']) + '/' \
			+ str(sql['database'])
	print(SQL_Address)

	if rt_conf['APIService']['ServerConfig']['port'] is not None:
		def_port = rt_conf['APIService']['ServerConfig']['port']

config.SQLALCHEMY_DATABASE_URI = SQL_Address

app = Flask(
	__name__,
	template_folder=template_dir,
	static_folder=static_dir,
	static_url_path=''
)
app.config.from_object(config)
db = SQLAlchemy(app)
cors = CORS(app,
			resources={
				r"/api/*": {"origins": "*"},
			},)

# from .model.UAC import UserMod, URoleMod, UGroupMod, roles_users, gps_users

# Flask-Security
# user_datastore = SQLAlchemyUserDatastore(db, UserMod, URoleMod)
# security = Security().init_app(app, user_datastore, register_blueprint=False)

baseauth = HTTPBasicAuth()
tokenauth = HTTPTokenAuth(scheme='Bearer')
auth = MultiAuth(baseauth, tokenauth)


@app.route('/')
def index():
	return render_template('index.html')


d = rt_conf.copy()
if d['APIService'] is not None:
	if d['APIService']['SQL']:
		del d['APIService']['SQL']

	if str(d['APIService']['ServerConfig']['host']) == '0.0.0.0' or \
			str(d['APIService']['ServerConfig']['host']) == '127.0.0.1' or\
			str(d['APIService']['ServerConfig']['host']) == 'host':
		d['APIService']['ServerConfig']['host'] = str(ipAddress)

	if 'QRCodeRW' in d and d['QRCodeRW'] is not None:
		del d['QRCodeRW']


@app.route('/config.json', methods=['GET'])
def cf_json():
	return jsonify(d)
