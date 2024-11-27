from app.ui import main
from app.crypto import Crypto
from app.core import Word, word_distance, letters_distance
# main()

cripto = Crypto()

original = Word("AAAAAAAAAAA")
encrypt = Word("ABCDEBBCDEF")

ret = cripto.find_key(original, encrypt)
print(f"ret {ret}")