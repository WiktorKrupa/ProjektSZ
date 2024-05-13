from dash import Dash, dash_table, html, Input, Output, State
from Logics.ProcessData import UpdateTableData, UpdateGHP

def create_ghp_table():
    ghp_table = dash_table.DataTable(
        id='ghp-table',  # Corrected ID for the main GHP table
        columns=(
            [{'id': 'Description', 'name': ''}] +
            [{'id': f'Week {i+1}', 'name': f'Week {i+1}'} for i in range(6)]
        ),
        data=[
            {'Description': 'Przewidywany popyt'},
            {'Description': 'Produkcja'},
            {'Description': 'Dostępne'}
        ],
        editable=True,
        style_table={'height': '200px', 'overflowY': 'auto'},
        style_cell={'textAlign': 'center', 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
    )
    time_stock_table = dash_table.DataTable(
        id='ghp-time-stock-table',
        columns=[
            {'id': 'Description', 'name': ''},
            {'id': 'Value', 'name': 'Value'}
        ],
        data=[
            {'Description': 'Czas realizacji'},
            {'Description': 'Na stanie'}
        ],
        editable=True,
        style_table={'height': '100px', 'overflowY': 'auto'},
        style_cell={'textAlign': 'center', 'minWidth': '100px', 'width': '100px', 'maxWidth': '100px'},
    )
    return html.Div([
        html.H3('GHP Table', style={'textAlign': 'center'}),
        html.Div([
            html.Div([
                html.H4('Przewidywany popyt, Produkcja i Dostępne', style={'textAlign': 'center'}),
                ghp_table
            ], style={'flex': '2'}),
            html.Div([
                html.H4('Czas realizacji i Na stanie', style={'textAlign': 'center'}),
                time_stock_table
            ], style={'flex': '1', 'margin-right': '20px'}),
        ], style={'display': 'flex'}),
    ])
def create_table(NumberOfColumns, Skateboard):
    app = Dash(__name__)
    
    #Zeby wyświetlić te dane trzeba odkomentować fragment poniżej, wtedy dla wszystkich tabel są takie same - funkcja do testów
    # dataExample = [
    # {'Model': 'Całkowite zapotrzebowanie', 'Week 1': '1', 'Week 2': '11', 'Week 3': '77', 'Week 4': '1', 'Week 5': '2', 'Week 6': '7'}, 
    # {'Model': 'Planowane przyjęcia', 'Week 1': '2', 'Week 2': '22', 'Week 3': '88', 'Week 4': '0', 'Week 5': '7', 'Week 6': '6'}, 
    # {'Model': 'Przewidywane na stanie', 'Week 1': '3', 'Week 2': '33', 'Week 3': '66', 'Week 4': '2', 'Week 5': '6', 'Week 6': '5'},
    # {'Model': 'Zapotrzebowanie netto', 'Week 1': '4', 'Week 2': '44', 'Week 3': '5', 'Week 4': '3', 'Week 5': '5', 'Week 6': '4'},
    # {'Model': 'Planowanie zamówienia', 'Week 1': '5', 'Week 2': '55', 'Week 3': '4', 'Week 4': '3', 'Week 5': '4', 'Week 6': '3'},
    # {'Model': 'Planowane przyjęcie zamówień', 'Week 1': '6', 'Week 2': '66', 'Week 3': '3', 'Week 4': '5', 'Week 5': '3', 'Week 6': '2'}
    # ]

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
            data=[dict(Model=label, **{param: 0 for param in column_labels})
                for label in params],
            editable=True,
            style_cell={
                'minWidth': '50px', 'width': '50px', 'maxWidth': '50px',
                'textAlign': 'center', 'overflow': 'hidden',
                'textOverflow': 'ellipsis',
            },
        )

        # Include 'Update' label and default value in the initial values
        labels = ["Czas realizacji =", "Wielkość partii =", "Poziom BOM =", "Na stanie =", "Update ="]
        default_values = initial_values + ['0']  # Add default value for 'Update'

        table2 = dash_table.DataTable(
            id=f'table-editing-simple-2-{id_suffix}',
            columns=[
                {'id': 'Labels', 'name': ' '},
                {'id': 'Value', 'name': 'Value'}
            ],
            data=[
                {'Labels': label, 'Value': value} for label, value in zip(labels, default_values)
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

# Then adjust the initial_values in your section setup to include this new value.

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
        html.H1('GHP Table', style={'textAlign': 'center'}),
        create_ghp_table(),
        html.Hr(),  # Separator
        html.Div([
            getattr(app, f'section{suffix}') for suffix, _, _ in sections
        ], style={'width': '90%', 'margin': 'auto'})
    ])
    # Update callbacks to include suffix
    for suffix, _, _ in sections:
        app.callback(
            Output(f'table-editing-simple-{suffix}', 'data'),
            Output(f'table-editing-simple-2-{suffix}', 'data'),
            Input(f'table-editing-simple-{suffix}', 'data'),
            Input(f'table-editing-simple-2-{suffix}', 'data'),
            State(f'table-editing-simple-{suffix}', 'data_previous'),
            State(f'table-editing-simple-2-{suffix}', 'data_previous')
        )(lambda data1, data2, data_previous1, data_previous2, suffix=suffix: update_data(data_previous1, data_previous2, data1, data2, int(suffix)))


    @app.callback(
    Output('ghp-table', 'data'),
    Input('ghp-table', 'data'),
    Input('ghp-time-stock-table', 'data'),
    State('ghp-table', 'data_previous'),
    State('ghp-time-stock-table', 'data_previous'),
    )
    def update_ghp(data_ghp, data_time_stock, data_previous_ghp, data_previous_time_stock):
        if data_ghp != data_previous_ghp or data_time_stock != data_previous_time_stock:
            updated_data_ghp, updated_data_time_stock = UpdateGHP(data_ghp, data_time_stock, data_previous_ghp, data_previous_time_stock)
            return updated_data_ghp
        return data_ghp
    return app

def update_data(data_previous1, data_previous2, data1, data2, week):
    edited = False
    if data_previous1 != data1 or data_previous2 != data2:
        edited = True
    updated_data1 = UpdateTableData(data1, data2, '0', edited, week)  # Pass suffix to your function
    return updated_data1, data2

