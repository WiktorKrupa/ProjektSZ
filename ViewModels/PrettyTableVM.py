# import matplotlib.pyplot as plt
# import ipywidgets as widgets
# from IPython.display import display

# def create_table():
#     rows = ["Okres", "Dane produkcyjne", "Całkowite zapotrzebowanie", "Planowane przyjęcia",
#             "Przewidywane na stanie", "Zapotrzebowanie netto", "Planowane zamówienia", "Planowane przyjęcie zamówień"]
#     data = {
#         "Okres": list(range(1, 7)), 
#         "Dane produkcyjne": [0] * 6,
#         "Całkowite zapotrzebowanie": [0] * 6,
#         "Planowane przyjęcia": [0] * 6,
#         "Przewidywane na stanie": [0] * 6,
#         "Zapotrzebowanie netto": [0] * 6,
#         "Planowane zamówienia": [0] * 6,
#         "Planowane przyjęcie zamówień": [0] * 6
#     }

#     cell_text = []
#     for row in rows[1:]:  #skip pierwszego bo się jakieś dziwne rzeczy działy
#         cell_text.append([str(data[row][i]) for i in range(6)])

#     plt.figure(figsize=(10, 4))
#     table = plt.table(cellText=cell_text, loc='center', cellLoc='center', rowLabels=rows[1:], colLabels=list(range(1, 7)))

#     # Kolory
#     cell_colors = [['lightgray' if (i + j) % 2 == 0 else 'white' for j in range(6)] for i in range(len(rows) - 1)]
#     for i in range(len(rows) - 1):
#         for j in range(6):
#             table.get_celld()[(i + 1, j)].set_facecolor(cell_colors[i][j])

#     plt.axis('off')
#     plt.show()
    
#     # Create widgets for editing
#     widgets_dict = {}
#     for i, row in enumerate(rows[1:]):
#         for j in range(6):
#             widgets_dict[(i, j)] = widgets.Text(value=str(data[row][j]), description='', disabled=False)
    
#     def update_table(change):
#         for i, row in enumerate(rows[1:]):
#             for j in range(6):
#                 data[row][j] = int(widgets_dict[(i, j)].value)
#         cell_text = []
#         for row in rows[1:]:
#             cell_text.append([str(data[row][i]) for i in range(6)])
#         for i in range(len(rows) - 1):
#             for j in range(6):
#                 table.get_celld()[(i + 1, j)].get_text().set_text(cell_text[i][j])
    
#     # Display widgets
#     for i, row in enumerate(rows[1:]):
#         for j in range(6):
#             widgets_dict[(i, j)].observe(update_table, names='value')
#             display(widgets_dict[(i, j)])
    
#     # Add a button to trigger the update
#     update_button = widgets.Button(description="Update Table")
#     update_button.on_click(update_table)
#     display(update_button)

# create_table()
