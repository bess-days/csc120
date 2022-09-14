#Word = print

catalog = { 'MIS': {'mis 101': 4, 'mis 102': 3, 'mis 202': 2},
 'CSC': {'csc 110': 4, 'csc 120': 4, 'csc 352': 3},
 'ECE': {'ece 111': 3, 'ece 222': 3, 'ece 333': 4}}

if "ENGL" not in catalog:
    catalog["ENGL"]  = {}
if "ENGL 101" not in catalog["ENGL"]:
    catalog["ENGL"]["ENGL 101"] = 3


def min_max(L):
    new = []
    for i  in range(len(L)):
        if L[i] % 2 == 0:
            new.append(L[i])
    return(min(new), max(new))

for cat in catalog:
    subject = cat
    lessons = catalog[cat]
    print("{}: {}".format(subject, lessons))

for cat in catalog:
    subject = cat
    lessons = catalog[cat]
    print("{}: {}".format(subject, lessons))

v = "ABCDEFGHIJ"
w = ( ("aa","ab","b"), (12, 23, 34), [45, 56, 67, 78] )
x = { "abc" : 12, "cde" : 34, "efg" : 56 }
y = [ ["pqr", "stu","abc","def"], ["uvw","xyz","bcd","cde"] ]

print(type(v))

#yes
#{'abc': 12, 'cde': 34, 'efg': 56, 'cd': 34}
