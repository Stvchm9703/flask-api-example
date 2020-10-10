from App import app, db
from . import Serializer


class URoleMod(db.Model, Serializer):
    __tablename__ = 'user_role_desp'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(100), unique=True)
    description = db.Column('desp', db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def serialize(self):
        d = Serializer.serialize(self)
        del d['user_infos']
        return d


class UGroupMod(db.Model, Serializer):
    __tablename__ = 'user_group_desp'
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(100), unique=True)
    description = db.Column('desp', db.String(255))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def serialize(self):
        d = Serializer.serialize(self)
        del d['user_infos']
        return d


class UserMod(db.Model, UserMixin, Serializer):
    __tablename__ = 'user_infos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column('user_name', db.String(30),
                          nullable=False, unique=True)
    password = db.Column('password', db.String(128), nullable=False)
    user_status = db.Column('user_status', db.String(255), nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    email = db.Column('email', db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())

    first_name = db.Column(db.String(100), nullable=False, server_default='')
    last_name = db.Column(db.String(100), nullable=False, server_default='')

    user_desc = db.Column('user_desc', db.String(255), nullable=True)

    roles = db.relationship(
        'URoleMod',
        secondary=roles_users,
        backref=db.backref('user_infos', lazy='dynamic')
    )
    group = db.relationship(
        'UGroupMod',
        secondary=gps_users,
        backref=db.backref('user_infos', lazy='dynamic')
    )

    def __init__(
            self,
            username=None,
            password=None,
            status=None,
            email=None,
            active=True,
            first_name=None,
            last_name=None,
            user_desc=None
    ):

        self.user_name = username
        self.password = pwd_context.encrypt(password)
        self.user_status = status
        self.email = email
        self.active = active
        self.first_name = first_name
        self.last_name = last_name
        self.user_desc = user_desc
        pass

    def serialize(self):
        d = Serializer.serialize(self)
        print(d)
        d['group'] = [K.id for K in d['group']]
        d['roles'] = [K.id for K in d['roles']]
        del d['password']
        return d
