from user_module import User, Privileges, Admin

superuser = Admin("Dan", "Hill", "derbs@funeral.dirge", "nb-individual", "ABC")
superuser.adprivs.show_privileges()
