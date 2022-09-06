def establish(file):
    pokemon = open(file, "r")
    rows = []
    for row in pokemon:
        if "#" not in row:
            row.strip("")
            lines = row.split(",")
            rows.append(lines)
    return rows
def entries(rows):
    entries = {}
    data = {}
    averages = {}
    for i in range(len(rows) - 1):
        entry = rows[i]
        names = entry[1]
        type = entry[2]
        if names not in entries:
            entries[names] = {}
        entries[names]["types"] = type
        if type not in data:
            data[type] = {}
        if type == entries[names]["types"] and names not in data[type]:
            data[type][names] = {}
        if type not in averages:
            averages[type] = []
        data[type][names] = {}
        if len(entry[3]) >= 0:
            data[type][names]["total"] = int(entry[4])
            data[type][names]["hp"] = int(entry[5])
            data[type][names]["attack"] = int(entry[6])
            data[type][names]["defense"] = int(entry[7])
            data[type][names]["specialattack"] = int(entry[8])
            data[type][names]["specialdefense"] = int(entry[9])
            data[type][names]["speed"] = int(entry[10])
    return data
def input_process(file, par):
    results = []
    averages = {}
    finishing = {}
    comparable = []
    par = par.lower()
    types_all = ["total", "speed", "attack", "specialattack", "defense", "specialdefense", "hp"]
    for i in range(len(types_all)):
        if par != types_all[i] and par not in types_all:
            par = input()
    for of_type in entries(establish(file)):
        average = of_type
        pokemon = entries(establish(file))[average]
        if average not in averages:
            averages[average] = []
        for p in pokemon:
            averages[average].append(pokemon[p][par])
        all = sum(averages[average])
        divisible = len(averages[average])
        average = all / divisible
        finishing[average] = average
        comparable.append(average)
    for finish in finishing:
        max_average = max(comparable)
        pokemon_type = finish
        if finishing[finish] == max_average:
            results.append(pokemon_type)
    for result in sorted(results):
        print("{}: {}".format(result, max(comparable)))
def main():
    file = input()
    entries(establish(file))
    par = input()
    while len(par) > 0:
        input_process(file, par)
        par = input()
main()

