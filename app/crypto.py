from app.core import EncryptWord, letters_distance


class Crypto:
    @staticmethod
    def find_key(original: str, encrypt: str) -> int:
        encrypt_text = EncryptWord(encrypt)
        original_text = EncryptWord(original)
        for i in range(1, 6):
            if (original_text + i) == encrypt_text:
                return i

        # diff = letters_distance(EncryptWord(original), EncryptWord(encrypt))
        # pattern = []
        # #find pattern in list
        # for i in range(5,1,-1):
        #     print(f"i: {i}")
        #     # get first i items for diff
        #     find_pattern = diff[:i]
        #     print(f"find pattern {find_pattern}, diff: {diff[i:i*2]}")
        #     if find_pattern == diff[i:i*2]:
        #         pattern = find_pattern
        #         break
        # return pattern

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
