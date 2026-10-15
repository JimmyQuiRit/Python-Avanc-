import matplotlib.pyplot as plt
from matplotlib.pyplot import legend
import os

mois = ("Jan", "Feb", "Mar", "Apr", "May", "Jun")
ventes = (1200, 1500, 1800, 1700, 2100, 2500)
depenses = [900, 1100, 1200, 1500, 1600, 1700]

#Représentation des ventes et des dépenses en fonction des mois
plt.title("Evolution des ventes")
plt.plot(mois, ventes, color="red", label="ventes", marker="o", linestyle="--")
plt.plot(mois, depenses, color="blue", label="depense", marker="o", linestyle="-")

plt.xlabel("mois")
plt.ylabel("ventes")


SAVE_DIR = f"{os.getcwd()}\\figures"

if not os.path.exists(SAVE_DIR):
    os.mkdir(SAVE_DIR)

plt.savefig(f"{SAVE_DIR}\\evolutions_ventes.png")

plt.show()
