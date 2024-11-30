alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num_to_char = {key:letter for key, letter in enumerate(alphabet)}
char_to_num = {letter:key for key, letter in enumerate(alphabet)}


class Word:
    """
    Classe para palavra para que possa ser usado para fazer incremetos e decrementos
    Exemplo de incremento
    Word('A') + 3 # Word('D')
    Word('Z') + 3 # Word('AC')

    Exemplo de decremento
    Word('D') - 3 # Word('A')
    Word('BA') - 2 # Word('AX')
    Word('AA') - 1 # Word('Z')
    """
    def __init__(self, value: str) -> None:
        self.value = value

    def __add__(self, other):        
        if other > 1:
            word = Word(self.value)
            for _ in range(other):
                word += 1
            return word
        
        last_letter = self.value[-1]
        if last_letter != 'Z':
            index = char_to_num[last_letter]
            next_char = num_to_char[index + 1]
            return Word(self.value[0:-1] + next_char)
        
        # Query
        if len(self.value) == 1:
            return Word('AA')
        
        next_query = Word(self.value[0:-1]) + 1
        return Word(next_query.value + 'A')

    def __sub__(self, other):        
        if other > 1:
            word = Word(self.value)
            for _ in range(other):
                word -= 1
            return word
        
        last_letter = self.value[-1]
        if last_letter != 'A':
            index = char_to_num[last_letter]
            prev_char = num_to_char[index - 1]
            return Word(self.value[0:-1] + prev_char)
        
        # Query
        if len(self.value) == 1:
            return Word('')
        
        next_query = Word(self.value[0:-1]) - 1
        return Word(next_query.value + 'Z')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Word):
            return self == Word(other)

        return self.value == other.value
    
    def __repr__(self) -> str:
        return f'<Word: {self}>'

    def __str__(self) -> str:
        return self.value
    

class EncryptWord(Word):
    def __add__(self, other):
        new_value = ''
        for letter in self.value:
            try:
                index = alphabet.index(letter)
                next_item = index + other
                new_value += alphabet[next_item % len(alphabet)]
            except ValueError:
                new_value += letter
        
        return EncryptWord(new_value)

    def __sub__(self, other):
        new_value = ''
        for letter in self.value:
            try:
                index = alphabet.index(letter)
                next_item = index - other
                new_value += alphabet[next_item % len(alphabet)]
            except ValueError:
                new_value += letter
        
        return EncryptWord(new_value)


def word_distance(first: Word, second: Word):
    """
    Função para calcular a diferença entre duas palavras por
    exemplo AAA para AAD vai ter uma diferença de 3 incrementos
    """
    count = 0
    while first != second:
        count += 1
        first += 1

    return count

