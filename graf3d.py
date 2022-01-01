import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import pandas as pd

# Read data from a csv
df = pd.read_csv(r"data2.csv")

fig = px.scatter_3d(df, x = 'Latitud', y = 'Longitud', z='Profundidad [Km]')



#fig.show()

fig.write_html("graf3d.html")