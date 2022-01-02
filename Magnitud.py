import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import pandas as pd

# Read data from a csv
df = pd.read_csv("data2.csv")


fig = px.scatter(df, x='Fecha Local', y="magnitud")

fig.show()