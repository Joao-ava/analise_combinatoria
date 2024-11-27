from app.core import Word, letters_distance


class Crypto:
    @staticmethod
    def find_key(original: str, encrypt: str) -> list:
        diff = letters_distance(original, encrypt)
        pattern = []
        #find pattern in list
        for i in range(5,1,-1):
            print(f"i: {i}")
            # get first i items for diff
            find_pattern = diff[:i]
            print(f"find pattern {find_pattern}, diff: {diff[i:i*2]}")
            if find_pattern == diff[i:i*2]:
                pattern = find_pattern
                break
        return pattern

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
