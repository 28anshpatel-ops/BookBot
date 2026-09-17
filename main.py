from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list


def print_report(book_path, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_chars:
        char = item[0]
        count = item[1]
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ==============")



def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)

    print_report(book_path, num_words, sorted_chars_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
