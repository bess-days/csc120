def read_file(file):
    entry = {}
    entries_all = [i for i in open(file, "r")]
    words_entry_all = [entries.split() for entries in entries_all]
    word_entry = [entry for entry in words_entry_all for w in entry]
    test = [word_entry[i] for i in range(len(word_entry))]
    for t in test:
        entry["word"] = t[0]
    print(entry)
    entry["phonemes"] = word_entry[1:]
    entry["vowels"] = [vowel for vowel in word_entry if vowel[len(vowel) - 1].isdigit()]


def read_files(file, word):
    entry = {}
    entry["word"] = []
    wor = ""
    empty_list = []
    words = []
    inner = {}
    entries_all = [i for i in open(file, "r")]
    for entries in entries_all:
        empty_list.append(
            entries.split())
    for list in empty_list:
        if list[0] not in inner:
            inner[list[0]] = []
        inner[list[0]].append(list[1:])
    for i in inner:
        phonemes = inner[i]
        for n in range(len(phonemes)):
            print(phonemes)


    print(inner)
    for w in words:
        entry[w] = []







def get_word(entry, word):
    stress_vowel = ""
    stress_loc = 0
    print(entry["word"])
    if entry["word"].upper() == word.upper():
        print(entry["word"])









def main():
    read_files("tdict.txt", "SILLY")

main()