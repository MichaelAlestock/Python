import duo_client
from Utilities.secret_manager import SecretManager
from Admin.Users.Users import Users
from Utilities.utilities import Utilities
import logging

"""
# TODO: Flesh out UserManager class
# TODO: IndexException error when returning dictionary
# TODO: Create function to convert timestamp datetimes to UTC datetimes
"""


class UserManager:
    ALLOWED_STATUSES = [
        "active",
        "bypass",
        "locked out",
        "disabled",
        "pending deletion",
    ]

    # internal function to create and return a Duo Admin client object
    # used to by all other functions to make API calls
    # TODO: Implement a unit test to test credentials work
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
        )

    def get_users():
        try:
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
                        created_on=Utilities.convert_to_dt(user["created"]),
                        last_directory_sync=Utilities.convert_to_dt(
                            user["last_directory_sync"]
                        ),
                        last_login=Utilities.convert_to_dt(user["last_login"]),
                    )
                )
            return user_list
        except Exception as generic_error:
            generic_error.add_note("No results returned.")
            raise

    # TODO: Refactor to include error-handling for empty list
    def get_user_by_username(username):
        app = UserManager.client_admin()
        response = app.get_users_by_name(username=username)

        user_list = []
        for user in response:
            user_list.append(
                Users(
                    realname=user["realname"],
                    username=user["username"],
                    email_address=user["email"],
                    status=user["status"],
                    created_on=Utilities.convert_to_dt(user["created"]),
                    last_directory_sync=Utilities.convert_to_dt(
                        user["last_directory_sync"]
                    ),
                    last_login=Utilities.convert_to_dt(user["last_login"]),
                )
            )
        # TODO: Refactor to include error-handling in case this has more than 1 index
        return user_list[0]

    def get_user_by_phone_number(phone_number):
        app = UserManager.client_admin()
        response = app.get_users_by_name(username=phone_number)

        user_list = []
        for user in response:
            user_list.append(
                Users(
                    realname=user["realname"],
                    username=user["username"],
                    email_address=user["email"],
                    status=user["status"],
                    created_on=Utilities.convert_to_dt(user["created"]),
                    last_directory_sync=Utilities.convert_to_dt(
                        user["last_directory_sync"]
                    ),
                    last_login=Utilities.convert_to_dt(user["last_login"]),
                )
            )
        # TODO: Refactor to include error-handling in case this has more than 1 index
        return user_list[0]

    # TODO: Is there a better way to do this? Seems like it could take a while to return
    def get_user_by_email_address(email_address):
        app = UserManager.client_admin()
        response = app.get_users()

        user_list = []

        # iterate over list and find the user who has the specified email
        try:
            for user in response:
                if user["email"] == email_address:
                    user_list.append(
                        Users(
                            realname=user["realname"],
                            username=user["username"],
                            email_address=user["email"],
                            status=user["status"],
                            created_on=Utilities.convert_to_dt(user["created"]),
                            last_directory_sync=Utilities.convert_to_dt(
                                user["last_directory_sync"]
                            ),
                            last_login=Utilities.convert_to_dt(user["last_login"]),
                        )
                    )
                    return user_list[0]
                else:
                    return []
            # TODO: Refactor to include error-handling in case this has more than 1 index
        except IndexError as ierror:
            ierror.add_note(f"No user found with the email address [{email_address}].")

    def get_users_by_status(status):
        app = UserManager.client_admin()
        response = app.get_users()

        user_list = []
        for user in response:
            # TODO: Error-handling for invalid status
            if status in UserManager.ALLOWED_STATUSES and user["status"] == status:
                user_list.append(
                    Users(
                        realname=user["realname"],
                        username=user["username"],
                        email_address=user["email"],
                        status=user["status"],
                        created_on=Utilities.convert_to_dt(user["created"]),
                        last_directory_sync=Utilities.convert_to_dt(
                            user["last_directory_sync"]
                        ),
                        last_login=Utilities.convert_to_dt(user["last_login"]),
                    )
                )
        # TODO: Refactor to include error-handling in case this has more than 1 index
        return user_list
