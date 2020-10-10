# # SECTION import class

# import json
# # from flask import jsonify
# from flask_restful import Resource, reqparse
# from flask_security import auth_token_required, roles_required, login_user
# from sqlalchemy import or_
# from App.model.UAC import UserMod, UGroupMod, URoleMod
# from App import db 
# # auth, baseauth, tokenauth
# # !SECTION endl


# # SECTION: Internal func --- auth verify_password

# # @baseauth.verify_password
# # def Cverify_password(username_or_token, password):
# #     # first try to authenticate by token
# #     user = UserMod.verify_auth_token(username_or_token)
# #     if not user:
# #         # try to authenticate with username/password
# #         user = UserMod.query.filter_by(user_name=username_or_token).first()
# #         if not user or not user.verify_password(password):
# #             return False
# #     return True
# # !SECTION

# # SECTION: Internal func --- auth verify_token
# # #   define


# # @tokenauth.verify_token
# # def verify_token(token):
# #     user = UserMod.verify_auth_token(token)
# #     if not user:
# #         # try to authenticate with username/password
# #         user = UserMod.query.filter_by(user_name=token).first()
# #         if not user:
# #             return False
# #     return True
# # # !SECTION

# # SECTION  Login Resx class 
# class Login(Resource):
#     def post(self):
#         args = reqparse.RequestParser() \
#             .add_argument(
#                 'username', type=str,
#                 location='json', required=True,
#                 help="user cannot null") \
#             .add_argument(
#                 "password", type=str,
#                 location='json', required=True,
#                 help="password cannot null") \
#             .parse_args()
#         user = UserMod.authenticate(args['username'], args['password'])
#         if user:
#             login_user(user=user)

#             def adf(val):
#                 r = val
#                 del r['user_infos']
#                 return r

#             def ro(val):
#                 r = val
#                 del r['user_infos']
#                 return

#             ugroup = [adf(x) for x in UGroupMod.serialize_list(user.group)]
#             urole = [ro(x) for x in URoleMod.serialize_list(user.roles)]
#             return {
#                 "message": "login success",
#                 "token": user.get_auth_token(),
#                 "group": ugroup,
#                 "role": urole
#                 }, 200
#         else:
#             return {"message": "error,WrongPassword"}, 401

		
#         pass

#     @auth_token_required
#     def get(self):
#         return {"msg": "tokenOK"}, 200

# # !SECTION 


# # SECTION  UserGroup Resx class
# class UserGroup(Resource):
#     @auth_token_required
#     @roles_required('admin')
#     def post(self):
#         args = reqparse.RequestParser() \
#             .add_argument(
#                 'name', type=str,
#                 location='json', required=True,
#                 help="name cannot null") \
#             .add_argument(
#                 'desp', type=str,
#                 location='json', required=True,
#                 help="desp cannot null") \
#             .parse_args()
#         grp = UGroupMod.query.filter(UGroupMod.name == args['name']).first()
#         if(grp):
#             return {
#                 "message": "create error"
#             }, 403
#         else:
#             try:
#                 db.session.add(UGroupMod(args['name'], args['desp']))
#                 db.session.commit()
#             except:
#                 return {
#                     "message": "error occur"
#                 }, 500
#         return {
#             "message": "create success"
#         }, 205
#         pass

#     @auth_token_required
#     def get(self):
#         query = UGroupMod.query.all()
#         return UGroupMod.serialize_list(query), 200
#         pass
# # !SECTION 


# # SECTION  UserRole Resx class
# class UserRole(Resource):
#     @auth_token_required
#     @roles_required('admin')
#     def post(self):
#         args = reqparse.RequestParser() \
#             .add_argument(
#                 'name', type=str,
#                 location='json', required=True,
#                 help="name cannot null") \
#             .add_argument(
#                 'desp', type=str,
#                 location='json', required=True,
#                 help="desp cannot null") \
#             .parse_args()
#         grp = URoleMod.query.filter(URoleMod.name == args['name']).first()
#         if(grp):
#             return {
#                 "message": "create error"
#             }, 403
#         else:
#             try:
#                 db.session.add(URoleMod(args['name'], args['desp']))
#                 db.session.commit()
#             except:
#                 return {
#                     "message": "error occur"
#                 }, 500
#         return {
#             "message": "create success"
#         }, 205
#         pass

#     @auth_token_required
#     def get(self):
#         query = URoleMod.query.all()
#         return URoleMod.serialize_list(query), 200
#         pass
# # !SECTION 


# # SECTION  UserSearch list Resx class
# # {
# #     'keyword' : "any",
# #     'status' : "<status enum>",
# #     'role' : "<role code>",
# #     'group' : "<group code>"
# # }

# class UserRead(Resource):
#     @auth_token_required
#     def post(self):
#         args = reqparse.RequestParser().parse_args()
#         grp = UserMod.query.filter(
#                 or_(
#                     UserMod.id.like(str(args['user_id'])),
#                     UserMod.name.like('%' + str(args['keyword']) + '%'),
#                     UserMod.user_status.like(str(args['status'])),
#                     UserMod.email.like('%' + str(args['keyword']) + '%'),
#                     UserMod.first_name.like('%' + str(args['keyword']) + '%'),
#                     UserMod.last_name.like('%' + str(args['keyword']) + '%'),
#                     UserMod.user_desc.like('%' + str(args['keyword']) + '%'),
#                     UserMod.roles.like(str(args['role'])),
#                     UserMod.group.like(str(args['group']))
#                 )
#             ).all()
#         return UserMod.serialize_list(grp), 200

#     @auth_token_required
#     def get(self):
#         query = UserMod.query.all()
#         return UserMod.serialize_list(query), 200
#         pass
# # !SECTION 


# # SECTION User Creat Resx class
# class UserCreate(Resource):
#     @auth_token_required
#     @roles_required('admin')
#     def post(self):
#         args = reqparse.RequestParser() \
#             .add_argument(
#                 'username', type=str,
#                 location='json', required=True,
#                 help="user name cannot null") \
#             .add_argument(
#                 'userdesp', type=str,
#                 location='json', required=False,
#                 help="") \
#             .add_argument(
#                 'password', type=str,
#                 location='json', required=True,
#                 help="password cannot null") \
#             .add_argument(
#                 'firstName', type=str,
#                 location='json', required=False,
#                 help="first name cannot null") \
#             .add_argument(
#                 'lastName', type=str,
#                 location='json', required=False,
#                 help="last name cannot null") \
#             .add_argument(
#                 'email', type=str,
#                 location='json', required=True,
#                 help="email cannot null") \
#             .parse_args()
#         user = UserMod.query.filter(UserMod.name == args['username']).first()
#         if(user):
#             return {
#                 "message": "create error, user exist"
#             }, 403
#         else:
#             try:
#                 db.session.add(
#                     URoleMod(
#                         args['username'],
#                         args['password'],
#                         'not_active',
#                         args['email'],
#                         args['firstName'],
#                         args['lastName'],
#                         args['userdesp']
#                         )
#                     )
#                 db.session.commit()
#             except:
#                 return {
#                     "message": "error occur"
#                 }, 500
#         return {
#             "message": "create success"
#         }, 205
#         pass
# # !SECTION 


# # SECTION User Edit Resx class

# # !SECTION 
