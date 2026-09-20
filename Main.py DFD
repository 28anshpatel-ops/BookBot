# Import sys module to access command-line arguments and system exit functions
import sys

# Import specific helper functions from stats module for processing text data
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list


def get_book_text(path):
    """
    Opens a target text file and reads its raw character contents into memory.
    Catches FileNotFoundError if path does not exist on disk.
    
    Args:
        path (str): Relative or absolute path to the text file.
        
    Returns:
        str: Full string content of the specified text file.
    """
    try:
        # Open file in read mode using context manager for automatic closure
        with open(path) as f:
            # Read complete file stream into memory
            return f.read()
    except FileNotFoundError:
        # Print clean terminal error message if path is invalid
        print(f"Error: The file at '{path}' could not be found.")
        # Terminate program cleanly with failure code
        sys.exit(1)


def print_report(book_path, num_words, sorted_chars):
    """
    Formats and displays character frequency stats and word counts to standard output.
    
    Args:
        book_path (str): Path of the analyzed text file for header output.
        num_words (int): Total word count calculated from text.
        sorted_chars (list): List of character dictionaries sorted by count.
    """
    # Print top border header for visual report separation
    print("============ BOOKBOT ============")
    # Output target file path currently being processed
    print(f"Analyzing book found at {book_path}...")
    # Output word count section header
    print("----------- Word Count -----------")
    # Print calculated total word count value
    print(f"Found {num_words} total words")
    # Output character count section header
    print("--------- Character Count -------")

    # Iterate through every dictionary entry in the sorted character list
    for item in sorted_chars:
        # Extract character symbol string from dictionary item
        char = item["char"]
        # Extract total count integer from dictionary item
        count = item["num"]
        # Check if character is strictly alphabetical
        if char.isalpha():
            # Print character symbol and frequency count pair
            print(f"{char}: {count}")

    # Print bottom border header signifying end of report output
    print("============= END ===============")


def main():
    """
    Coordinates execution flow: checks arguments, loads text, triggers analysis, and prints report.
    """
    # Check if user provided at least one command-line argument beyond script name
    if len(sys.argv) < 2:
        # Output correct CLI usage template if file path argument is missing
        print("Usage: python3 main.py <path_to_book>")
        # Exit execution immediately with failure status code 1
        sys.exit(1)

    # Store provided command-line file path string in local variable
    book_path = sys.argv[1]
    # Read text file into string using file handling helper function
    text = get_book_text(book_path)
    # Calculate total word count in text using string splitting utility
    num_words = get_num_words(text)
    # Generate dictionary containing raw character frequency counts
    chars_dict = get_chars_dict(text)
    # Convert dictionary into sorted list of key-value dictionaries
    sorted_chars_list = chars_dict_to_sorted_list(chars_dict)

    # Output formatted terminal report with calculated metrics
    print_report(book_path, num_words, sorted_chars_list)


# Check if script is run directly as main program rather than imported as module
if __name__ == "__main__":
    # Execute main control function
    main()
