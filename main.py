import secrets
from tkinter.messagebox import RETRY
from wordle import Wordle
from letter_state import LetterState
from colorama import Fore
from typing import List
import random


def main():
    choose_language = 0
    while choose_language != "1" or choose_language != "2":
        print("Choose game language")
        print("1 - English")
        print("2 - Portuguese")
        choose_language = str(input("Enter the option: "))
        break

    if choose_language == "1":
        word_set_data = "my_wordle_training/data/wordle_words.txt"
    elif choose_language == "2":
        word_set_data = "my_wordle_training/data/wordle_words_portuguese.txt"

    word_set = load_word_set(word_set_data)
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input("\nType your guess: ")
        if len(x) != wordle.WORD_LENGTH:
            print(
                Fore.RED + f"Word must be {wordle.WORD_LENGTH} characters long!" + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")
        print(f"The secret word was: {wordle.secret}")


def display_results(wordle: Wordle):
    print("\nYour results so far...\n")
    print(f"\nYou have {wordle.remaining_attempts} attempts remaining.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_to_color(result)
        lines.append(colored_result_str)

    for _ in range(wordle.remaining_attempts):
        lines.append(" ".join(["_"] * wordle.WORD_LENGTH))

    draw_border_around(lines)


def convert_result_to_color(result: List[LetterState]):
    result_with_color = []
    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.LIGHTRED_EX
        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)
    return " ".join(result_with_color)


def draw_border_around(lines: List[str], size: int = 9, pad: int = 1):
    content_length = size + pad * 2
    top_border = "???" + "???" * content_length + "???"
    bottom_border = "???" + "???" * content_length + "???"
    space = " " * pad
    print(top_border)

    for line in lines:
        print("???" + space + line + space + "???")

    print(bottom_border)


def load_word_set(path: str):
    word_set = set()
    with open(path, "r") as file:
        for line in file.readlines():
            word = line.strip().upper()
            word_set.add(word)
    return word_set


if __name__ == "__main__":
    main()
