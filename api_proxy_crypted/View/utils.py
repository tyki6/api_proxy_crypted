from cryptography.fernet import Fernet


def encrypt(message: bytes, key: str) -> bytes:
    return Fernet(key.encode()).encrypt(message)


def decrypt(token: bytes, key: str) -> bytes:
    return Fernet(key.encode()).decrypt(token)
