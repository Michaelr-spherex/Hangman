import typer
from utils.word import load_words, index_word, check_completed_word
from utils.game import enter_num_of_players, handle_guess, take_guess, display_score
import random

app = typer.Typer()

@app.command()
def play_game(filename: str = "wordlist.txt", max_words: int = 15):
    """
    Play Hangman game.
    """
    
    words = load_words(filename)
    words_to_play = random.sample(words, min(max_words, len(words)))
    typer.echo("Welcome to Hangman!")
    number_of_players = enter_num_of_players()
    players = []
    for i in range(number_of_players):
        player_name = input(f"What will player {i + 1} be called?")
        players.append({"score": 0, "name": player_name})
            
    if max_words > len(words):
        typer.echo(f"\nThe number of words you entered is bigger than the exisiting words. You'll be playing with the maximum number of words available")
    
    for i in range(len(words_to_play)):
        typer.echo(f"\nNew word! {str(i + 1)}/{str(len(words_to_play))}")
        word_indices = index_word(words_to_play[i])
        guessed_letters = set()
        guessed_word = ["_"] * len(words_to_play[i])
        player_turn = 0
        while not check_completed_word(word_indices, guessed_letters):
            typer.echo("\n" + "  ".join([f"{player["name"]}: {player["score"]}" for player in players]))
            typer.echo(f"Current word: {" ".join(guessed_word)}")
            typer.echo(f"\nGuessed Letters: {" ".join(guessed_letters)}")
            guess = take_guess(player_turn, guessed_letters)
            guessed_word = handle_guess(player_turn, guessed_letters, players, word_indices, guess, guessed_word)
            player_turn = (player_turn + 1) % number_of_players

        typer.echo(f"The word was {words_to_play[i]}")
        
    typer.echo("\nGame over!")
    display_score(players)

if __name__ == "__main__":
    app()
