import json
from Logics import MrpObject


def UpdateTableData(data, data2, TableNume, edited):
    #Funkcja przyjmuje trzy argumenty 
    #data - dane z dużej tabeli
    #data2 - dane z małej tabeli
    #TableNume -numer sekcji 1-5 patrząc od góry
    #edited - czy w tej tabeli dane się zmieniły
    #nazwy zmiennych ofc można pozmieniać 
    
    #Funkcja wywoływana jest 5 razy, po razie dla każdej pary tablic(duża - mała)
    #Rozróżnienie która to tablica jest w zmiennej TableNume
    #Aktualnie tabele są wypełnione 0 także żeby je początkowo wypełnić można
    #zrobić jakieś sprawdzenie, że jeżeli wszystkie komórki to 0, to ustawiamy jakieś wartości,
    #np tak:
    
    #    dataExample = [
    # {'Model': 'Całkowite zapotrzebowanie', 'Week 1': '1', 'Week 2': '11', 'Week 3': '77', 'Week 4': '1', 'Week 5': '2', 'Week 6': '7'}, 
    # {'Model': 'Planowane przyjęcia', 'Week 1': '2', 'Week 2': '22', 'Week 3': '88', 'Week 4': '0', 'Week 5': '7', 'Week 6': '6'}, 
    # {'Model': 'Przewidywane na stanie', 'Week 1': '3', 'Week 2': '33', 'Week 3': '66', 'Week 4': '2', 'Week 5': '6', 'Week 6': '5'},
    # {'Model': 'Zapotrzebowanie netto', 'Week 1': '4', 'Week 2': '44', 'Week 3': '5', 'Week 4': '3', 'Week 5': '5', 'Week 6': '4'},
    # {'Model': 'Planowanie zamówienia', 'Week 1': '5', 'Week 2': '55', 'Week 3': '4', 'Week 4': '3', 'Week 5': '4', 'Week 6': '3'},
    # {'Model': 'Planowane przyjęcie zamówień', 'Week 1': '6', 'Week 2': '66', 'Week 3': '3', 'Week 4': '5', 'Week 5': '3', 'Week 6': '2'}
    # ]
    
    #return data example
    
    # i potem trzeba wykonywać działania jeżeli coś się zmieni w tabeli
    #Poniżej są moje testy i lekki start zaproponowany przez chata GPT.
    
    #dane w "małej" tabeli ustawiane są z góry, w pliku GetSkateboard.py
    
    
    
    print (data2)
    print('\n')
    return data

    #Moje próby z działaniem na zbiorze danych
    print (TableNume)
    if (int(TableNume) == 5):
    
        print(data2)
    
    #dataInJson = json.loads(data)
    #print(data)

    #MRP = MrpObject(data)
    
    
    print (data2)
    #Słowniki do zmiennych - każda zmienna zawiera kolejny wiersz danych
    firstRow = data[0]
    secondRow = data[1]
    thirdRow = data[2]
    fourthRow = data[3]
    fifthRow = data[4]
    sixthRow = data[5]
    
    #zapisanie w zmiennej wartosci z pierwszego wiersza, i pierwszego tygodnia
    week_1_value = firstRow['Week 1']
    
    
    #zmiana wartości w komórce 
    #pierwszy wiersz drugi tydzień 
    #ustawienie wartości week_1_value + 10
    firstRow['Week 2'] = str(10+ int(week_1_value ))
    data[0] = firstRow
    
    
    print(week_1_value)
    
    # Część rozwiązania zaproproponowana przez chat GPT, pokazuje jak można działać na tabelach
    
    params = {item['Labels']: item['Value'] for item in data2}
    
    # Przykładowe obliczenia
    # Przeliczanie przewidywanego na stanie i zapotrzebowania netto
    for item in data:
        if item['Model'] == 'Przewidywane na stanie':
            # Przykład wykorzystuje tylko jedną wartość - potrzebne pełne równanie
            for week in range(1, 7):
                week_str = f'Week {week}'
                previous_week_str = f'Week {week-1}' if week > 1 else None
                if previous_week_str:
                    # Przewidywane na stanie(t) = Przewidywane na stanie(t-1) + Planowane przyjęcia(t) +
                    # Planowane przyjęcie zamówień(t) - Całkowite zapotrzebowanie(t)
                    predicted_on_hand = int(data[2][previous_week_str]) + \
                                        int(data[1][week_str]) + \
                                        int(data[5][week_str]) - \
                                        int(data[0][week_str])
                    data[2][week_str] = predicted_on_hand

        elif item['Model'] == 'Zapotrzebowanie netto':
            # Zapotrzebowanie netto = potrzeby brutto – aktualny zapas – zapas już zamówiony
            for week in range(1, 7):
                week_str = f'Week {week}'
                net_requirements = max(0, int(data[0][week_str]) - int(data[2][week_str]))
                data[3][week_str] = net_requirements

    return data


    # updated_data = [
    #     {key: '1' for key in row.keys()}
    #     for row in data
    # ]
    # return updated_data