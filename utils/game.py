import typer

def take_guess(player: int, guessed_letters: set) -> str:
    """
    Handle player input
    """
    is_valid_guess = False
    guess = ""
    while not is_valid_guess:
        guess = input(f"Player {player + 1}, guess a letter: ").lower()
        if guess in guessed_letters:
            typer.echo("You already guessed that letter!")
        elif len(guess) != 1 or not guess.isalpha():
            typer.echo("Incorrect input, Please guess an alphabetic letter")
        else:
            is_valid_guess = True
    return guess

def handle_guess(player: int, guessed_letters: set, players_score: dict[int:int], word_indices: dict[str:list[int]], guess: str, guessed_word: list[str]) -> str:
    """
    Determine if player guess is correct or not
    """
    guessed_letters.add(guess)
    if word_indices.get(guess):
        players_score[player] += len(word_indices[guess])
        for i in word_indices[guess]:
            guessed_word[i] = guess
        typer.echo("Correct guess!")
    else:
        typer.echo("Incorrect guess!")
    return guessed_word

def check_completed_word(word_indices: dict[str:list[int]], guessed_letters: set) -> bool:
    """
    Check all letters in word have been guessed
    """
    return all(letter in guessed_letters for letter in word_indices)

def display_score(players_score: dict[int:int]):
    """
    Display the final score of the game
    """
    winner_score = max(players_score.values())
    winner_name = []
    for player, points in players_score.items():
        if winner_score == points:
            winner_name.append(player)
        typer.echo(f"Player {player + 1}: {points} points")
    
    for winner in winner_name:
        typer.echo(f"Player {winner + 1} Won!")