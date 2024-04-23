import json
from Logics import MrpObject


def UpdateTableData(data):
    
    
    #dataInJson = json.loads(data)
    #print(data)

    #MRP = MrpObject(data)
    
    
    
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
    
    
    #print(week_1_value)
    return data

    # updated_data = [
    #     {key: '1' for key in row.keys()}
    #     for row in data
    # ]
    # return updated_data