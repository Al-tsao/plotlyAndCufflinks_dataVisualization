#載入模組
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import iplot
import plotly as py
import cufflinks as cf
import plotly.graph_objects as go
import plotly.express as px

#載入資料
data_canada = px.data.gapminder().query("country == 'Canada'")

#繪圖
fig = px.bar(data_canada, x='year', y='pop')
fig.show()

