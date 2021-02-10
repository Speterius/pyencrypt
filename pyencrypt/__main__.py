import easygui
from cryptography.fernet import InvalidToken
from custom_filesavebox import filesavebox
from encryption import init_fernet, file_to_bytes, bytes_to_file

# Title of the easygui:
title = "PyEncrypt"


def main():

    # Choose action:
    choice = easygui.buttonbox(msg="Choose action", title=title, choices=["Encrypt", "Decrypt"])

    def routine():

        # Initialize password defined key
        password_from_user = easygui.passwordbox(msg="Enter password for this session", title=title)

        if password_from_user is None:
            return

        fernet = init_fernet(password_from_user)

        # Get files:
        in_file = easygui.fileopenbox(msg=f"Choose file to {choice}.", title=title)

        if in_file is None:
            return

        in_data = file_to_bytes(in_file)

        try:
            if choice == "Encrypt":
                out_data = fernet.encrypt(in_data)
            elif choice == "Decrypt":
                out_data = fernet.decrypt(in_data)
            else:
                return
        except InvalidToken:
            choice_try = easygui.buttonbox(msg="Incorrect password", title=title, choices=["Try again", "Exit"])
            if choice_try == "Try again":
                return routine()
            else:
                return

        out_file = filesavebox(msg="Save result as:.", title=title)

        if out_file is None:
            return

        return out_data, out_file

    output = routine()

    if output is None:
        return

    data, file = output

    bytes_to_file(filepath=file, data=data)
    easygui.msgbox(msg=f"Result has been written to {file}")

    return 0


if __name__ == '__main__':
    main()
