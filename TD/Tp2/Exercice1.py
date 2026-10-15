import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#Notes Etudians
ETUDIANT_NOTES = (10, 12, 14, 13, 15, 17, 16)
SEMESTRES = (1, 2, 3, 4, 5, 6, 7)

#Ages etudiants
AGES =  (18, 19, 20, 21, 20, 22, 21, 23, 24, 19, 20, 21, 22, 23)

#Nombres Etudiants par filière
FILERES = ("AI", "Big Data", "Cyber", "Robotic")

NB_ETUDIANTS = (120, 90, 75, 60)

#Expériences salaires des diplomés (3D scatter plot)
EXPERIENCE = (1, 2, 3, 4, 5)
SALAIRE = (4000, 4500, 5500, 6500, 8000)
AGE_DIPLOMES = (23, 24, 25, 27, 30)

#Création du Line char 1
plt.subplot(2,2,1)
plt.title("Notes Etudiants")
plt.xlabel("Semestres")
plt.ylabel("Notes")
plt.plot(SEMESTRES,
         ETUDIANT_NOTES,
         label="NOTES",
         color="#C4C4C4",
         marker="o",
         linestyle="-",)


#Création de l'histogramme 2
plt.subplot(2,2,2)
plt.title("Ages Etudiants")
plt.xlabel("Ages")
plt.bar(AGES,
        height=AGES,
        color="#C0BBFC",
        width=0.8,)

#Creation du Bar Chart
plt.subplot(2,2,3)
plt.title("Nombre Etudiants")
plt.xlabel("Filieres")
plt.ylabel("Etudiants")
plt.bar(FILERES,
        NB_ETUDIANTS,
        color="#F527D6",
        width=0.8,
        )

#Création du 3D scatters plot
#plt.subplot(2,2,4)
ax = plt.subplot(2,2,4, projection="3d")
ax.scatter(EXPERIENCE, SALAIRE, AGE_DIPLOMES, c="#63F870")

ax.set_xlabel("Experience")
ax.set_ylabel("Salaire")
ax.set_zlabel("Etudiants")


#Affichage de la figure
plt.tight_layout()
plt.show()
