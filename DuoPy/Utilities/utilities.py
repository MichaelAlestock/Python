# other imports
from pathlib import Path
from datetime import datetime


class Utilities:

    def script_root():
        return Path(__file__).resolve().parent

    def convert_to_dt(date_item):
        if type(date_item) is type(None):
            return "No Date Info Found"
        else:
            return datetime.fromtimestamp(date_item).strftime("%m/%d/%Y @ %I:%M %p")
