import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet


# Function return typing alias
void = type(None)


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


def encrypt(password: str, in_file: str, out_file: str) -> void:
    fernet = init_fernet(password)
    in_data = file_to_bytes(in_file)
    out_data = fernet.encrypt(in_data)
    bytes_to_file(out_file, out_data)


def decrypt(password: str, in_file: str, out_file: str) -> void:
    fernet = init_fernet(password)
    in_data = file_to_bytes(in_file)
    out_data = fernet.decrypt(in_data)
    bytes_to_file(out_file, out_data)
