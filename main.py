def main():
  book_contents = get_book_text("books/frankenstein.txt")
  words_number = get_book_words(book_contents)
  print(f"{words_number} words found in the document")

def get_book_text(filepath):
  with open(filepath) as b:
    book_contents = b.read()
    return book_contents
def get_book_words(booktext):
  return len(booktext.split())

main()