from app.core import Word


class Crypto:
    @staticmethod
    def find_key(original: str, encrypt: str) -> int:
        return 0

    @staticmethod
    def encrypt(key: int, text: str) -> str:
        encrypted_text = ""
        for char in text:
            word_char = Word(char)
            encrypted_char = word_char + key
            encrypted_text += encrypted_char.value
        return encrypted_text

    @staticmethod
    def decrypt(key: int, text: str) -> str:
        decrypted_text = ""
        for char in text:
            word_char = Word(char)
            decrypted_char = word_char - key
            decrypted_text += decrypted_char.value
        return decrypted_text
