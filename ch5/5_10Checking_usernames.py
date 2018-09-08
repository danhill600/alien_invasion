current_users = ["dink", "dale", "sharpmouth", "sloan", "Croad"]
new_users = ["shoat", "Dale", "Stunk", "Croad", "Baby"]
current_users_lower = []

for current_user in current_users:
    current_users_lower.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
         print("sorry chief but the name " + new_user +" is already taken.")
    else:
         print("okay the name " + new_user + " is fine.")

#Not sure I did this in the tightest way, I should check the answer.


