# You’ve been hired to help build a puzzle game that includes a secret code challenge. 
# In one level, players must enter a magic word that is the same when read forwards and backwards — a palindrome — to unlock the next clue.

# Your job is to write a program that:

# Accepts a word (or sentence) from the player.

# Checks if it is a palindrome using string manipulation.

def palindrome(word):
    revs_word =""
    for i in word:
        revs_word = i + revs_word
    if word == revs_word:
        print("The entered magic word is palindrome")
    else:
        print("The entered magic word is not palindrome")
        
        
magic_word = input("enter a magic word: ")
palindrome(magic_word)

