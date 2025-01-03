def main():
    book_path = "./frankenstein.txt"
    book_text = get_file_text(book_path)
    num_words = count_words(book_text)
    characters = count_chars(book_text)

    generate_report(book_path, num_words, characters)

# opens file at the given path to read
def get_file_text(path):
    with open(path) as file:
        return file.read()

# returns number of words in string
def count_words(string):
    return len(string.split())

# return dict of count of each char in string
def count_chars(string):
    lowercase = string.lower()
    char_dict = dict()

    for c in lowercase:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    
    return char_dict

# generates report detailing the num_words and chars in a book
def generate_report(book, num_words, chars):
    print(f"--- Begin report of {book} ---")
    print(f"{num_words} words found in the document\n")

    # convert dict into list of lists (of each key-value pair)
    char_list = list(chars.items())
    # sort list of lists by value
    char_list.sort(reverse=True, key=lambda x : x[1])

    # print num of occurrences of each alphabetic char
    for c in char_list: 
        if c[0].isalpha():
            print(f"The '{c[0]}' character was found {c[1]} times")

    print("--- End report ---")


main()