from cgitb import reset
from wordle import Wordle


def main():
    print("Hello Wordle!")
    wordle = Wordle("APPLE")

    while wordle.can_attempt:
        x = input("Type your guess: ")
        wordle.attempt(x)
        result = wordle.guess(x)
        print(*result, sep="\n")

    if wordle.is_solved:
        print("You've solved the puzzle.")
    else:
        print("You failed to solve the puzzle!")


if __name__ == "__main__":
    main()
