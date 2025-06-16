#!/usr/bin/python3

from user_try import Admin

admin_user = Admin("Joe", "Gleason")
admin_user.describe_user()
admin_user.privileges.show_privileges()
