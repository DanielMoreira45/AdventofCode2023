def day3_part1(fichier):
    def crea_matrice(ficher):
        matrice = []
        with open(ficher,'r') as f:
            for ligne in f:
                matrice.append(list(ligne.strip()))
        return matrice
    
    def symbole(matrice, x,y):
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i < 0 or j < 0 or i >= len(matrice) or j >= len(matrice[0]):
                    continue
                if matrice[i][j] != "." and not(matrice[i][j].isnumeric()):
                    return True
        return False
    
    def trouvee_nombre(matrice, i , j):
        suite = []
        k = 0
        for k in range(len(matrice[0])-j):
            if matrice[i][j+k].isnumeric():
                suite.append((i,j+k))
            else:
                return (suite, j+k)
        return (suite, j+k)

    def traitement(matrice):
        sum = 0
        for i in range(len(matrice)):
            pos_j = -1
            for j in range(len(matrice[0])):
                if pos_j > j:
                    continue
                else:
                    if matrice[i][j].isnumeric():
                        numero = ""
                        liste_pos_nombre, pos_j = trouvee_nombre(matrice, i , j)
                        oui = not all(not symbole(matrice, posi, posj) for posi, posj in liste_pos_nombre)
                        if oui:
                            for posi, posj in liste_pos_nombre:
                                numero += f"{matrice[posi][posj]}"
                            sum += int(numero)
        return sum
    matrice = crea_matrice(fichier)
    return traitement(matrice)



print("-------Jour 3--------")
print("-------Partie 1-------")
print(day3_part1("input_day3.txt"))
# print("-------Partie 2-------")
# print(day3_part2("input_day3.txt"))