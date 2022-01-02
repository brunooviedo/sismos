import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

import pandas as pd

# Read data from a csv
df = pd.read_csv("data2.csv")

fig = px.scatter_3d(df, x = 'Latitud', y = 'Longitud', z='Profundidad [Km]', color='magnitud',
                    color_continuous_scale=["blue", "green", "red"], title="Grafica de Profundidad")

fig.update_traces(marker=dict(size=5,
                         line=dict(width=5,
                         color='Black')),
              selector=dict(mode='markers'))

fig.update_layout(
    scene = dict(
        xaxis = dict(nticks=6),
                     zaxis = dict(nticks=4, range=[300,0],),),
    margin=dict(r=20, l=10, b=10, t=10))

fig2 = px.scatter(df, x='Fecha Local', y="magnitud", color='magnitud',
                  color_continuous_scale=["blue", "green", "red"], title="Grafica de Magnitud")

fig2.update_traces(marker=dict(size=8,
                         line=dict(width=1,
                         color='Black')),
              selector=dict(mode='markers'))


# fig.show()
# fig2.show()

fig.write_html("graf3d.html")
fig2.write_html("magnitud.html")