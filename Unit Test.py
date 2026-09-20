import unittest
from stats import get_num_words, get_chars_dict, chars_dict_to_sorted_list


class TestBookBotStats(unittest.TestCase):

    # Test Case 1: Word Count Standard Execution (Happy Path)
    def test_get_num_words_returns_correct_count(self):
        # Arrange
        sample_text = "The quick brown fox jumps over the lazy dog."
        expected_word_count = 9

        # Act
        actual_word_count = get_num_words(sample_text)

        # Assert
        self.assertEqual(actual_word_count, expected_word_count)

    # Test Case 2: Word Count Empty String (Edge Case)
    def test_get_num_words_empty_string_returns_zero(self):
        # Arrange
        sample_text = ""
        expected_word_count = 0

        # Act
        actual_word_count = get_num_words(sample_text)

        # Assert
        self.assertEqual(actual_word_count, expected_word_count)

    # Test Case 3: Character Frequency & Lowercase Normalization (Happy Path)
    def test_get_chars_dict_counts_characters_and_normalizes_case(self):
        # Arrange
        sample_text = "Aa Bb 123!"
        expected_dict = {
            "a": 2,
            " ": 2,
            "b": 2,
            "1": 1,
            "2": 1,
            "3": 1,
            "!": 1,
        }

        # Act
        actual_dict = get_chars_dict(sample_text)

        # Assert
        self.assertEqual(actual_dict, expected_dict)

    # Test Case 4: Character Frequency Non-Alphabetic Only (Edge Case)
    def test_get_chars_dict_handles_non_alphabetic_only(self):
        # Arrange
        sample_text = "1234!! @@"
        expected_dict = {
            "1": 1,
            "2": 1,
            "3": 1,
            "4": 1,
            "!": 2,
            " ": 1,
            "@": 2,
        }

        # Act
        actual_dict = get_chars_dict(sample_text)

        # Assert
        self.assertEqual(actual_dict, expected_dict)

    # Test Case 5: Character Dictionary Sorting Order (Happy Path)
    def test_chars_dict_to_sorted_list_sorts_descending_by_frequency(self):
        # Arrange
        input_dict = {"a": 5, "b": 12, "c": 2, "d": 8}
        expected_list = [
            {"char": "b", "num": 12},
            {"char": "d", "num": 8},
            {"char": "a", "num": 5},
            {"char": "c", "num": 2},
        ]

        # Act
        actual_list = chars_dict_to_sorted_list(input_dict)

        # Assert
        self.assertEqual(actual_list, expected_list)


if __name__ == "__main__":
    unittest.main()
