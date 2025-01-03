def main():
    book_path = "books/frankenstein.txt"
    book_text = get_file_text(book_path)
    num_words = count_words(book_text)
    print(num_words)

def get_file_text(path):
    with open(path) as file:
        return file.read()

def count_words(string):
    return len(string.split())


main()