import pandas as pd

df = pd.read_csv('log.csv')


print(df[:3])


#dataframe
# data = pd.read_csv ("cenlutyutf8.csv", sep=";")
#
# print (data)


# df = pd.read_csv("cenlutyutf8.csv", sep=";")



# import pandas as pd
#df = pd.read_csv('http://analityk.edu.pl/wp-content/uploads/2020/01/Countries.csv')
# data = pd.read_csv (r'D:\projectBootcampALX\cenlutyutf8.csv')
# df = pd.DataFrame(data, columns= ['answered','callee_last_name'])
# print (df)
# import tkinter as tk
# from tkinter import filedialog
# import pandas as pd
#
# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=300, height=300, bg='lightsteelblue2', relief='raised')
# canvas1.pack()
#
# def getCSV():
#     global df
#     import_file_path = filedialog.askopenfilename()
#     df = pd.read_csv(import_file_path)
#     print(df)
#
# browseButton_CSV = tk.Button(text="      Import CSV File     ", command=getCSV, bg='green', fg='white',
#                              font=('helvetica', 12, 'bold'))
# canvas1.create_window(150, 150, window=browseButton_CSV)
#
# root.mainloop()