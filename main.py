def main() -> None:
    folder = "books"
    book = "frankenstein.txt"
    pathfile = f"{folder}/{book}"

    with open(pathfile) as f:
        file_contents = f.read()

if __name__ == '__main__':
    main()