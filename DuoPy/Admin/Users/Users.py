from Utilities.utilities import Utilities


class Users:
    def __init__(
        self,
        user_id,
        realname,
        username,
        email_address,
        status,
        created_on,
        last_directory_sync,
        last_login,
    ):
        self.user_id = user_id
        self.realname = realname
        self.username = username
        self.email_address = email_address
        self.status = status
        self.created_on = created_on
        self.last_directory_sync = last_directory_sync
        self.last_login = last_login

    @classmethod
    def build_object(cls, data: dict) -> "Users":
        """Dynamically build the Users class object."""
        return cls(
            user_id=data["user_id"],
            realname=data["realname"],
            username=data["username"],
            email_address=data["email"],
            status=data["status"],
            created_on=Utilities.convert_to_dt(data["created"]),
            last_directory_sync=Utilities.convert_to_dt(data["last_directory_sync"]),
            last_login=Utilities.convert_to_dt(data["last_login"]),
        )

    def __repr__(self):
        return f"Users(user_id='{self.user_id}',realname='{self.realname}',username='{self.username}',email_address='{self.email_address}',status='{self.status}',created_on='{self.created_on}',last_directory_sync='{self.last_directory_sync}',last_login='{self.last_login}')\n"

    def __str__(self):
        return f"UserId: {self.user_id}\nReal Name: {self.realname}\nUsername: {self.username}\nEmail Address: {self.email_address}\nStatus: {self.status}\nCreated On: {self.created_on}\nLast Directory Sync: {self.last_directory_sync}\nLast Login: {self.last_login}"
