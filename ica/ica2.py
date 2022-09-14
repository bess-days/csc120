lists = []
for num in range(0, 102, 2)[::-1]:
    print(num)

for num in range(0, 102, 2)[::-1]:
    lists.append(num)


def get_words(s):
    sentence = s.split('-')
    print(sentence)


get_words('CS-120-Summer-2018-U-of-A')


def sum_column(grid, offset):
    sum = 0
    for gr in grid:
        sum += gr[offset]
    print(sum)


sum_column([[11, 22, 33, 34], [12, 5, 6, 7]], 0)


def print_some_words(file, n):
    lines = open(file, "r")
    results = []
    for line in lines:
        lin = line.strip(",;\n")
        l = lin.split(" ")
        for i in range(len(l)):
            if l[i] == n:
                results.append(l[i])
            print(results)


print_some_words("../files", 3)
