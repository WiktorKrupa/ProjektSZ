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
    for row in rows[1:]:  #skip pierwszego bo się jakieś dziwne rzeczy działy
        cell_text.append([str(data[row][i]) for i in range(6)])

    plt.figure(figsize=(10, 4))
    table = plt.table(cellText=cell_text, loc='center', cellLoc='center', rowLabels=rows[1:], colLabels=list(range(1, 7)))

    # Do zabawy
    # table.auto_set_font_size(False)
    # table.set_fontsize(10)
    # table.scale(1.2, 1.2)  # Scale up the table for better readability

    # Kolory
    cell_colors = [['lightgray' if (i + j) % 2 == 0 else 'white' for j in range(6)] for i in range(len(rows) - 1)]
    for i in range(len(rows) - 1):
        for j in range(6):
            table.get_celld()[(i + 1, j)].set_facecolor(cell_colors[i][j])

    plt.axis('off')
    plt.show()

