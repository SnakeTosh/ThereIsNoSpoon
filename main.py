import sys
import math

def found_voisin_doite(position_x1, position_y1, i, grille):

    position_y2 = 0
    rep = ""
    rep = rep + " " + str(position_x1) + " " + str(position_y1)
    for i in grille :
        position_x2 = 0
        for a in i :

            if a == "0":
                if position_x2 > position_x1:
                    if position_y1 == position_y2 :
                        rep = rep + " " + str(position_x2) + " " + str(position_y2)
                        return rep
            position_x2 += 1
        position_y2 += 1

        if position_y2 > position_y1:
            position_x2 = -1
            position_y2 = -1
            rep = rep + " " + str(position_x2) + " " + str(position_y2)
            return rep


def found_voisin_bas(position_x1,position_y1, i, rep, grille):
    position_y3 = 0

    for i in grille :
        position_x3 = 0
        for a in i :

            if a == "0":
                if position_y3 > position_y1 :
                    if position_x1 == position_x3:
                        rep = rep + " " + str(position_x3) + " " + str(position_y3)
                        return rep

            position_x3+=1
        position_y3+=1

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grille = []
for i in range(height):
    liste = []
    line = input()  # width characters, each either 0 or .
    for i in line :
        liste.append(i)

    grille.append(liste)

liste_de_noeud = []
position_y1 = 0
for i in grille:
    position_x1 = 0

    for a in i:

        if a == "0":

            rep = found_voisin_doite(position_x1,position_y1,i,grille)
            if  found_voisin_bas(position_x1,position_y1, i, rep, grille) == None:
                position_x3 = -1
                position_y3 = -1
                rep = rep + " " + str(position_x3) + " " + str(position_y3)
            else :
                rep = found_voisin_bas(position_x1,position_y1, i, rep, grille)

            liste_de_noeud.append(rep)
        position_x1 += 1
    position_y1 += 1

for i in liste_de_noeud:
    print(i)