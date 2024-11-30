from app.core import EncryptWord


class Crypto:
    @staticmethod
    def find_key(original: str, encrypt: str) -> int:
        return 0

    @staticmethod
    def encrypt(key: int, text: str) -> str:
        word = EncryptWord(text)
        encrypted_text = word + key
        return encrypted_text.value

    @staticmethod
    def decrypt(key: int, text: str) -> str:
        word = EncryptWord(text)
        decrypted_text = word - key
        return decrypted_text.value
