import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Liste
prix = [10, 15, 20, 25, 30, 35, 40]
quantites = [100, 80, 70, 60, 50, 40, 30]
satisfaction = [7.5, 8.0, 6.5, 9.0, 7.0, 8.5, 6.0]

#Affichage d'un scatter 3d
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter3D(prix, quantites, satisfaction, c=satisfaction, cmap="coolwarm_r", alpha=0.9)
ax.set_xlabel("Prix")
ax.set_ylabel("Quantites")
ax.set_xlabel("Prix")
ax.set_ylabel("Quantites")

ax.set_xlabel("Prix")
ax.set_ylabel("Quantites")
ax.set_zlabel("Satisfaction")

ax.set_title("Satisfaction vs Prix")


plt.show()

#Version bubble chart


