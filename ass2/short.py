def sum_csv_string(csv_string):
    sum = 0
    for l in csv_string.split(","):
        sum += int(l)
    return sum
def list_to_dict(lists):
    dictionary = {}
    for list in lists:
        dictionary[list[0]] = list[1:]
    print(dictionary)
    return dictionary
def shuffle_dict(somedict):
    shuffled = {}
    sorted_keys = sorted(somedict.keys())
    sorted_vals = sorted(somedict.values())
    for x in range(len(somedict)):
        shuffled[sorted_keys[x]] = sorted_vals[x]
    return shuffled
def invert_dict(orgdict):
    newdict = {}
    orgdict_vals = list(orgdict.values())
    orgdict_keys = list(orgdict.keys())
    for x in range(len(orgdict)):
        newdict[orgdict_vals[x]] = orgdict_keys[x]
    return newdict
def update_dict2(dict2, key1, key2, value):
    newdict2 = dict2
    if key1 or key2 not in newdict2:
        return newdict2
    newdict2[key1][key2] = value
    return newdict2


DD = {'aaa': {'bbb': 'string1', 'ccc': 'string2', 'ddd': 'string3'},
      'bbb': {'ccc': 'string4', 'ddd': 'string5', 'eee': 'string6', 'fff': 'string7'},
      'ccc': {'aaa': 'string8', 'bbb': 'string9'}
      }
update_dict2(DD, 'aaa', 'dddd', 12)

somedict = {345: 'pqr', 456: 'abc', 123: 'wxy', 234: 'ijk'}
shuffle_dict(somedict)
x1 = [['aa', 'bb', 'cc', 'dd'],
      ['ee', 'ff', 'gg', 'hh', 'ii', 'jj'],
      ['kk', 'll', 'mm', 'nn']]
list_to_dict(x1)
sum_csv_string("123")
invert_dict(somedict)



