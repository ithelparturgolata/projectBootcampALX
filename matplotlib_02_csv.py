import pandas as pd
from pandasgui import show
dane = pd.read_csv('log.csv')
gui = show(dane)