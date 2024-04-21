
import matplotlib.pyplot as plt

#from ViewModels.TableDisplay import create_table
#from ViewModels.GetInfoVM import MRPApp
import tkinter as tk
from tkinter import messagebox
#from ViewModels .PrettyTableVM import create_table
from ViewModels import PrettyTableVM
from ViewModels.EditableTable import create_table
from Logics.GetSkateboard import getSkate

my_skateboard = getSkate()


#my_skateboard.display_info()


# root = tk.Tk()
# root.geometry("400x200")  
# app = MRPApp(root)
# root.mainloop()
# #root.destroy()


if __name__ == '__main__':
    app =  create_table(6)
    app.run_server(debug=True)






