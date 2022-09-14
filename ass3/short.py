wordlist = ['evolve', 'absolve', 'crow', 'spoke', 'truck', 'lake', 'wow', 'wave']
wordlist2 = ['evolve', 'absolve', 'evil', 'absent', 'evidence', 'lake', 'ladder', 'list']
def  words_ending_with(wordlist, tail):
    return [word for word in wordlist if word[len(word) - len(tail):] == tail ]

def word_beginning_with(wordlist, head):
    #this function takes a list of words and returns a list of with the words that begin with the string head
    return [word for word in wordlist if word[:len(head)] == head]
def primary_stress_position(phoneme_list):
    return_value = None
    for i in range(len(phoneme_list)):
        phoneme = phoneme_list[i]
        if phoneme[len(phoneme) -1] == "1":
            return i
    return return_value
