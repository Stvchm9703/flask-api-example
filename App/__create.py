from App import db
from App.model.UAC import URoleMod, UGroupMod, UserMod, roles_users, gps_users

db.create_all()

# db.create_all()
# db.session.add(URoleMod("admin", "admin"))
# db.session.add(URoleMod("user", "user"))
# db.session.add(URoleMod("superuser", "Super user"))
# db.session.add(UGroupMod("AA", "AA_maintainer"))
# db.session.add(UGroupMod("CS", "Custom"))
# db.session.commit()
# # db.session.add(UserMod(
# #     "admin",
# #     "admin",
# #     "active",
# #     "admin@system.com",
# #     True,
# #     "Admin",
# #     "A",
# #     "first admin"
# # ))
# # db.session.add(UserMod(
# #     "user",
# #     "user",
# #     "active",
# #     "user@system.com",
# #     True,
# #     "User",
# #     "A",
# #     "first User"
# # ))
# # db.session.add(UserMod(
# #     "super",
# #     "super",
# #     "active",
# #     "super@system.com",
# #     True,
# #     "Super",
# #     "A",
# #     "first Super User"
# # ))

# db.session.commit()

# db.engine.execute(roles_users.insert(), user_id=1, role_id=1)
# db.engine.execute(roles_users.insert(), user_id=2, role_id=2)
# db.engine.execute(roles_users.insert(), user_id=3, role_id=3)

# db.engine.execute(gps_users.insert(), user_id=1, group_id=1)
# db.engine.execute(gps_users.insert(), user_id=2, group_id=2)
# db.engine.execute(gps_users.insert(), user_id=3, group_id=1)
# db.session.commit()

db.commit()
