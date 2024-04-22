import json
from Logics import MrpObject


def UpdateTableData(data):
    
    #dataInJson = json.loads(data)
    #print(data)

    #MRP = MrpObject(data)
    firstRow = data[0]
    secondRow = data[1]
    thirdRow = data[2]
    fourthRow = data[3]
    fifthRow = data[4]
    sixthRow = data[5]
    sevenRow = data[6]
    
    week_1_value = firstRow['Week 1']
    firstRow['Week 2'] = str(10+ int(week_1_value ))
    data[0] = firstRow
    
    
    #print(week_1_value)
    return data

    # updated_data = [
    #     {key: '1' for key in row.keys()}
    #     for row in data
    # ]
    # return updated_data