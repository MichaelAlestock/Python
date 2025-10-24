import sys
import os
from pathlib import Path
from glob import glob
from dotenv import load_dotenv


def ScriptRoot():
    return Path(__file__).resolve().parent


wildcard = f"{ScriptRoot()}\\*.env"
path_wildcard = glob(wildcard)


class SecretManager:
    @staticmethod
    def get_next_argv(prompt):
        argv_iter = iter(sys.argv[1:])
        try:
            return next(argv_iter)
        except StopIteration:
            return input(prompt)

    def HasMatch():
        if path_wildcard:
            return True
        else:
            return False

    def GetMatchedFile():
        for matched_file in path_wildcard:
            return matched_file

    def PrintMatch():
        print(SecretManager.HasMatch())

    def GetSecretInformation():
        load_dotenv(SecretManager.GetMatchedFile())
        ikey = os.getenv("IKEY")
        skey = os.getenv("SKEY")
        host = os.getenv("HOST")

        print(f"IKEY: [{ikey}]\nSKEY: [{skey}]\nHOST: [{host}]")

    def WriteSecret():
        # check file existence
        print("Checking if environment file exists...")
        if not SecretManager.HasMatch():
            print("No environment file found, create a new one.")
            file_path = SecretManager.get_next_argv(
                "Enter a name for your secrets file: "
            )
            new_file_path = Path.joinpath(ScriptRoot(), file_path)
            Path(f"{new_file_path}.env").touch()
        elif SecretManager.HasMatch():
            print(f"{SecretManager.GetMatchedFile()} was found.")

            confirm_choice = input("Check secrets now? [y/N] ")

            if confirm_choice == "Y" or confirm_choice == "y":
                print("Outputting your secrets.")
                SecretManager.GetSecretInformation()
                print("Exiting...")
                exit(0)
            elif confirm_choice == "N" or confirm_choice == "n" or confirm_choice == "":
                print("Exiting...")
                exit(0)

        ikey = SecretManager.get_next_argv("Enter your integration key: ")
        skey = SecretManager.get_next_argv("Enter your secret key: ")
        hostname = SecretManager.get_next_argv("Enter the hostname: ")

        print(f"Environment file successfully created in [{ScriptRoot()}].")

        with open(f"{new_file_path}.env", mode="w+t") as file:
            file.write(f"IKEY='{ikey}'\n" f"SKEY='{skey}'\n" f"HOST='{hostname}'")
            print(
                f"Environment variables successfully written to [{new_file_path}.env]"
            )
