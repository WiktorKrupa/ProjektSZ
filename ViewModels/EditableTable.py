from dash import Dash, dash_table, html, Input, Output

def create_table(NumberOfColumns, Skateboard):
    app = Dash(__name__)

    params = ["Dane produkcyjne", "Całkowite zapotrzebowanie",
              "Planowane przyjęcia", "Przewidywane na stanie",
              "Zapotrzebowanie netto", "Planowanie zamówienia",
              "Planowane przyjęcie zamówień"]
    
    # Generate column labels
    column_labels = [f"Week {i+1}" for i in range(NumberOfColumns)]

    # First table
    table1 = dash_table.DataTable(
        id='table-editing-simple',
        columns=(
            [{'id': 'Model', 'name': ' ', 'presentation': 'dropdown'}] +  # added 'presentation' key for styling
            [{'id': p, 'name': p} for p in column_labels]
        ),
        data=[
            dict(Model=label, **{param: 0 for param in column_labels})
            for label in params
        ],
        editable=True,
        style_cell={  # Adjusting the width of the first column
            'minWidth': '50px', 'width': '50px', 'maxWidth': '50px',
            'textAlign': 'center',  # Centering the content of the first column
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    )
    
    # Second table
    labels = ["Czas realizacji =", "Wielkość partii =", "Poziom BOM =", "Na stanie ="]
    initial_values = [Skateboard.leadTime, Skateboard.batchSize, Skateboard.bomLevel, Skateboard.inStock] 
    table2 = dash_table.DataTable(
        id='table-editing-simple-2',
        columns=[
            {'id': 'Labels', 'name': ' ', 'presentation': 'dropdown'},
            {'id': 'Value', 'name': 'Value'}
        ],
         data=[
            {'Labels': label, 'Value': value} for label, value in zip(labels, initial_values)
        ],
        editable=True,
        style_cell={'textAlign': 'center'},  # Centering the content of cells
    )

    app.layout = html.Div([
        html.Div([
            html.H4("Danee"),
            table1
        ]),
        html.Div([
            html.H4("Dane dodatkowe"),
            table2
        ])
    ])
    
    # Callback to update table1 data
    @app.callback(
        Output('table-editing-simple', 'data'),
        Input('table-editing-simple', 'data_previous'),
        Input('table-editing-simple', 'data'),
    )
    def update_table1_data(data_previous, data):
        if data_previous != data:
            return data
        else:
            return Dash.no_update

    # Callback to update table2 data
    @app.callback(
        Output('table-editing-simple-2', 'data'),
        Input('table-editing-simple-2', 'data_previous'),
        Input('table-editing-simple-2', 'data'),
    )
    def update_table2_data(data_previous, data):
        if data_previous != data:
            return data
        else:
            return Dash.no_update
    
    return app

# if __name__ == '__main__':
#     app = create_table(6)
#     app.run_server(debug=True)
