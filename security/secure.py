# import bcrypt
# password = "super secret password"
# # Hash a password for the first time, with a randomly-generated salt

# st = bcrypt.gensalt()
# print st

# hashed = str(bcrypt.hashpw(password, st))
# print hashed
# # Check that an unhashed password matches one that has previously been
# # hashed
# if bcrypt.checkpw(password, hashed):
# 	print("It Matches!")
# else:
# 	print("It Does not Match :(")

# print "==============================================="

# # static_salt="#ANTS@!%"
# # password = "t@sahu"
# # salted_password = static_salt + password
# # hashed = bcrypt.hashpw(salted_password, dynamic_salt)
# # print "hash is : ", hashed

import hashlib

password = 'a@pinto'
h = hashlib.md5(password.encode())
print h.hexdigest()
print type(h.hexdigest())