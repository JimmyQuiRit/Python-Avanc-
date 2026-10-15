
import numpy as np
import matplotlib.pyplot as plt

#Création des notes entières entre 0 et 20
notes_math = np.random.randint(0, 21, 30)
print("----Affichage des notes Math----")
print(notes_math)

#Création des notes décimal entre 5 et 20
notes_python = np.random.uniform(5, 20, 30)
print("----Affichage des note Python----")
print(notes_python)

#Assemblage des 2 matrices
print("----Affichage des notes----")
notes = np.column_stack((notes_math, notes_python))
print(notes)

#Calcul de la moyenne par matière
print("----Affichage des moyennes----")

moy_math = notes[:, 0].mean()
moy_python = notes[:, 1].mean()

print("----Math----")
print("moyenne", moy_math, sep=": ")

print("----Python----")
print("moyenne", moy_python, sep=": ")

#Calcul de la mediane par matière
print("----Affichage des médianes----")

med_math = np.median(notes[:, 0])
med_python = np.median(notes[:, 1])

print("----Math----")
print("Medianne", med_math, sep=": ")

print("----Python----")
print("Medianne", med_python, sep=": ")

#Ecart-type

print("----Affichage de l'écart type----")

std_math = notes[:, 0].std()
std_python = notes[:, 1].std()

print("----Math----")
print("Ecart-type", std_math, sep=": ")

print("----Python----")
print("Ecart-type", std_python, sep=": ")


#Notes minimales
print("----Affichage des notes minmales----")

min_math = notes[:, 0].min()
min_python = notes[:, 1].min()

print("----Math----")
print("Notes minimale", min_math, sep=": ")

print("----Python----")
print("Note maximale", min_python, sep=": ")

#Notes maximales
print("----Affichage des notes minmales----")

max_math = notes[:, 0].max()
max_python = notes[:, 1].max()

print("----Math----")
print("Notes minimale", max_math, sep=": ")

print("----Python----")
print("Note maximale", max_python, sep=": ")

#Affichages des notes > 15

notes_math_sup = notes[:, 0][notes[:, 0] > 15]
notes_python_inf = notes[:, 1][notes[:, 1] < 10]
print("----Math----")
print("Notes supérieur à 15", notes_math_sup, sep=": ")

print("----Python----")
print("Notes inférieur à 10", notes_python_inf, sep=": ")

#Etudiant de la meilleur notes en python
print("-----Meilleur notes en python-----")
python_max_notes = notes[:, 1].max()
print("Notes max: ", round(python_max_notes, 2))

#La moyenne générale par étudiant
print("----Moyenne générale par étudiant----")
moyenne_par_etudiant = notes.mean(axis=1)
print(moyenne_par_etudiant)

#Triage des notes par ordre croissant
print("----Triage Notes ordres----")

math_asc = np.sort(notes_math)
python_desc = np.sort(notes_python)

print("----Math----")
print("Croissant: ", math_asc)

print("----Python----")
print("Décroissant", python_desc)

#Création d' un tableau contenant python - math
print("----Création tableau----")
tableau = notes_python - notes_math
print(tableau)

#Ajout du tableau dans notes
print("----Affichage du tableau----")
tableau = tableau.reshape(30, 1)

notes = np.hstack((notes, tableau))
print(notes)

#Algèbre linéaire
A = np.array(
    ([2, 5],
    [1, 3])
)

print("----Calcul de déterminant----")
det = np.linalg.det(A)
print(det)

print("----Inverse----")
inverse = np.linalg.inv(A)
print(inverse)