# from App import app, db
# # from App.util import Serializer
# from flask_security import UserMixin, RoleMixin
# from passlib.apps import custom_app_context as pwd_context 
# from itsdangerous import (
#     TimedJSONWebSignatureSerializer as TJSONSign,
#     BadSignature,
#     SignatureExpired)
# from . import Serializer

# roles_users = \
#     db.Table(
#         'user_roles',
#         db.Column(
#             'user_id',
#             db.Integer(),
#             db.ForeignKey('user_infos.id')),
#         db.Column(
#             'role_id',
#             db.Integer(),
#             db.ForeignKey('user_role_desp.id'))
#         )

# gps_users = \
#     db.Table(
#         'user_groups',
#         db.Column(
#             'user_id',
#             db.Integer(),
#             db.ForeignKey('user_infos.id')
#         ),
#         db.Column(
#             'group_id',
#             db.Integer(),
#             db.ForeignKey('user_group_desp.id')
#         ),
#     )


# class URoleMod(db.Model, RoleMixin, Serializer):
#     __tablename__ = 'user_role_desp'
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     name = db.Column('name', db.String(100), unique=True)
#     description = db.Column('desp', db.String(255))

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

#     def serialize(self):
#         d = Serializer.serialize(self)
#         del d['user_infos']
#         return d


# class UGroupMod(db.Model, Serializer):
#     __tablename__ = 'user_group_desp'
#     id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
#     name = db.Column('name', db.String(100), unique=True)
#     description = db.Column('desp', db.String(255))

#     def __init__(self, name, description):
#         self.name = name
#         self.description = description

#     def serialize(self):
#         d = Serializer.serialize(self)
#         del d['user_infos']
#         return d


# class UserMod(db.Model, UserMixin, Serializer):
#     __tablename__ = 'user_infos'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_name = db.Column('user_name', db.String(30), nullable=False, unique=True)
#     password = db.Column('password', db.String(128), nullable=False)
#     user_status = db.Column('user_status', db.String(255), nullable=True)
#     active = db.Column(db.Boolean(), default=True, nullable=False)    
#     email = db.Column('email', db.String(255), nullable=False, unique=True)
#     email_confirmed_at = db.Column(db.DateTime())
    
#     first_name = db.Column(db.String(100), nullable=False, server_default='')
#     last_name = db.Column(db.String(100), nullable=False, server_default='')

#     user_desc = db.Column('user_desc', db.String(255), nullable=True)

#     roles = db.relationship(
#         'URoleMod',
#         secondary=roles_users,
#         backref=db.backref('user_infos', lazy='dynamic')
#     )
#     group = db.relationship(
#         'UGroupMod',
#         secondary=gps_users,
#         backref=db.backref('user_infos', lazy='dynamic')
#     )

#     def __init__(
#             self,
#             username=None,
#             password=None,
#             status=None,
#             email=None,
#             active=True,
#             first_name=None,
#             last_name=None,
#             user_desc=None
#             ):

#         self.user_name = username
#         self.password = pwd_context.encrypt(password)
#         self.user_status = status
#         self.email = email
#         self.active = active
#         self.first_name = first_name
#         self.last_name = last_name
#         self.user_desc = user_desc
#         pass
        
#     def serialize(self):
#         d = Serializer.serialize(self)
#         print(d)
#         d['group'] = [K.id for K in d['group']]
#         d['roles'] = [K.id for K in d['roles']]
#         del d['password']
#         return d
    
#     @staticmethod
#     def authenticate(username, password):
#         user = UserMod.query.filter(UserMod.user_name == username).one()
#         if user and pwd_context.verify(password, user.password):  
#             return user

#     def verify_password(self, password):
#         return pwd_context.verify(password, self.password)
        
#     #  SECTION : token chapter
#     def generate_auth_token(self, expiration=3600):
#         s = TJSONSign(app.config['SECRET_KEY'], expires_in=expiration)
#         return s.dumps({'id': self.id, 'username': self.user_name})

#     @staticmethod
#     def verify_auth_token(token):
#         s = TJSONSign(app.config['SECRET_KEY'])
#         try:
#             data = s.loads(token)
#         except SignatureExpired:
#             return None    # valid token, but expired
#         except BadSignature:
#             return None    # invalid token
#         user = UserMod.query.get(data['id'])
#         return user
#     #  !SECTION  !endl

