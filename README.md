# BookBot

BookBot is a Python-based Command-Line Interface (CLI) application designed to analyze text files (such as digital books) and generate detailed statistical reports. It processes full-length books to extract total word counts and frequency analysis for every alphabetic character, presented in a clean, sorted report.

---

## Features

- **Word Count Analysis:** Reads full text files and computes total word counts.
- **Character Frequency Analysis:** Counts the occurrence of all characters, handling case-insensitivity (e.g., treating `'A'` and `'a'` as the same character).
- **Sorted Statistical Output:** Filters for alphabetic characters and presents frequency data ordered from most frequent to least frequent.
- **Command-Line Interface:** Takes target text paths as command-line arguments, complete with usage validation and error messaging.

---

## Directory Structure

```text
.
├── main.py
├── stats.py
├── books/
│   ├── frankenstein.txt
│   ├── mobydick.txt
│   └── prideandprejudice.txt
└── README.md
```

---

## Requirements

- **Python:** 3.8 or higher installed on your system.

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/your-username/bookbot.git](https://github.com/your-username/bookbot.git)
   ```
2. Navigate into the project directory:
   ```bash
   cd bookbot
   ```
3. Ensure your text files are placed inside the `books/` directory.

---

## Usage

Run `main.py` using Python 3, passing the relative path to the target book file as an argument:

```bash
python3 main.py books/frankenstein.txt
```

### System Behavior & Input Handling

- If no argument is provided, the program outputs standard usage instructions and terminates safely:
  ```text
  Usage: python3 main.py <path_to_book>
  ```

---

## Example Output

Running the tool on `books/frankenstein.txt`:

```text
$ python3 main.py books/frankenstein.txt
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count -----------
Found 75757 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
r: 20807
h: 19725
l: 12739
d: 16863
m: 10604
u: 10407
c: 9243
f: 8731
y: 7914
w: 7638
p: 6121
g: 5971
b: 5026
v: 3847
k: 1755
x: 677
j: 504
q: 324
z: 243
============= END ===============
```

---

## Credits & Acknowledgments

- Built as part of the **Boot.dev** curriculum (Build a Bookbot in Python).
- Classic book texts sourced from Project Gutenberg.
- Collin Del Rosario, for making me have many sleepless nights. 
