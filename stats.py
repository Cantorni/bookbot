
def get_num_words(booktext):
  return len(booktext.split())

def sort_on(items):
    return items["num"]

def get_char_count(booktext):
  char_count = {}
  list = []
  for word in booktext:
    for char in word:
      if char.lower() in char_count:
        char_count[char.lower()] += 1
      else:
        char_count[char.lower()] = 1
  for char in char_count:
    if char.isalpha(): 
      list.append({"char": char, "num": char_count[char]})
  list.sort(reverse=True,key=sort_on)
  return list
