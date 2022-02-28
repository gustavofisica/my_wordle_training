def main():
    input_file_path = "my_wordle_training/data/word_source.txt"
    output_file_path = "my_wordle_training/data/wordle_words.txt"
    five_letter_words = []

    with open(input_file_path, "r") as file:
        for line in file.readlines():
            word = line.strip()
            if len(word) == 5:
                five_letter_words.append(word)
    
    with open(output_file_path, "w") as file:
        for word in five_letter_words:
            file.write(word + "\n")
    
    print(f"Found {len(five_letter_words)} five-letter words")
    pass

if __name__ == "__main__":
    main()