import random
import string
from words import words
def get_word():
    word=random.choice(words)
    #Since some words are like "work-day" or "work day"
    while '-'in word or ' 'in word:
        word=random.choice(word)
    return word

def print_the_word(used,word):
    for i in word:
        if i in used:
            print(i,end=' ')
        else:print('_',end=' ')

word=get_word().upper()
# word="what"
print(f"it is a {len(word)} letter word")
word_set=set(word)
print(word_set)
input_set=set()
used_set=set()#letters used by user
alphabet=set(string.ascii_uppercase)#set of alphabets
c=0
while c!=6:
    if word_set == used_set:
        print(f"\nAmazing!the word is {word}")
        break
    ip=input("\n\t\tGuess a letter: ").upper()
    if ip in alphabet:#if among alphabets
        #Success case
        if ip in word_set:
            used_set.add(ip)
            print("\tCorrect")#end of success case
        else:
            print("\tNope!")
            c+=1
            print("\t"+"X"*c)
            #If failed
        alphabet.remove(ip)
        input_set.add(ip)
    elif ip in input_set:print("\tAlready used this character,Try again")#if in alrready used set of words
    else:print("\tInvalid input")# if the input is not a alphabet
    print_the_word(used_set,word)
else:print(f"\nYou lost!the word is {word}")
