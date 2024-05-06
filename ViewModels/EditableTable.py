from dash import Dash, dash_table, html, Input, Output, State
from Logics.ProcessData import UpdateTableData

def create_table(NumberOfColumns, Skateboard):
    app = Dash(__name__)
    
    dataExample = [
    {'Model': 'Całkowite zapotrzebowanie', 'Week 1': '1', 'Week 2': '11', 'Week 3': '77', 'Week 4': '1', 'Week 5': '2', 'Week 6': '7'}, 
    {'Model': 'Planowane przyjęcia', 'Week 1': '2', 'Week 2': '22', 'Week 3': '88', 'Week 4': '0', 'Week 5': '7', 'Week 6': '6'}, 
    {'Model': 'Przewidywane na stanie', 'Week 1': '3', 'Week 2': '33', 'Week 3': '66', 'Week 4': '2', 'Week 5': '6', 'Week 6': '5'},
    {'Model': 'Zapotrzebowanie netto', 'Week 1': '4', 'Week 2': '44', 'Week 3': '5', 'Week 4': '3', 'Week 5': '5', 'Week 6': '4'},
    {'Model': 'Planowanie zamówienia', 'Week 1': '5', 'Week 2': '55', 'Week 3': '4', 'Week 4': '3', 'Week 5': '4', 'Week 6': '3'},
    {'Model': 'Planowane przyjęcie zamówień', 'Week 1': '6', 'Week 2': '66', 'Week 3': '3', 'Week 4': '5', 'Week 5': '3', 'Week 6': '2'}
]

    def generate_table_pair(id_suffix, initial_values, section_title):
        params = [
            "Całkowite zapotrzebowanie", "Planowane przyjęcia",
            "Przewidywane na stanie", "Zapotrzebowanie netto",
            "Planowanie zamówienia", "Planowane przyjęcie zamówień"
        ]

        column_labels = [f"Week {i + 1}" for i in range(NumberOfColumns)]

        table1 = dash_table.DataTable(
            id=f'table-editing-simple-{id_suffix}',
            columns=([{'id': 'Model', 'name': ' '}]+
                     [{'id': p, 'name': p} for p in column_labels]),
            # data=[dict(Model=label, **{param: 0 for param in column_labels})
            #       for label in params],
            data = dataExample,
            editable=True,
            style_cell={
                'minWidth': '50px', 'width': '50px', 'maxWidth': '50px',
                'textAlign': 'center', 'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
        )

        labels = ["Czas realizacji =", "Wielkość partii =", "Poziom BOM =", "Na stanie ="]
        table2 = dash_table.DataTable(
            id=f'table-editing-simple-2-{id_suffix}',
            columns=[
                {'id': 'Labels', 'name': ' '},
                {'id': 'Value', 'name': 'Value'}
            ],
            data=[
                {'Labels': label, 'Value': value} for label, value in zip(labels, initial_values)
            ],
            editable=True,
            style_cell={'textAlign': 'center'},
        )

        return html.Div([
            html.H3(section_title, style={'textAlign': 'center'}),
            html.Div([
                html.H4("Dane"),
                table1
            ]),
            html.Div([
                html.H4("Dane dodatkowe"),
                table2
            ])
        ], className="section")

    sections = [
        ('1', [Skateboard.leadTime, Skateboard.batchSize, Skateboard.bomLevel, Skateboard.inStock], "Skateboard"),
        ('2', [Skateboard.wheels.leadTime, Skateboard.wheels.batchSize, Skateboard.wheels.bom, Skateboard.wheels.inStock], "Wheels"),
        ('3', [Skateboard.tracks.leadTime, Skateboard.tracks.batchSize, Skateboard.tracks.bom, Skateboard.tracks.inStock], "Tracks"),
        ('4', [Skateboard.deck.leadTime, Skateboard.deck.batchSize, Skateboard.deck.bom, Skateboard.deck.inStock], "Deck"),
        ('5', [Skateboard.plywood.leadTime, Skateboard.plywood.batchSize, Skateboard.plywood.bom, Skateboard.plywood.inStock], "Plywood")
    ]
    for suffix, initial_values, title in sections:
        setattr(app, f'section{suffix}', generate_table_pair(suffix, initial_values, title))

    app.layout = html.Div([
        getattr(app, f'section{suffix}') for suffix, _, _ in sections
    ], style={'width': '90%', 'margin': 'auto'})

    # Update callbacks to include suffix
    for suffix, _, _ in sections:
        app.callback(
            Output(f'table-editing-simple-{suffix}', 'data'),
            Output(f'table-editing-simple-2-{suffix}', 'data'),
            Input(f'table-editing-simple-{suffix}', 'data_previous'),
            Input(f'table-editing-simple-2-{suffix}', 'data_previous'),
            State(f'table-editing-simple-{suffix}', 'data'),
            State(f'table-editing-simple-2-{suffix}', 'data')
        )(lambda data_previous1, data_previous2, data1, data2, suffix=suffix: update_data(data_previous1, data_previous2, data1, data2, suffix))

    return app

def update_data(data_previous1, data_previous2, data1, data2, suffix):
    if data_previous1 != data1 or data_previous2 != data2:
        updated_data1 = UpdateTableData(data1, data2, suffix)  # Pass suffix to your function
        return updated_data1, data2
    else:
        return data1, data2
