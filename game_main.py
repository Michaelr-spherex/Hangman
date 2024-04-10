import typer
from utils.word import load_words, index_word
from utils.game import handle_guess, take_guess, check_completed_word, display_score
import random

app = typer.Typer()

@app.command()
def play_game(filename: str = "wordlist.txt", max_words: int = 15):
    """
    Play Hangman game.
    """
    number_of_players = 2
    words = load_words(filename)
    words_to_play = random.sample(words, min(max_words, len(words)))
    players_score = {i : 0 for i in range(number_of_players)}
    
    for i in range(len(words_to_play)):
        typer.echo(f"\nNew word! {str(i + 1)}/{str(len(words_to_play))}")
        word_indices = index_word(words_to_play[i])
        guessed_letters = set()
        guessed_word = ["_"] * len(words_to_play[i])
        player_turn = 0
        while not check_completed_word(word_indices, guessed_letters):
            typer.echo("\n" + "  ".join([f"Player {player_index + 1}: {score}" for player_index, score in players_score.items()]))
            typer.echo(f"Current word: {" ".join(guessed_word)}")
            guess = take_guess(player_turn, guessed_letters)
            guessed_word = handle_guess(player_turn, guessed_letters, players_score, word_indices, guess, guessed_word)
            player_turn = (player_turn + 1) % number_of_players

        typer.echo(f"The word was {words_to_play[i]}")
        
    typer.echo("\nGame over!")
    display_score(players_score)

if __name__ == "__main__":
    app()
