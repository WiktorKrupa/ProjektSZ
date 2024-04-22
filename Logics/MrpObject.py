class MrpObject:
    def __init__(self, data):
        for row in data:
            model_name = row['Model'].replace(' ', '')  
            setattr(self, model_name, MrpDataRow(row))


class MrpDataRow:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key.replace(' ', ''), value)