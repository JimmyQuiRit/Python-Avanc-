import pandas as pd

s1 = pd.Series([1200, 1500, 800, 950, 2000, 1800, 1600], ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"])

#Affichez les valeurs de la serie
print(s1.values)

#Affichez les index
print(s1.index)

#Affichez le type des valeurs
print(s1.dtypes)

#Recuperation de la valeur du mercredi et du dimache avec loc
print("Mercredi: ", s1.loc["mer"])
print("Dimanche: ", s1.loc["dim"])

#Recuperation de la valeur 3 avec iloc
print(s1.iloc[2])

#Multiplication des ventes par 1.2
"""s1 = s1 * 1.2 #Change la serie
print(s1)"""
s2 = s1 * 1.2
print(s2)

#Affichafge des jours ou les ventes dépassent 1500 dhr
print(s1[s1 > 1500])

#Calculons la somme totale des ventes
print(s1.sum())

#Calculons la moyenne des ventes
print(s1.mean())

#Le maximm et le minimum
print("Maximum: ", s1.max)
print("Minimum: ", s1.min())

#Triage de la serie

print("Ordre croissant", s1.sort_values(ascending=True), sep="\n")

print("Ordre croissant", s1.sort_values(ascending=False), sep="\n")

print("Ordre Jour", s1.sort_index(ascending=True), sep="\n")

#Creation d'une nouvelle serie à partir de ce dictionnaire
prix_produits = {"Stylo": 5.5, "Cahier": 12.0, "Livre": 45.0, "Crayon": 3.5, "Gomme": 2.0}

s3 = pd.Series(prix_produits)
print(s3)

#Affichons la liste des produits
print(s3.index)

#Affichage du prix du livre
print("Prix: ", s3.loc["Livre"])

#Calculons le prix moyen
print(s3.mean())

#Triage par ordre decroissant
print(s3.sort_values(ascending=False))

#Ajout d'un nouveau produit
s3["Classeur"] = 18

#Supprimer le produit gomme
s3.drop("Gomme", axis=0, inplace=True) #Inplace = True => La modification se fait directement sur le dataFrame; Dans le cas contraire elle se fait dans une copie qui est renvoyée
print(s3)

#Appliquer une remise de 10%
s3.apply(lambda value: value * 0.9)

#Arrondir les prix à une décimale près
s3.apply(lambda value: round(value, 1))

#Verification de l'exiistence de stylo
print(s3.isin(["Stylo"]))

#convertir en dictionnaire
dictionnaire = s3.to_dict()
print(dictionnaire)

#Valeur manquantes
notes = pd.Series([14, 16, None, 10, None, 18], index=["A", "B", "C", "D", "E", "F"])

#Affichons les valeurs manquantes
print(notes.isnull())

#Remplaçons les valeurs manquantes par la moyenne
nouvelles_notes_valeur_manquante_remplace_par_la_moyenne = notes.fillna(notes.mean(), inplace=False)
print(nouvelles_notes_valeur_manquante_remplace_par_la_moyenne)

#Suppression des valeurs manquates
nouvelles_notes_valeurs_manquantes_supprime = notes.dropna(inplace=False)
print(nouvelles_notes_valeurs_manquantes_supprime)

#Affichage des notes > 12
print(nouvelles_notes_valeurs_manquantes_supprime[nouvelles_notes_valeurs_manquantes_supprime > 12])
