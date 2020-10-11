"""
Écrire un programme qui demande à l’utilisateur combien de plis de papier sont nécessaires pour se rendre sur la Lune, et pose la question tant que l’utilisateur n’a pas saisi la bonne réponse.
Si la réponse saisie par l’utilisateur n’est pas correcte, le programme affiche le message "Mauvaise réponse.", puis pose à nouveau la question.
Si la réponse saisie par l’utilisateur est correcte, le programme affiche le message "Bravo !", et s’arrête.
"""

question=int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
plis=42
while question != plis:
    question=question+1
    print("Mauvaise réponse.")
    question=int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
while question == plis:
    question=question+1
    print("Bravo !")


