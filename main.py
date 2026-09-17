from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)

    print(f"Found {num_words} total words")
    print(sorted_chars_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
