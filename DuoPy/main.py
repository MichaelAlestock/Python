from Utilities.secret_manager import SecretManager
from Admin.Users.user_manager import UserManager

# UserManager.sync_user("mmedeiros")
# UserManager.update_user_status("malestock", "active")
# print(UserManager.get_user_by_email_address(email_address="alestockm@gnmhc.org"))
users = UserManager.get_users_by_status("bypass")

for user in users:
    print(f"{user}\n")
