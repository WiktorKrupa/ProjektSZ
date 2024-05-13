from ViewModels.EditableTable import create_table
from Logics.GetSkateboard import getSkate

Skateboard = getSkate()

if __name__ == '__main__':
    app = create_table(6, Skateboard)
    app.run_server(debug=True)
