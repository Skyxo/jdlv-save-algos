# coding: utf-8

def produit_matriciel(A, B):
    lgAi = len(A)
    lgAj = len(A[0])
    lgBi = len(B)
    lgBj = len(B[0])

    if lgAj != lgBi:
        return False

    lg = lgAj
    M = []

    for i in range(lgAi):
        M.append([])

        for j in range(lgBj):            
            M[i].append(sum([A[i][k]*B[k][j] for k in range(lg)]))

    return int(M[0][0]), int(M[1][0])

def createTableau(n):
    tb_ = []
    for i in range(n):
        tb_.append([])
        for o in range(n):
            tb_[i].append(0)
    return tb_  

def actualize2(liste):                                                 #recherche des cellules voisines et application des regles
    lg = len(liste)
    compteur = 0
    liste2 = createTableau(lg)

    for y in range(lg):

        for x in range(lg):
            
            if y == 0 and x == 0:                                  #cote en haut a gauche

                if liste[y][x+1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                            
            elif y == 0 and x == lg-1:                           #cote en haut a droite

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1
                            
            elif y == lg-1 and x == 0:                           #cote en bas a gauche

                if liste[y][x+1]:
                    compteur += 1

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1
                            
            elif y == lg-1 and x == lg-1:                      #cote en bas a droite

                if liste[y][x-1]:
                    compteur += 1

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1
                        
            elif y == 0 and 1 <= x <= lg-1:                 #ligne du haut

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1   
            
            elif 1 <= y <= lg-1 and x == 0:                 #colonne de gauche

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1  
                
            elif y == lg-1 and 1 <= x <= lg-1:              #ligne du bas

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1

                if liste[y][x-1]:
                    compteur += 1  
                    
            elif 1 <= y <= lg-1 and x == lg-1:             #colonne de droite

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1  
                
            else:                                                            #tous les autres

                if liste[y-1][x]:
                    compteur += 1

                if liste[y-1][x-1]:
                    compteur += 1

                if liste[y][x-1]:
                    compteur += 1

                if liste[y+1][x-1]:
                    compteur += 1

                if liste[y+1][x]:
                    compteur += 1

                if liste[y+1][x+1]:
                    compteur += 1

                if liste[y][x+1]:
                    compteur += 1

                if liste[y-1][x+1]:
                    compteur += 1
        
            if liste[y][x]:                                                #application des règles

                if compteur >= 2 and compteur <= 3:
                    liste2[y][x] = 1

                else:
                    liste2[y][x] = 0

            elif compteur == 3:
                liste2[y][x] = 1
            compteur = 0

    return liste2

def compteur(tab, n):
    count = 0
    
    for i in range(n):
        for o in range(n):
            count += 1 if tab[i][o] else 0
            
    return count
