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
df = pd.DataFrame(np.random.randn(100, 3), columns = ['A', 'B', 'C'])
df = df.stack().reset_index().iloc[:, ::-1]
df.columns = ['Value', 'Column Name', 'Index']

#繪圖
fig = px.scatter(df, x = 'Index', y = 'Value', color = 'Column Name')
fig.show()

