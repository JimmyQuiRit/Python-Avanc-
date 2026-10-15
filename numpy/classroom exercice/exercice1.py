import numpy as np
import matplotlib.pyplot as plt

notes = np.random.uniform(0, 20, 20)
notes = np.round(notes, 2)


#Affichage de la moyenne des notes
print("-----Moyennes------")
moyenne = np.mean(notes)
print(moyenne)

#Affichage de l' écart type
print("-----Ecart type------")
ecart_type = np.std(notes)
print(round(ecart_type, 2))

#Affichage de la note maximale
print("-----Notes maximale------")
note_max = np.max(notes)
print(note_max)

#Affichage des notes supérieur à la moyenne
print("-----Notes supérieur à la moyenne------")
notes_sup = notes[notes >= 10]
print(notes_sup)

#Affichage des notes dans l' ordre croissant
print("----Ordre croissant------")
ordre = np.sort(notes)
print(ordre)
