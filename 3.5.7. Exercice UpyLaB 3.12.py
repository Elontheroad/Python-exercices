"""
Cet exercice propose une variante de l’exercice précédent sur le carré de X.
Écrire un programme qui lit en entrée une valeur naturelle n
et qui affiche à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).
"""

n=int(input())
a=0
for a in range (n):
    ligne = " "*a+"X"*(n-a)
    a=a+1
    print(ligne)

    






