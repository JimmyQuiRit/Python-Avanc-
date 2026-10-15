import pandas as pd
import matplotlib.pyplot as plt
import datetime

#charger le fichier csv
df = pd.read_csv("ventes.csv")

#Suppressions des doublons
df.drop_duplicates(inplace=True)

#Suppression des espaces et correction de la casse des  des noms de villes et produits
df["Produit"] = df["Produit"].apply(lambda produit: produit.strip().title())
df["Ville"] = df["Ville"].apply(lambda Ville: Ville.strip().title())

#Remplacement des valeurs manquantes
df["Prix"] = df["Prix"].fillna(df["Prix"].mean())
df["Quantite"] = df["Quantite"].fillna(df["Quantite"].mean())
df["ModePaiement"] = df["ModePaiement"].fillna("inconnu")

#Création de la colonne montant
df["Montant"] = df["Prix"] * (1 - df["Remise"])

#Calcul du chiffres d'affaires totale par ville
print("====Chiffre d'affaire par ville====")
chiffre_affaire_total_par_ville = df.groupby("Ville")["Montant"].sum()
print(chiffre_affaire_total_par_ville)

#Le produit le plus vendu
print("====Produit le plus vendu====")
produit_plus_vendu = df.loc[
    (df["Quantite"] == df["Quantite"].max())
]
print(produit_plus_vendu)
#La ville la plus rentable

print(chiffre_affaire_total_par_ville)
print("====La ville la plus rentable====")
print(
    chiffre_affaire_total_par_ville.idxmax()
      )

#Le CA mensuel
print("====Le CA mensuel====")
#Conversion du champ date str en date (panda.Timestanp)
date = pd.to_datetime(df["Date"])
df["Date"] = date
mois = date.dt.month_name()
df["mois"] = mois
print(df)
print("Le Mois est: ", mois)

CA_mensuel = df.groupby(["mois"])["Montant"].sum()
print(CA_mensuel)

#Visualisation et traçage
plt.title("Chiffre Affaire par mois")
plt.xlabel("Mois")
plt.ylabel("Montant totale")

plt.subplot(2,2,1)
plt.plot(CA_mensuel.index, list(CA_mensuel), marker="o", linestyle="-", color="#8AFFA7")

plt.subplot(2,2,2)
plt.bar(CA_mensuel.index, height=list(CA_mensuel), color="#8AFFA7")

#Affichage figure
plt.show()