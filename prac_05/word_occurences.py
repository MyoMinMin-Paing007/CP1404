"""
Word Occurrences
Estimate: 20 minutes
Actual:  25 minutes
"""


"""
Text: this is a collection of words of nice words this is a fun thing it is
a : 2
collection : 1
fun : 1
is : 3
it : 1
nice : 1
of : 2
thing : 1
this : 2
words : 2
"""

sentence = input("Enter a sentence: ")
characters = sentence.split()
print(characters)

dict_characters = {}
for character in characters:
    dict_characters[character] = characters.count(character)

max_length = max((len(word) for word in dict_characters))
for character, count_character in sorted(dict_characters.items()):
    print(f"{character:{max_length}} : {count_character}")