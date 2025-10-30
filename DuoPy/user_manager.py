import duo_client
from secret_manager import SecretManager
from Users import Users
from datetime import datetime

"""
# TODO: Flesh out UserManager class
# TODO: IndexException error when returning dictionary
# TODO: Create function to convert timestamp datetimes to UTC datetimes
"""


class UserManager:

    @staticmethod
    def client_admin():
        load_env = SecretManager.load_secret_information()

        ikey = load_env.get("ikey")
        skey = load_env.get("skey")
        host = load_env.get("host")

        if not all([ikey, skey, host]):
            raise ValueError("Missing required credentials.")

        return duo_client.Admin(
            ikey=ikey,
            skey=skey,
            host=host,
            sig_timezone="UTC",
            # TODO: Fix 401 error | caused by invalid credentials.. need them to test
        )

    def convert_to_dt(date_item):
        if type(date_item) is type(None):
            return "No Date Info Found"
        else:
            return datetime.fromtimestamp(date_item).strftime("%m/%d/%Y @ %I:%M %p")

    def get_users():
        app = UserManager.client_admin()
        response = app.get_users()

        user_list = []
        for user in response:
            user_list.append(
                Users(
                    realname=user["realname"],
                    username=user["username"],
                    email_address=user["email"],
                    status=user["status"],
                    created_on=UserManager.convert_to_dt(user["created"]),
                    last_directory_sync=UserManager.convert_to_dt(
                        user["last_directory_sync"]
                    ),
                    last_login=UserManager.convert_to_dt(user["last_login"]),
                )
            )
        return user_list

    def get_user_by_username():
        return True

    def get_user_by_phone_number():
        return True

    def get_user_by_email_address():
        return True

    def get_user_information(self):
        UserManager.client_admin().get_users_by_name(self.username)

    def print_connected():
        load_env = SecretManager.load_secret_information()
        ikey = load_env.get("host")
        print(ikey)
