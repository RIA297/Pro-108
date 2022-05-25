import  plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv
df=pd.read_csv("data (1).txt")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=True)
fig.show()
