# Écrire un programme qui lit en entrée deux nombres entiers strictement positifs,
# et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.
# Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.


n1=int(input())
n2=int(input())
if (n1//n2 and n1%n2==0) or (n2//n1 and n2%n1==0):
    print("False")
else:
    print("True")

