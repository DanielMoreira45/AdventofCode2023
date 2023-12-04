import re
def day4_part1(fichier):
    def crealistes(line):
        ligne = [item.strip() for item in re.split(": | \|", line) if item.strip()]
        nombregagant = ligne[1].split(" ")
        nombresortie = ligne[2].split(" ")
        return nombregagant, nombresortie
        
    def verifgagnant(nombregagant, nombresortie):
        sub_sum = 0
        for nombre in nombregagant:
            for nombresorti in nombresortie:
                if nombresorti.isnumeric():
                    if nombre == nombresorti:
                        if sub_sum > 0:
                            sub_sum *=2
                        else:
                            sub_sum += 1
                else:
                    continue
        return sub_sum
    
    sum = 0
    with open(fichier, "r") as f:
            for line in f:
                listegagant, listenombre = crealistes(line)
                sum += verifgagnant(listegagant, listenombre)
    return sum

def day4_part2(fichier):
    def crealistes(line):
        ligne = [item.strip() for item in re.split(": | \|", line) if item.strip()]
        nombregagant = ligne[1].split(" ")
        nombresortie = ligne[2].split(" ")
        return nombregagant, nombresortie
        
    def verifgagnant(nombregagant, nombresortie, nombregagnantderniereparti = 1):
        sub_sum = 0
        for nombre in nombregagant:
            for nombresorti in nombresortie:
                if nombresorti.isnumeric():
                    if nombre == nombresorti:
                        if sub_sum > 0:
                            sub_sum *=2
                        else:
                            sub_sum += 1
                else:
                    continue
        print(f"sub_sum = {sub_sum}, nombregagnantderniereparti = {nombregagnantderniereparti}")
        return sub_sum * nombregagnantderniereparti, sub_sum
    
    sum = 0
    derniereparti = 1
    with open(fichier, "r") as f:
            for line in f:
                listegagant, listenombre = crealistes(line)
                sub_sum, aled = verifgagnant(listegagant, listenombre, derniereparti)
                sum += sub_sum
                if aled == 0:
                    derniereparti = 1
                else:
                    derniereparti = aled
    return sum

print(day4_part2("input_day4.txt"))