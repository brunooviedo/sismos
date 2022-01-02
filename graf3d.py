import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import pandas as pd

# Read data from a csv
df = pd.read_csv("data2.csv")

fig = px.scatter_3d(df, x = 'Latitud', y = 'Longitud', z='Profundidad [Km]')

fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=6),
                     zaxis = dict(nticks=4, range=[300,0],),),
    width=700,
    margin=dict(r=20, l=10, b=10, t=10))

fig2 = px.scatter(df, x='Fecha Local', y="magnitud")


# fig.show()
# fig2.show()

fig.write_html("graf3d.html")
fig2.write_html("magnitud.html")