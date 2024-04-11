# I suggest you use pathlib.Path for file paths next time. It's easier for many things.


def load_words(filename: str) -> str:
    # CR: same comment about name of function and docstring
    """
    Load words from file.
    """
    with open(filename, "r") as file:
        words = file.read().splitlines()
    return words


def index_word(word: str) -> dict[str : list[int]]:
    """
    Index the letters in the word.
    """
    word_indices = {}
    for i, letter in enumerate(word):
        # CR: this could have been made a bit easier to read by using defaultdict. "defaultdict"s are cool. Use them :)
        if letter in word_indices:
            word_indices[letter].append(i)
        else:
            word_indices[letter] = [i]
    return word_indices


# CR: same comment about name of function and docstring
def check_completed_word(
    word_indices: dict[str : list[int]], guessed_letters: set
) -> bool:
    """
    Check all letters in word have been guessed
    """
    return all(letter in guessed_letters for letter in word_indices)
