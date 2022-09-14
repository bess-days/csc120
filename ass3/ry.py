def get_word(word, file):
    words = []
    pri_stress = []
    pri_loc = 0
    entries_all = [i for i in open(file, "r")]
    entries = [ent.split() for ent in entries_all]
    the_word = [w for w in entries if word.upper() in w]
    for wor in the_word:
        pri_stress =  [w for w in wor if w.endswith("1")]
        pri_loc = wor.index(pri_stress[0])
        stress  = pri_stress, pri_loc

    for entry in entries:
        print(entry)


get_word("silly", "tdict.txt")