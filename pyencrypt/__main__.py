import base64
import easygui
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet, InvalidToken
from gui import filesavebox


# Function return typing alias
void = type(None)

# Title of the easygui:
title = "PyEncrypt"


def password_to_key(password: str) -> bytes:

    # todo: For better security, salt should be generated and stored on the device.
    salt = b'\x15\x02y\x1e\x9cqe\xe0\xe5e\xef^\xb9\xee(\xfb'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=1000000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key


def file_to_bytes(filepath: str) -> bytes:
    with open(filepath) as file:
        file_string = file.read()
    return file_string.encode()


def bytes_to_file(filepath: str, data: bytes) -> void:
    with open(filepath, 'wb') as file:
        file.write(data)


def init_fernet(password: str) -> Fernet:
    key = password_to_key(password)
    return Fernet(key)


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

        return out_data, filesavebox(msg="Save result as:.", title=title)

    data, out_file = routine()

    bytes_to_file(filepath=out_file, data=data)
    easygui.msgbox(msg=f"Result has been written to {out_file}")

    return 0


if __name__ == '__main__':
    main()
