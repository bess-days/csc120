def establish(file):
    pokemon = open(file, "r")
    rows = []
    for row in pokemon:
        if "#" not in row:
            row.strip("")
            lines = row.split(",")
            rows.append(lines)
    return rows
def set_dict(rows):
    entries = {}
    data = {}
    averages = {}
    for i in range(len(rows)):
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
def inputs(file, skill):
    averages = {}
    outputs = []
    perskill = []
    all_entries = set_dict(establish(file))
    sums = 0
    for entries in all_entries:
        for pokemon in all_entries[entries]:
            if entries not in averages:
                averages[entries] = []
            averages[entries].append(all_entries[entries][pokemon][skill])
        for i in range(len(averages[entries])):
            sums += averages[entries][i]
        avg = sums/len(averages[entries])
        averages[entries] = [avg]
        perskill.append(avg)
        sums = 0
    highest = sorted(perskill)[len(perskill) -1]
    for average in averages:
        if averages[average] == [highest]:
            outputs.append(average)
    for i in sorted(outputs):
        print("{}: {}".format(i, highest))
def main():
    file = input()
    set_dict(establish(file))
    skill = input().lower()
    skills_all = ["total", "speed", "attack", "specialattack", "defense", "specialdefense", "hp"]
    while len(skill) > 0:
        for i in range(len(skills_all)):
            if skill != skills_all[i] and skill not in skills_all:
                skill = input().lower()
        inputs(file, skill)
        skill = input().lower()
main()