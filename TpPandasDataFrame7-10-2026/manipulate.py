import os
from load_file_csv import load_csv

df = load_csv("Produit.csv")

#Variable constante symbole
e = "=============="

#Affichage des 5 premières lignes du dataframe
print(f"{e}Affichage des 5 premières lignes du DataFrame{e}")
print(df.head())

#Affichage du nombres de lignes et colones du dataframe
print(f"{e}Affichage du nombres de lignes et colones du dataframe{e}")
print(df.shape)

#Vérication du type de données
print(f"{e}Vérication du type de données{e}")
print(df.dtypes)

#Affichage des valeurs uniques
print(f"{e}Valeur Unique{e}")
print(df["Ville"].unique())

#Affichage des info générale du dataframe
print(f"{e}Info Générale{e}")
print(df.info())

#Ajout colonne Total
df["Total"] = df["Quantité"] * df["Prix_Unitaire"]

#Tri des ventes selon le montant total
df.sort_values(by="Total", ascending=False, inplace=True)
print(f"{e}Affichage du dataframe Après tri{e}")
print(df)

#Affichage des lignes où la catégorie est électronique
print(f"{e}Affichage des produits de la catégorie électronique{e}")
print(df.loc[
    (df["Catégorie"] == "Électronique")
])

#Calcul de la somme total des ventes
print(f"{e}Calcul de la somme total des ventes{e}")
print(df["Total"].sum())

#Calcul de la moyenne du prix unitaire
print(f"{e}Calcul de la moyenne du prix unitaire{e}")
print(df["Prix_Unitaire"].mean())

#Identification du produit le plus vendu
print(f"{e}Produit le plus vendu{e}")
print(df.loc[
          df["Quantité"] == df["Quantité"].max()
      ])

#Trouver le prix unitaire max et min
print(f"{e}Prix unitaire max: {e}")
print(df.loc[
    df["Prix_Unitaire"] == df["Prix_Unitaire"].max()
      ])

print(f"{e}Prix unitaire min: {e}")
print(df.loc[
    df["Prix_Unitaire"] == df["Prix_Unitaire"].min()
      ])

#Calcul du total des ventes par villes
print(f"{e}Total des ventes par villes{e}")
print(df.groupby("Ville")["Total"].sum())

#Calcul du total des ventes par catégories
print(f"{e}Calcul du total des ventes par catégories{e}")
print(df.groupby("Catégorie")["Total"].sum())

#Myenne du montant par vendeur
print(f"{e}Moyenne par vendeur{e}")
print(df.groupby("Vendeur")["Total"].mean())

#Nettoyage de la colone ville
df["Ville"] = df["Ville"].apply(lambda ville: ville.strip().upper())
print(f"{e}Affichage du dataset après normalisation de la colonne ville{e}")
print(df)

#Exportation dans un autres fichier
FILE_PATH = os.getcwd() + r"\ventes_nettoyées.csv"
print(FILE_PATH)
df.to_csv(FILE_PATH)

#Bonus
print(f"Total vente: {df["Total"]}\n"
      f"")