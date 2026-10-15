import pandas as pd
import csv

class Etudiant:
    def __init__(self, nom, age, note):
        self.nom = nom
        self.age = age
        self.note = note
        self.FILE_NAME = 'Etudiant.csv'

    def affchage(self):
        print("Nom: ", self.nom)
        print("Age: ", self.age)
        print("Note: ", self.note)

    def sauvegarder_csv(self):

        with open(self.FILE_NAME, 'a') as csvfile:
            dictionnaire_donnees = {"Nom": self.nom, "Age": self.age, "Note": self.note}
            etudiant = csv.DictWriter(csvfile, fieldnames=dictionnaire_donnees.keys())
            etudiant.writeheader()
            etudiant.writerow(dictionnaire_donnees)


etudiant1 = Etudiant("Jimmy", 22, 15)
etudiant1.affchage()
etudiant1.sauvegarder_csv()