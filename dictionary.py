# Make sure to first install PyDictionary with "pip install PyDictionary"
# Ever have a huge list of words to define? Don't feel like using Google and constantly waste precious time by deleting the
# old word and typing in the new one? Well, with this simple, barely working script, you don't have to delete that old word!
# Now you can just type the new one in and instantly get your result! Sure, it's not a lot of time saved, but it all adds up,
# right?

from PyDictionary import PyDictionary    # PyDictionary is a dictionary module that's easy to use with Python
dictionary=PyDictionary()

while True:
    print("What do you want to know the definition of?\n")
    word = input()
    print(dictionary.meaning(word))
    word = ""
