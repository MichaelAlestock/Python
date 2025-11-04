from Utilities.utilities import Utilities


class Phones:
    def __init__(
        self,
        user_realname,
        user_email,
        activated,
        creation_date,
        extension,
        last_activated_date,
        last_seen,
        model,
        name,
        number,
        platform,
        last_directory_sync,
    ):
        self.user_realname = user_realname
        self.user_email = user_email
        self.activated = activated
        self.creation_date = creation_date
        self.extension = extension
        self.last_activated_date = last_activated_date
        self.last_seen = last_seen
        self.model = model
        self.name = name
        self.number = number
        self.platform = platform
        self.last_directory_sync = last_directory_sync

    @classmethod
    def build_phone_object(cls, data: dict) -> "Phones":
        """Dynamically build a phone object."""
        return cls(
            user_realname=data["user_realname"],
            user_email=data["user_email"],
            activated=data["activated"],
            creation_date=Utilities.convert_to_dt(data["creation_date"]),
            extension=data["extension"],
            last_activated_date=Utilities.convert_to_dt(data["last_activated_date"]),
            last_seen=Utilities.convert_to_dt(data["last seen"]),
            model=data["model"],
            name=data["name"],
            number=data["number"],
            platform=data["platform"],
            last_directory_sync=Utilities.convert_to_dt(data["last_directory_sync"]),
        )

    def __str__(self):
        return f"User Name: {self.user_realname}\nUser Email: {self.user_email}\nActivated: {self.activated}\nCreated On: {self.creation_date}\nExtenstion: {self.extension}\nLast Activated: {self.last_activated_date}\nLast Seen: {self.last_seen}\nPhone Model: {self.model}\nPhone Name: {self.name}\nPhone Number: {self.number}\nPhone Platform: {self.platform}\nLast Directory Sync: {self.last_directory_sync}"

    def __repr__(self):
        return f"Phones(user_realname={self.user_realname},user_email={self.user_email},activated={self.activated},creation_date={self.creation_date},extension={self.extension},last_activated_date={self.last_activated_date},last_seen={self.last_seen},model={self.model},name={self.name},number={self.number},platform={self.platform},last_directory_sync={self.last_directory_sync})"
