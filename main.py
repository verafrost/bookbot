def main() -> None:
    folder = "books"
    book = "frankenstein.txt"
    pathfile = f"{folder}/{book}"

    with open(pathfile) as f:
        file_contents = f.read()

    words = file_contents.split()
    word_count = len(words)

    print(word_count)

if __name__ == '__main__':
    main()