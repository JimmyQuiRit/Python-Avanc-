import matplotlib.pyplot as plt

marque = ["Samsung", "Apple", "Xiaomi", "Oppo"]
marche = [31, 27, 13, 6]

plt.title("Part de marché des fabricants de smartphone en 2024")
plt.pie(marche,
        colors=["red", "green", "blue", "cyan"],
        labels=marque,
        explode=[0.1, 0.1, 0, 0],
        )
plt.show()
