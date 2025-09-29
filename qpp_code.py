# Auteur : Fournera A.

import numpy as np
import random as rd
import matplotlib as mp
import matplotlib.pyplot as plt
import math as ma


pi = ma.pi  # affectation de la constante pi à pi pour simplifier le code
sin = ma.sin  # De même avec la fonction sin
cos = ma.cos  # etc

fancy_blue = "#21488B"  # choix d'un bleu "fancy" pour faire des graphes magnifiques
fancy_grey = "#F5F5F5"  # (...)

##Implémentation de l'écran

Xmin = -3  # coordonnées de l'écran
Xmax = 3  # .
Ymin = -1  # .
Ymax = 1  # .
Xpixel = 50  # Nombre de pixels selon OX
Ypixel = 50  # Nombre de pixels selon OY
nombre_p = 100000  # nombre de photons


# Définition des fonctions utiles dans l'exercice
def p_x_d(x, Xmin, Xmax):
    """Densité de probabilité en x"""
    E = (1 + cos(2 * pi * x)) / (
        Xmax - Xmin + (sin(2 * pi * Xmax) - sin(2 * pi * Xmin)) / (2 * pi)
    )
    return E


def p_x(x, Xmin, Xmax):
    """fonction de répartition en x"""
    E = (x - Xmin + (sin(2 * pi * x) - sin(2 * pi * Xmin)) / (2 * pi)) / (
        Xmax - Xmin + (sin(2 * pi * Xmax) - sin(2 * pi * Xmin)) / (2 * pi)
    )
    return E


# Fonction de résolution par dichotomie
def dichotomie(f, a, b, tolerance=1e-6, max_iter=1000):
    """fonction de résolution par dichothomie"""
    # Initialisation des bornes initiales
    left = a
    right = b

    # Nombre d'itérations effectuées
    iterations = 0

    # Boucle de recherche de la solution
    while iterations < max_iter:
        mid = (left + right) / 2
        # Calcul de la valeur de la fonction au point "mid"
        f_mid = f(mid)

        # Test de convergence
        if abs(f_mid) < tolerance:
            return mid

        # Mise à jour des bornes
        if f_mid < 0:
            left = mid
        else:
            right = mid

        iterations += 1

    # Si la boucle se termine sans trouver de solution, renvoyer None
    return None


# Initialisation des listes des positions des photons sur l'écran
ylist = []
xlist = []

# Tirage des valeurs de x et y
for i in range(nombre_p):
    alea = rd.random()
    # Résolution par dichotomie de l'équation P(t, Xmin, Xmax) - alea = 0
    x_solution = dichotomie(lambda t: p_x(t, Xmin, Xmax) - alea, Xmin, Xmax)
    if x_solution is not None:
        xlist.append(x_solution)
    # La densité de probabilité pour y est uniforme
    ylist.append(Ymin + (Ymax - Ymin) * rd.random())


"""
# Définition des valeurs de x dans l'intervalle [-3, 3] avec une résolution de 400 points
A = np.linspace(Xmin, Xmax, 400)
# Calcul de la densité de probabilité en fonction de chaque valeur de x
E1 = [p_x_d(x, Xmin, Xmax) for x in A]
# Calcul de la fonction de répartition cumulée en fonction de chaque valeur de x
E2 = [p_x(x, Xmin, Xmax) for x in A]
# Tracé des deux courbes sur un même graphique
plt.plot(A, E1, color=fancy_blue, label="Densite de probabilite")
plt.plot(A, E2, "darkorange", label="Probabilité cumulee")
# Ajout d'une grille pour une meilleure lisibilité du graphique
plt.grid()
# Ajout de l'axe des abscisses avec le label "x"
plt.xlabel("x")
# Ajout de l'axe des ordonnées avec le label "Probabilité"
plt.ylabel("Probabilité")
# Ajout de la légende dans le coin supérieur gauche du graphique
plt.legend(loc="upper left")
# Affichage du graphique
plt.show()


# Définition des valeurs de y dans l'intervalle [-1, 1] avec une résolution de 400 points
B = np.linspace(-1, 1, 400)
# Calcul de la densité de probabilité uniforme pour chaque valeur de y
F1 = [1 / (Ymax - Ymin) for y in B]
# Calcul de la fonction de répartition cumulée pour chaque valeur de y
F2 = [(y - Ymin) / (Ymax - Ymin) for y in B]
# Tracé des deux courbes sur un même graphique
plt.plot(B, F1, color=fancy_blue, label="Densite de probabilite")
plt.plot(B, F2, "darkorange", label="Probabilité cumulee")
# Ajout d'une grille pour une meilleure lisibilité du graphique
plt.grid()
# Ajout de l'axe des abscisses avec le label "y"
plt.xlabel("y")
# Ajout de l'axe des ordonnées avec le label "Probabilité"
plt.ylabel("Probabilité")
# Ajout de la légende dans le coin supérieur gauche du graphique
plt.legend(loc="upper left")
# Affichage du graphique
plt.show()
"""



# Création de l'image d'interférence souhaitée pour l'image intermédiaire
Image = [[0 for i in range(Xpixel)] for j in range(Ypixel)]
# Cette ligne crée une liste 2D nommée "Image" remplie de zéros, avec une taille de Ypixel lignes et Xpixel colonnes.
# Elle est utilisée pour représenter une image où chaque élément représente la valeur d'un pixel. En initialisant tous les pixels à zéro,
# on crée une image vide avant d'ajouter des valeurs correspondant à l'intensité lumineuse des photons arrivant à chaque position sur l'image.

for i in range(nombre_p):
    # Calcul de la position X et Y du photon reçu (en pixels)
    # Conversion de l'échelle de [Xmin,Xmax] à [0,Xpixel] et [Ymin,Ymax] à [0,Ypixel].
    Position_X = int(Xpixel * (xlist[i] - Xmin) / (Xmax - Xmin))
    Position_Y = int(Ypixel * (ylist[i] - Ymin) / (Ymax - Ymin))

    # Incrémentation de la valeur du pixel où arrive le photon
    Image[Position_Y][Position_X] += 1

    # Affichage de l'image pour certaines valeurs de i (celle demandé par l'exercice)
    if i in [999, 9999, 99999]:
        plt.imshow(Image, cmap=mp.cm.gray)
        plt.title("Après l'arrivée de " + str(i + 1) + " photons")
        plt.show()
# Visualisation 2D de l'image de 100 000 pixels



# Crée un nuage de points
plt.scatter([], [], color="blue")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Nuage de photons")

plt.gca().set_facecolor("black")

# Affiche le tracé initial
plt.draw()
plt.pause(0.000005)

# Parcours les coordonnées et ajoute les points un par un
for x, y in zip(xlist, ylist):
    plt.scatter(x, y, color="#FFFFFF", marker="s", s=0.5)
    plt.draw()
    plt.pause(0.000005)  # Ajuste la durée de la pause si nécessaire

# Garde la fenêtre du tracé ouverte
plt.show(block=True)
