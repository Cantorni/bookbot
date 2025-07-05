from stats import *

def main():
  print("============ BOOKBOT ============")
  book_path = "books/frankenstein.txt"
  print(f"Analyzing book found at {book_path}")
  book_contents = get_book_text(book_path)
  words_number = get_num_words(book_contents)
  char_count = get_char_count(book_contents)
  print("----------- Word Count ----------")
  print(f"Found {words_number} total words")
  print("--------- Character Count -------")
  print_char(char_count)
  print("============= END ===============")

def print_char(char_count):
  for char in char_count:
    print(f"{char["char"]}: {char["num"]}")

def get_book_text(filepath):
  with open(filepath) as b:
    book_contents = b.read()
    return book_contents
  
main()