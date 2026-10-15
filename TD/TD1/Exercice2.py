import pandas as pd
import os

#Chargement du fichier panda

df = pd.read_csv("./employes.csv")
print("-----Affichage du dataset------")
print(df)
print("------------------")

#Affichage des trois (3) première ligne
print("-----Affichage des 3 premières lignes du dataset------")
print(df.head(3))
print("------------------")

#Le nombre de lignes et colonnes
print("-------Affichage Nombre de lignes et de colonnes----------")
print(df.shape)
print("------------------")

#Les infos générales du dataframe
print("--------Affichage des infos générales---------")
print(df.info())
print("------------------")

#Affichage statistiques descriptive
print("-------Affichage des statistiques descriptive----------")
print(df.describe())
print("------------------")

#Selection de la colonne salaire
print("------Selection de la colone salaire-----------")
print(df.loc[::, "Salaire"])
print("------------------")

#Employe dont le salaire est supérieur à 7500
print("---------Affichage colone ou le salaire est supérieur à 7500--------")
print(df.loc[
          (df["Salaire"] > 7500),
        [
            "Nom",
            "Salaire"
        ]
      ])
print("------------------")

#Triage du dataFrame selon le salaire

print("-------Triage du dataframe seleon le salaire----------")
print(df.sort_values(["Salaire"], ascending=False))
print("------------------")

#Affichage des colonnes nom et département
print("--------Affichage des colonnes nom et departement---------")
print(df[["Nom", "Département"]])
print("------------------")
#Affichage de l'employe Sara
print("---------Affichage de l' employé sara--------")
print(df.loc[
          (df["Nom"] == "Sara"),
      ])
print("------------------")
#Valeur manquantes

print("--------Affichage des valeurs manquantes---------")
nouvelle_ligne = {"Nom":"Ahmed","Département":None,"Âge":30,"Salaire":None,"Ville":"Rabat"}

df.loc[len(df)] = nouvelle_ligne
print(df)
print("------------------")
#Verification des valeurs manquantes

print("---------Verification des valuer null--------")
print(df.isnull())
print("------------------")
#Remplacer les valeurs manquantes du salaire par la moyenne du salaire

print("---------Remplacement des valeurs manquantes du salaire par la moynne des salires--------")
df["Salaire"] = df["Salaire"].fillna(df["Salaire"].mean())
print(df)
print("------------------")
#Supprimer les colones où le departement est manquant
print("---------Suppression des colonnes manquantes--------")
df.dropna(axis=1, inplace=False)
print("------------------")
#Création d'une colone Prime
print("-------Création de la colonne prime----------")
df["Prime"] = df["Salaire"] * 0.1
print(df)
print("------------------")
#Création Salaire totale
print("---------creation de la colonne salaire totale--------")
df["Salaire_Total"] = df["Salaire"] + df["Prime"]
print(df)
print("------------------")
#Suppression de la colone Prime
print("--------Suppression de la colonne prime---------")
df.drop("Prime", axis=1, inplace=True)
print(df)
print("------------------")
#Renomme salaire totale en revenu
print("---------Rennomer salaire totale en revennu--------")
df.rename(columns={"Salaire_Total": "Revenu"}, inplace=True)
print(df)
print("------------------")
#Triage des employe selon leur revenue
print("---------Triage des employé selpn le revenu--------")
df["Revenu"].sort_values(ascending=False)
print(df)
print("------------------")

#Calcul du salaire moyen par département

print("-----------Salaire moyen par département-----------")
salaire_moyen_departement = df.groupby("Département")["Salaire"].mean()
print(salaire_moyen_departement)
print("---------------------------------")

#Le revenu totale par ville
print("-----------------Revenu totale par ville---------------")
revenu_total_par_ville = df.groupby("Ville")["Revenu"].sum()
print(revenu_total_par_ville)
print("---------------------------------")

#Le plus jeune employé de chaque département
print("-----------------Employé le plus jeune par département---------------")
employe_plus_jeune_departement = df.groupby("Département")["Âge"].min()
print(employe_plus_jeune_departement)
print("---------------------------------")

#Enregistrer le fichier csv
file_path = os.path.join(f"{os.getcwd()}", "Exercice2.csv") #os.getcwd() retourne le chemin absolu du repertoire de travail actulle
df.to_csv(file_path, index=False)
