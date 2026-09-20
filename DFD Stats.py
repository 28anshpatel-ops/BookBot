def get_num_words(text):
    """
    Splits string into tokens delimited by whitespace and returns word count.
    
    Args:
        text (str): Raw string content of input book text.
        
    Returns:
        int: Total count of word tokens.
    """
    # Split raw text string into list of individual words by whitespace
    words = text.split()
    # Measure length of word list and return total count as integer
    return len(words)


def get_chars_dict(text):
    """
    Constructs a frequency map for every lowercase character in the input string.
    
    Args:
        text (str): Raw string content of input book text.
        
    Returns:
        dict: Key-value map of character strings to frequency counts.
    """
    # Initialize empty dictionary to store character frequency counts
    chars = {}
    # Loop through every individual character symbol in input text string
    for c in text:
        # Convert character to lowercase for case-insensitive counting
        lowered = c.lower()
        # Check if lowercase character already exists as key in dictionary
        if lowered in chars:
            # Increment existing character occurrence count by 1
            chars[lowered] += 1
        else:
            # Create new dictionary key with initial occurrence count of 1
            chars[lowered] = 1
    # Return fully populated character frequency dictionary
    return chars


def sort_on(dict_item):
    """
    Extraction function serving as sort key for list ordering.
    
    Args:
        dict_item (dict): Dictionary element formatted as {"char": str, "num": int}.
        
    Returns:
        int: Character frequency count value used during sort comparisons.
    """
    # Return numeric count value used as primary sorting criteria
    return dict_item["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    """
    Transforms frequency dictionary into list of single-pair dicts sorted by count descending.
    
    Args:
        num_chars_dict (dict): Raw character frequency dictionary.
        
    Returns:
        list: List of dicts sorted in descending order by character frequency.
    """
    # Initialize empty list to hold structured character records
    sorted_list = []
    # Iterate over key-value pairs in character dictionary
    for ch, count in num_chars_dict.items():
        # Append newly formatted dictionary record to list
        sorted_list.append({"char": ch, "num": count})
    # Sort list in-place descending based on numeric frequency count key
    sorted_list.sort(reverse=True, key=sort_on)
    # Return sorted list of character record dictionaries
    return sorted_list
