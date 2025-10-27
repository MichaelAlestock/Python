from secret_manager import secret_manager

env_match = secret_manager.get_matched_file

if not env_match:
    secret_manager.write_secret_information()
else:
    print("It's working baby!")
    secret_manager.print_match()
    secret_manager.print_secret_information()
