#!/usr/bin/python

# Converts a word to a hash key
# by taking the word, converting it
# to lowercase, sorting the letters
# and combining the word back as a
# string
def word_to_key(word):
  return ''.join(sorted(word.lower()))

# Takes a filename a builds a word
# list hash with the value being a 
# list of anagrams for the given 
# key 
def build_word_list(filename):
  word_list = { }
  input_file = open(filename, 'rU')
  for line in input_file:
    word = line.strip()
    key = word_to_key(word)
    if key in word_list:
      word_list[key].append(word)
    else:
      word_list[key] = [word]
  input_file.close()
  return word_list

# Retrieves the anagrams for the
# word given the word_list and 
# the word. Results include
# the original word.
def get_anagrams(word_list, word):
  key = word_to_key(word)
  if key in word_list:
    anagrams = word_list[key]
  else:
    anagrams = [word]
  return anagrams 
  
# Build the word_list and retrieve
# anagrams for some example words
def main(): 
  word_list = build_word_list('/usr/share/dict/words')
  anagrams = get_anagrams(word_list, 'top')
  print(anagrams)
  anagrams = get_anagrams(word_list, 'retains')
  print(anagrams)
  anagrams = get_anagrams(word_list, 'something')
  print(anagrams)
  
if __name__ == '__main__':
  main()
