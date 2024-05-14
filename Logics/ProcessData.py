import json
from Logics import MrpObject
from typing import List, Dict

def UpdateGHP(data_ghp, data_time_stock, data_previous_ghp, data_previous_time_stock):
        
    na_stanie = data_time_stock[1].get('Value', 0)
    data_ghp[2]['Week 1'] = na_stanie

    
    # Uzupełnienie danych dla wszystkich tygodni
    for week in range(2, 7):
        if f'Week {week}' not in data_ghp[0]:
            data_ghp[0][f'Week {week}'] = 0
        if f'Week {week}' not in data_ghp[1]:
            data_ghp[1][f'Week {week}'] = 0
        if f'Week {week}' not in data_ghp[2]:
            data_ghp[2][f'Week {week}'] = 0
            
    # Dostępne (t) = Dostępne (t-1) - Przewidywany popyt (t) + Produkcja (t)
    for week in range(2, 7):
        prev_dostepne = int(data_ghp[2][f'Week {week-1}'])
        przewidywany_popyt = int(data_ghp[0][f'Week {week}'])
        prod = int(data_ghp[1][f'Week {week}'])
        dostepne = prev_dostepne - przewidywany_popyt + prod
        data_ghp[2][f'Week {week}'] = str(dostepne)
    
    updated_data_ghp = data_ghp
    updated_data_time_stock = data_time_stock
    return updated_data_ghp, updated_data_time_stock

def UpdateTableData(data: List[Dict[str, str]], data2: List[Dict[str, str]], TableNume: str, updated_data_ghp: List[Dict[str, str]], updated_data_time_stock: List[Dict[str, str]]) -> List[Dict[str, str]]:
    bom = data2[2].get('Value', 0)
    # Aktualizacja danych w zależności od tabeli (BOM 0 - Skateboard, BOM 1 - Wheels, Tracks, Deck, BOM 2 - Plywood)
    # Aktualizacja dla komponentów z BOM 0:
    if bom == 0:
        na_stanie_skateboard = int(data2[3].get('Value', 0))
        czas_realizacji_bom0 = int(data2[0].get('Value', 0))
        data[2]['Week 1'] = na_stanie_skateboard
        
        for week in range (2,7):
            
            #netto
            if int(data[0][f'Week {week}']) > 0:
                data[3][f'Week {week}'] += int(data[0][f'Week {week}']) - int(data[2][f'Week {week}'])
            
            #planowane przyjęcie zamówień
            if int(data[5][f'Week {week}']) < int(data2[1].get('Value', 0)) and int(data[3][f'Week {week}']) > 0:
                data[5][f'Week {week}'] += int(data2[1].get('Value', 0))
            elif int(data[3][f'Week {week}']) == 0:
                data[5][f'Week {week}'] == 0
            else:
                data[5][f'Week {week}'] = 10
                for x in range (week, 7):
                    data[5][f'Week {week + x}'] = 10
                    x -= 1
                    
            #planowane zamówienia
            if week - czas_realizacji_bom0 >=1 and data[3][f'Week {week}'] > 0:
                data[4][f'Week {week - czas_realizacji_bom0}'] += int(data[5][f'Week {week}'])
            else:
                data[4][f'Week {week}'] = 0
            
            #przewidywane na stanie
            data[2][f'Week {week}'] = int(data[2][f'Week {week - 1}']) + int(data[1][f'Week {week - 1}']) + int(data[5][f'Week {week}']) - int(data[0][f'Week {week}'])
            
            #netto again
            if int(data[2][f'Week {week}']) < 0:
                data[3][f'Week {week + 1}'] = int(data[3][f'Week {week}']) - int(data2[1].get('Value', 0))

    elif bom == 1:
        # Aktualizacja dla komponentów z BOM 1: Wheels, Tracks, Deck
        # Tutaj wykonaj odpowiednie operacje na danych dotyczących Wheels, Tracks, Deck
        pass
    elif bom == 2:
        # Aktualizacja dla Plywood (BOM 2)
        # Tutaj wykonaj odpowiednie operacje na danych dotyczących Plywood
        pass

    # Zwróć zaktualizowane dane
    return data


