def print_upper_words(words):
    ''' Prints all words, capitalizes all letters in each string '''
    for word in words:
        print (word.upper())

def print_upper_words2(words):
    ''' Prints words that begin with E/e, capitalizes all letters in each string '''
    for word in words:
        if word[0] == 'E' or word[0] == 'e':
            print (word.upper())

def print_upper_words3(words, must_start_with):
    ''' Prints words that begin with letter(s) in must_start_with, capitalizes all letters in each string '''
    for word in words:
        for letter in must_start_with:
            if word[0] == letter:
                print (word.upper())
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes", "ello"])
print_upper_words2(["hello", "hey", "goodbye", "yo", "yes", "ello"])
print_upper_words3(["hello", "hey", "goodbye", "yo", "yes", "ello"], {'h', 'y'})