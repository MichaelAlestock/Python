from Utilities.secret_manager import SecretManager
from Admin.Users.Users import Users
from Utilities.utilities import Utilities

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

    def get_users():
        try:
            app = SecretManager.client_admin()
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

    def get_users_by_status(status):
        app = SecretManager.client_admin()
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

    # TODO: Refactor to include error-handling for empty list
    def get_user_by_username(username: str) -> Users | None:
        try:
            response = SecretManager.client_admin().get_users_by_name(username=username)

            if not response:
                raise IndexError("No users found in the response.")

            first_object = response[0]

            return Users.build_object(first_object)

        except IndexError:
            print(f"No user found with the specified username [{username}].")
            return None

    def get_user_by_phone_number(phone_number):
        app = SecretManager.client_admin()
        response = app.get_users_by_name(username=phone_number)

    # TODO: Is there a better way to do this? Seems like it could take a while to return
    def get_user_by_email_address(
        email_address="", email_address_list=[]
    ) -> Users | None:
        try:
            response_list = list()

            if len(email_address_list) > 0:
                for email in email_address_list:
                    email_response = SecretManager.client_admin().get_user_by_email(
                        email=email
                    )

                    if not email_response:
                        raise IndexError(f"No objects returned in response.")

                    inside_array = email_response[0]

                    response_list.append(Users.build_object(inside_array))
                return response_list
            else:
                response = SecretManager.client_admin().get_user_by_email(
                    email=email_address
                )

                if not response:
                    raise IndexError(
                        f"User with email address [{email_address}] was not found in directory."
                    )

                inside_array = response[0]

                return Users.build_object(inside_array)

        except IndexError:
            print(
                f"User with email address [{email_address}] was not found in directory."
            )
            return None

    def update_user_status(username: str, status):
        # Obtain user
        try:
            user_information = UserManager.get_user_by_username(username=username)

            current_user_status = user_information.status
            current_user_id = user_information.user_id

            if status not in UserManager.ALLOWED_STATUSES:
                raise Exception(f"[{status}] not an acceptable status.")

            if current_user_status != status:
                response = SecretManager.client_admin().update_user(
                    user_id=current_user_id, status=status
                )

                if not response:
                    raise IndexError("")

                print(f"{user_information.realname} has been successfully updated.")

        except RuntimeError:
            print(f"No user found with the user_id: [{user_information.user_id}]")

    def sync_user(username: str) -> None:
        # Grab dkey from secrets
        try:
            LOAD_ENV = SecretManager.load_secret_information()

            SecretManager.client_admin().sync_user(
                username=username,
                directory_key=LOAD_ENV.get("dkey"),
            )

            # Get user information so we can print that out to show the user was actually synced
            user_information = UserManager.get_user_by_username(username)
            user_last_directory_sync = user_information.last_directory_sync

            print(
                f"[{username}]successfully synced from external directory: {user_last_directory_sync}"
            )
        except RuntimeError:
            print(f"User [{username}] not found in directory.")

