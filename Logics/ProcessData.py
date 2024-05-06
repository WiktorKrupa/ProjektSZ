import json
from Logics import MrpObject


def UpdateTableData(data, data2, TableNume):
    # print (TableNume)
    # if (int(TableNume) == 5):
    
    #     print(data2)
    
    # #dataInJson = json.loads(data)
    # #print(data)

    # #MRP = MrpObject(data)
    
    
    # print (data2)
    # #Słowniki do zmiennych - każda zmienna zawiera kolejny wiersz danych
    # firstRow = data[0]
    # secondRow = data[1]
    # thirdRow = data[2]
    # fourthRow = data[3]
    # fifthRow = data[4]
    # sixthRow = data[5]
    
    # #zapisanie w zmiennej wartosci z pierwszego wiersza, i pierwszego tygodnia
    # week_1_value = firstRow['Week 1']
    
    
    # #zmiana wartości w komórce 
    # #pierwszy wiersz drugi tydzień 
    # #ustawienie wartości week_1_value + 10
    # firstRow['Week 2'] = str(10+ int(week_1_value ))
    # data[0] = firstRow
    
    
    #print(week_1_value)
    
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