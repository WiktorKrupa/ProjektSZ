import matplotlib.pyplot as plt

def create_table():
    rows = ["Okres", "Dane produkcyjne", "Całkowite zapotrzebowanie", "Planowane przyjęcia",
            "Przewidywane na stanie", "Zapotrzebowanie netto", "Planowane zamówienia", "Planowane przyjęcie zamówień"]
    data = {
        "Okres": list(range(1, 7)), 
        "Dane produkcyjne": [0] * 6,
        "Całkowite zapotrzebowanie": [0] * 6,
        "Planowane przyjęcia": [0] * 6,
        "Przewidywane na stanie": [0] * 6,
        "Zapotrzebowanie netto": [0] * 6,
        "Planowane zamówienia": [0] * 6,
        "Planowane przyjęcie zamówień": [0] * 6
    }

    cell_text = []
    for row in rows[1:]:  # Skip the first row label
        cell_text.append([str(data[row][i]) for i in range(6)])

    plt.figure(figsize=(10, 4))
    plt.table(cellText=cell_text, loc='center', cellLoc='center', rowLabels=rows[1:], colLabels=list(range(1, 7)))
    plt.axis('off')
    plt.show()


