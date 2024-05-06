from dash import Dash, dash_table, html, Input, Output, State
from Logics.ProcessData import UpdateTableData

## funkcja tworząca interaktywną tabelę 
def create_table(NumberOfColumns, Skateboard):
    app = Dash(__name__)

    # Ustawienie etykiet wierszy i liczby wierszy. 
    # Dodanie wartości do tablicy spowoduje dodanie
    # wiersza do tablicy z podaną etykietą 
    params = [ "Całkowite zapotrzebowanie",
              "Planowane przyjęcia", "Przewidywane na stanie",
              "Zapotrzebowanie netto", "Planowanie zamówienia",
              "Planowane przyjęcie zamówień"]
    
    # Ustawienie etykiet kolumn i liczby kolumn
    # Na podstawie zmiennej Number of columns ustalana jest
    # liczba kolumn. Ustalane są etykiety 'Week 1', 'Week 2' etc.
    # Działanie analogiczne do ustawiania wierszy powyżej. 
    column_labels = [f"Week {i+1}" for i in range(NumberOfColumns)]

    # Tworzenie głównej tabeli
    table1 = dash_table.DataTable(
        #Dodawanie kolumn i wierszy. mechanizm z dokumentacji dash
        #Dopóki działa to nie trzeba wiedzieć o co tu chodzi
        id='table-editing-simple',
        columns=(
            [{'id': 'Model', 'name': ' ', 'presentation': 'dropdown'}] + 
            [{'id': p, 'name': p} for p in column_labels]
        ),
        #Wypełnienie tabeli danymi, a konkretnie zerami. 
        #W dalszej części projektu pewnie będzie to trzeba zmienić.
        data=[
            dict(Model=label, **{param: 0 for param in column_labels})
            for label in params
        ],
        
        # Editable i styl tabeli - zwykły
        editable=True,
        style_cell={  
            'minWidth': '50px', 'width': '50px', 'maxWidth': '50px',
            'textAlign': 'center',  
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
        },
    )
    
    # Tworzenie tabeli z bom, stanem itp.
    
    # etykiety wierszy
    labels = ["Czas realizacji =", "Wielkość partii =", "Poziom BOM =", "Na stanie ="]
   
    # Ustawienie wartości z obiektu Skateboard
    # Te wartości przypisywane są w funkcji Logic.GetSkateboard.getSkate()
    # Wyświetlają się w tabeli po uruchomieniu aplikacji
    initial_values = [Skateboard.leadTime, Skateboard.batchSize, Skateboard.bomLevel, Skateboard.inStock] 
    table2 = dash_table.DataTable(
        # Mechanizm tworzenia tabeli dash
        id='table-editing-simple-2',
        columns=[
            {'id': 'Labels', 'name': ' ', 'presentation': 'dropdown'},
            {'id': 'Value', 'name': 'Value'}
        ],
         data=[
            {'Labels': label, 'Value': value} for label, value in zip(labels, initial_values)
        ],
        editable=True,
        style_cell={'textAlign': 'center'},  
    )

    # Layout na stronie i ustawienie nazw tabel
    app.layout = html.Div([
        html.Div([
            html.H4("Dane"),
            table1
        ]),
        html.Div([
            html.H4("Dane dodatkowe"),
            table2
        ])
    ])
    
    
    # Callback pierwszej tabeli
    # Gdy w tabeli wprowadzimy zmiane (wpiszemy 
    # do komórki nową wartośc i wciśniemy enter, uruchamia się callback)
    # dostajemy data_previous - dane przed zmianą
    # oraz data - dane po zmianie 
    @app.callback(
        Output('table-editing-simple', 'data'),
        Input('table-editing-simple', 'data_previous'),
        State('table-editing-simple', 'data'),
    )
    
    # Callback wywołuje funkcję capture_table_data 
    # funkcja sprawdza czy dane się zmieniły i jeśli tak
    # wywołuje funkcje UpdateTableData(data)
    #               Logics.ProcessData.UpdateTableData(data)
    # która zwraca dane które zostaną pokazane na tabeli
    def capture_table_data(data_previous, data):
        if data_previous != data:         
            updated_data = UpdateTableData(data)
            return updated_data
        else:
            return data
   

    #Callback drugiej tabeli. Tak samo jak przy pierwszej, 
    # Ale nie ma wywołania funkcji do zmiany danych. zmiana następuje 
    #tylko w edytowanej komórce 
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
#     app = create_table(6, Skateboard)  
#     app.run_server(debug=True)
