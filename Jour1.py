def day1_part1(fichier):
    def premier_nombre(liste):
        for i in liste:
            if (i.isnumeric()):
                return i
    sum = 0
    with open(fichier, "r") as f:
        for line in f:
            sum += int(str(premier_nombre(line))+str(premier_nombre(reversed(line))))

    return sum


def day1_part2(fichier):
    def premier_nombre(liste):
        for i in liste:
            if (i.isnumeric()):
                return i

    def replace_nombre(liste):
        liste = liste.replace("one","o1e").replace("two","t2o").replace("three","t3e").replace("four","f4r").replace("five","f5e").replace("six","s6x").replace("seven","s7n").replace("eight","e8t").replace("nine","n9e")
        return liste
    sum = 0
    with open(fichier, "r") as f:
        for line in f:
            new_line = replace_nombre(line)
            sum += int(str(premier_nombre(new_line))+str(premier_nombre(reversed(new_line))))

    return sum

print("-------Jour 1--------")
print("-------Partie 1-------")
print(day1_part1("input_day1.txt"))
print("-------Partie 2-------")
print(day1_part2("input_day1.txt"))