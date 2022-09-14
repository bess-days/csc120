"""
File: pokemon.py
Author: Sydney Bess Greenspun
Purpose: This file allows a user to find out the Pokémon type (based on data from a file) is the best (the highest score) at the skill the user inputs

"""
def establish(file):
    """
    This function reads a csv of varies lines,
     each line representing an entry of a pokemon,
     the commas separating types
    :param file:
    :return: each pokein as a lis (row)
     t of it's qualities adding to a list of lists (rows)
    """
    pokemon = open(file, "r")
    rows = []
    for row in pokemon:
        if "#" not in row:
            #This excludes the first line that sets the types
            row.strip("")
            lines = row.split(",")
            rows.append(lines)
    return rows
def set_dict(rows):
    """
    This function takes the lists of lists established in the previous
    function and turns it into a dictionary.
    There are two main dictionaries,
    the first being what is returned: data
    data is a dictionary of keys of the
     different pokemon types. The subdictionary
      (entries)  has the key of the pokemon's name
       and a value of another dictionary
    The data inside data[type][names] is a dictionary
     where the keys are the category as seen above,
      and the value is the value of that skill
    :param the list of lists :
    :return: the dictictionary data which
     has each type with individual dictionaries
      with keys of the pokemon name and it's traits
    """
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
        if type == entries[names]["types"] and \
                names not in data[type]:
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
    """
    This function takes the user input which is the
     skill they want information about and the file
      it reads from. This takes the data
      turned in set dict and iterates through it
      First, there is the dictionary 'averages'
      which holds keys of each type of Pokémon (entries.)
      then, it reads through the entries of each
      pokemon and sets the average of type to the
      values of that pokemon at index ["skill""]
       which is the user input
       Next, it iterates through the list of data
       asociated with the skill and calculates the
       average. There, it returns to the types
       level in the dictionary and prints the
       sum of each type while appended those
       averages to another dictionary 'perskill'
       which gathers all the sums to determinate
       the highest level per skill
       Finally, if the highest data point is int the
       averages[entries]
       (which now equals a single number) then that
       means the the type ("entries") has the highest
    :param file: file which is read through
     the data and therefore gets established within
    :param skill: user input established in main()
    :return: null, but prints a statement using
     .format to fill in the output in the phrase
    """
    averages = {}
    outputs = []
    perskill = []
    all_entries = set_dict(establish(file))
    #I could have established this another way, but kept running into errors

    sums = 0
    for entries in all_entries:
        for pokemon in all_entries[entries]:
            if entries not in averages:
                averages[entries] = []
            averages[entries].append(all_entries[entries]
                                     [pokemon][skill])
        for i in range(len(averages[entries])):
            sums += averages[entries][i]
        avg = sums/len(averages[entries])
        averages[entries] = [avg]
        perskill.append(avg)
        sums = 0
    highest = sorted(perskill)[len(perskill) -1]
    for average in averages:
        if averages[average] == [highest]:
            # compares the average of each type to the total highest
            outputs.append(average)
    for i in sorted(outputs):
        print("{}: {}".format(i, highest))
def main():
    """
    This function accepts the input 'file'
     which is needed as a parameter for establish,
     which is then used to set the dictionary
    It also asks for the user input of skill and
     does two thing to user input: makes it lower
      case and checks that what user inputted can
       be mapped, if not, it prompts user for new
        input or if it is blank, it again asks for
         user input. Next it uses the function
         inputs() which takes the data and input
         and returns through a print statement the
         desired result
    :return: null, but does allow a loop so
     as long as the user types something, it keeps
      spitting information
    """
    file = input()
    set_dict(establish(file))
    skill = input().lower()
    skills_all = ["total", "speed", "attack", "specialattack",
                  "defense", "specialdefense", "hp"]
    while len(skill) > 0:
        for i in range(len(skills_all)):
            if skill != skills_all[i] and\
                    skill not in skills_all:
                skill = input().lower()
        inputs(file, skill)
        skill = input().lower()
main()