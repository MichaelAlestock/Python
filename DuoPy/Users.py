class Users:
    def __init__(
        self,
        realname,
        username,
        email_address,
        status,
        created_on,
        last_directory_sync,
        last_login,
    ):
        self.realname = realname
        self.username = username
        self.email_address = email_address
        self.status = status
        self.created_on = created_on
        self.last_directory_sync = last_directory_sync
        self.last_login = last_login

    def __repr__(self):
        return f"Users(realname='{self.realname}',username='{self.username}',email_address='{self.email_address}',status='{self.status}',created_on='{self.created_on}',last_directory_sync='{self.last_directory_sync}',last_login='{self.last_login}')\n"

    def __str__(self):
        return f"Real Name: {self.realname}\nUsername: {self.username}\nEmail Address: {self.email_address}\nStatus: {self.status}\nCreated On: {self.created_on}\nLast Directory Sync: {self.last_directory_sync}\nLast Login: {self.last_login}"
