import sys
import os
from pathlib import Path
from glob import glob
from dotenv import load_dotenv

# my libs
from Utilities.utilities import utilities


class secret_manager:
    @staticmethod
    def get_next_argv(prompt):
        argv_iter = iter(sys.argv[1:])
        try:
            return next(argv_iter)
        except StopIteration:
            return input(prompt)

    @staticmethod
    def get_matched_files():
        wildcard = f"{utilities.script_root()}\\*.env"
        return glob(wildcard)

    @staticmethod
    def get_matched_file():
        matches = secret_manager.get_matched_files()
        return matches[0] if matches else False

    def print_match():
        print(secret_manager.get_matched_file())

    def load_secret_information():
        load_dotenv(secret_manager.get_matched_file())

        secret_dict = {
            "ikey": os.getenv("IKEY", ""),
            "skey": os.getenv("SKEY", ""),
            "host": os.getenv("HOST", ""),
        }

        return secret_dict

    def print_secret_information():
        load_env = secret_manager.load_secret_information()
        print(
            f"IKEY: [{load_env['ikey']}]\nSKEY: [{load_env['skey']}]\nHOST: [{load_env['host']}]"
        )

    def write_secret_information():
        # check file existence
        print("Checking if environment file exists...")
        if not secret_manager.get_matched_file():
            print("No environment file found, create a new one.")
            file_path = secret_manager.get_next_argv(
                "Enter a name for your secrets file: "
            )
            new_file_path = Path.joinpath(utilities.script_root(), file_path)
            Path(f"{new_file_path}.env").touch()
        elif secret_manager.GetMatchedFile():
            print(f"{secret_manager.GetMatchedFile()} was found.")

            confirm_choice = input("Check secrets now? [y/N] ")

            if confirm_choice == "Y" or confirm_choice == "y":
                print("Outputting your secrets.")
                secret_manager.print_secret_information()
                print("Exiting...")
                exit(0)
            elif confirm_choice == "N" or confirm_choice == "n" or confirm_choice == "":
                print("Exiting...")
                exit(0)

        ikey = secret_manager.get_next_argv("Enter your integration key: ")
        skey = secret_manager.get_next_argv("Enter your secret key: ")
        hostname = secret_manager.get_next_argv("Enter the hostname: ")

        print(f"Environment file successfully created in [{utilities.script_root()}].")

        with open(f"{new_file_path}.env", mode="w+t") as file:
            file.write(f"IKEY='{ikey}'\n" f"SKEY='{skey}'\n" f"HOST='{hostname}'")
            print(
                f"Environment variables successfully written to [{new_file_path}.env]"
            )
