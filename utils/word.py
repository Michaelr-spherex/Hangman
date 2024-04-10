def load_words(filename: str) -> str:
    """
    Load words from file.
    """
    with open(filename, 'r') as file:
        words = file.read().splitlines()
    return words

def index_word(word: str) -> dict[str:list[int]]:
    """
    Index the letters in the word.
    """
    word_indices = {}
    for i, letter in enumerate(word):
        if letter in word_indices:
            word_indices[letter].append(i)
        else:
            word_indices[letter] = [i]
    return word_indices
