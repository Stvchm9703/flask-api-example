# from .UAC import UserMod, roles_users, gps_users, UGroupMod, URoleMod
# SECTION: helper class

from sqlalchemy.inspection import inspect


class Serializer(object):
    def serialize(self):
        # check it when fail
        # print(str(inspect(self).attrs.keys()))
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]

# !SECTION
