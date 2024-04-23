Instalacja "dash"

    pip install dash

Główny plik -> App.py
Po uruchomienu ( i zainstaliwaiu dash) w terminalu pojawia się link do tabeli

# Działanie programu: #
## Utworzenie obiektu deskorolka ##
    Skateboard = getSkate()
funkcja **Logics.GetSkateboard.getSkate()** tworzy obiekt klasy **Skateboard** (Models.SkateboardModel)

Obiekt **Skateboard** posiada atrybuty
- bomLevel - poziom BOM
- batchSize - wielkość partii
- leadTime - czas realizacji
- inStock - na stanie
- quantity - ilość 

Oraz obiekty które również posiadają powyższe atybuty
- wheels - koła (Models.WheelsModel)
- tracks - traki (Models.TracksModel)
- deck - blat (Models.DeckModel)
- plywood - płyta (Models.PlywoodModel)

Funkcja **getSkate()** wywoływana w **App.py** tworzy obiekt **Skateboard** i przypisuje mu atrybuty.

Po wywołaniu funkcji możemy odnosić się do atrybutów deskorolki
    
    Skateboard = getSkate()
    print(Skateboard.batchSize)
output:
    
    10


Oraz do atrybutów obiektów deskorolki

    Skateboard = getSkate()
    print(Skateboard.tracks.leadTime)

output:

    3

## Tworzenie Interaktywnej Tabeli ##

Funkcja **ViewModels.EditableTable.createTable** przyjmuje dwa argumenty
- NumberOfColumns - Ilość tygodni do wyświetlenia w tabeli
- Skatebord - Utworzony wcześniej obiekt klasy **Skateboard** 

Wywoływana jest w **App.py**

    app = create_table(6, Skateboard)

funkcja tworzy tabelę (dokładny opis w pliku EditableTable.py) i jeżei dane w tabeli zostały zmienione wywołuje funkcję **UpdateTableData**

## Procesowanie danych ##
Logics.ProcessData.UpdateTableData

funcja przyjmuje dane z tabeli, i zwraca dane które mają być wyświetlone w tabeli.

zmienna dane to lista słowników

Przykładowe dane ze zmiennej 'dane':

    [{'Model': 'Całkowite zapotrzebowanie', 'Week 1': '1', 'Week 2': '11', 'Week 3': '77', 'Week 4': '1', 'Week 5': '2', 'Week 6': '7'}, 
    {'Model': 'Planowane przyjęcia', 'Week 1': '2', 'Week 2': '22', 'Week 3': '88', 'Week 4': 0, 'Week 5': '7', 'Week 6': '6'}, 
    {'Model': 'Przewidywane na stanie', 'Week 1': '3', 'Week 2': '33', 'Week 3': '66', 'Week 4': '2', 'Week 5': '6', 'Week 6': '5'},
     {'Model': 'Zapotrzebowanie netto', 'Week 1': '4', 'Week 2': '44', 'Week 3': '5', 'Week 4': '3', 'Week 5': '5', 'Week 6': '4'},
      {'Model': 'Planowanie zamówienia', 'Week 1': '5', 'Week 2': '55', 'Week 3': '4', 'Week 4': '3', 'Week 5': '4', 'Week 6': '3'},
    {'Model': 'Planowane przyjęcie zamówień', 'Week 1': '6', 'Week 2': '66', 'Week 3': '3', 'Week 4': '5', 'Week 5': '3', 'Week 6': '2'}]

Aktualnie funkcja **UpdateTableData** jest jedynie do celów testowych

Funkcja zawiera aktualnie przykładowe działania na zbiorze danych