def day2_part1(fichier):
    bags = {"red" : 12, "green" : 13, "blue":14}

    def get_id(ligne):
        res = ""
        for i in ligne:
            if i.isnumeric():
                res += str(i)
        return int(res)

    def traitement(ligne):
        liste_possible = list()
        contenue = ligne.split(":")
        contenu = contenue[1].split(";")
        for bag in contenu:
            dico_parti = dict()
            new_bag = bag.split(" ")
            for i in range(len(new_bag)):
                item = new_bag[i].replace("\n","").replace(",","")
                if item in bags:
                    if new_bag[i-1].isnumeric():
                        if item in dico_parti:
                            dico_parti[item] += int(new_bag[i-1])
                        else:
                            dico_parti[item] = int(new_bag[i-1])
            liste_possible.append(all(dico_parti[key] <= bags[key] for key in dico_parti))
        if all(liste_possible):
            return get_id(contenue[0])
        else:
            return 0
        
    sum = 0
    with open(fichier,'r')as f:
        for line in f:
            sum += traitement(line)

    return sum


def day2_part2(fichier):
    def traitement(ligne):
        contenue = ligne.split(": ")
        contenu = contenue[1].split("; ")
        dico_parti = dict()
        for bag in contenu:
            new_bag = bag.split(" ")
            for i in range(len(new_bag)):
                item = new_bag[i].replace("\n","").replace(",","")
                if item.isalpha():
                    if item in dico_parti.keys() and dico_parti[item] < int(new_bag[i-1]):
                        dico_parti[item] = int(new_bag[i-1])
                    else:
                        dico_parti[item] = int(new_bag[i-1])
        return multiplication(dico_parti)

    def multiplication(dico_parti):
        sum = 1
        for key in dico_parti:
            sum *= dico_parti[key]
        return sum

    sum = 0
    with open(fichier,'r')as f:
        for line in f:
            sum += traitement(line)

    return sum


print("-------Jour 2--------")
print("-------Partie 1-------")
print(day2_part1("input_day2.txt"))
print("-------Partie 2-------")
print(day2_part2("input_day2.txt"))
