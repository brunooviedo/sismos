import folium
from folium import Map
from folium.map import Popup
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
import pandas as pd


  # Creating a more organized map using clusters
mapa = folium.Map([-24.093570, -69.298989], zoom_start=7,  tiles='Stamen Terrain',)

# leer el archivo csv que contiene los datos de localización
data = pd.read_csv(r'C:\Users\supegeo\data1.csv')

df = data.head(10)

tooltip = "Ubicacion Tranque"



def generate_popup(Hora, Magnitud, Profundidad, referencia):
    return f'''<strong>Hora Local:</strong><br> {Hora}<br><strong>Magnitud:</strong> {Magnitud}<br><strong>Profundidad:</strong> {Profundidad} <strong>Referencia:</strong>{referencia}'''

def generate_color(Magnitud):
    if Magnitud <= 3:
        c_outline, c_fill = '#008f39', '#008f39'
        m_opacity, f_opacity = 0.4, 0.3
    elif Magnitud <= 5:
        c_outline, c_fill = '#ffda79', '#ffda79'
        m_opacity, f_opacity = 0.6, 0.5
    else:
        c_outline, c_fill = '#c0392b', '#e74c3c'
        m_opacity, f_opacity = 1, 1
    return c_outline, c_fill, m_opacity, f_opacity

mc = MarkerCluster()

for _, row in df.iterrows():
# for i in range(len(data)):
    # c_outline, c_fill, m_opacity, f_opacity = generate_color(row['Magnitud'])
    # folium.Circle(
    #     popup = generate_popup(row ['Fecha Local'],row ['Magnitud'], row['Profundidad [Km]'], row['Referencia Geográfica']),
    #     color=c_outline,  # this is the color of the border
    #     fill=True,
    #     fill_color=c_fill,  # fill is inside the circle
    #     opacity=m_opacity,  # this is the alpha for the border
    #     fill_opacity=f_opacity,  # we will make that less opaque so we can see layers
    #     radius=(row['Magnitud'] ** 6) / 3)
    
    mc.add_child(folium.Marker(
        location=[str(row['Latitud']),
        str(row['Longitud'])],
        popup = generate_popup(row ['Fecha Local'],row ['Magnitud'], row['Profundidad [Km]'], row['Referencia Geográfica']),
        clustered_marker=True))
    
mapa.add_child(mc)

folium.Circle(
    radius=200000,
    location=[-24.397486, -69.161143],
    popup="Radio de 200 Kilometros",
    color="red",
    fill=True,
    opacity=0.5,
    fill_opacity=0.1,
    fill_color="red",
).add_to(mapa)

folium.Circle(
    radius=300000,
    location=[-24.397486, -69.161143],
    popup="Radio de 300 Kilometros",
    color="yellow",
    fill=True,
    opacity=0.5,
    fill_opacity=0.1,
    fill_color="yellow",
).add_to(mapa)

folium.Marker(
    [-24.397486, -69.161143], popup="<i>Coordenadas Tranque -24.397486, -72.161143</i>",
    icon=folium.Icon(color="red",icon="home", prefix='fa'),
).add_to(mapa)
    
mapa1 = folium.Map([-24.093570, -69.298989], zoom_start=7,  tiles='Stamen Terrain',)

for _, row in df.iterrows():
# for i in range(len(data)):
        c_outline, c_fill, m_opacity, f_opacity = generate_color(row['Magnitud'])
        folium.Circle(
            location=[row['Latitud'], row['Longitud']],
            popup = generate_popup(row ['Fecha Local'],row ['Magnitud'], row['Profundidad [Km]'], row['Referencia Geográfica']),
            color=c_outline,  # this is the color of the border
            fill=True,
            fill_color=c_fill,  # fill is inside the circle
            opacity=m_opacity,  # this is the alpha for the border
            fill_opacity=f_opacity,  # we will make that less opaque so we can see layers
            radius=(row['Magnitud'] ** 6) / 3
        
    ).add_to(mapa1)
        
folium.Circle(
    radius=200000,
    location=[-24.397486, -69.161143],
    popup="Radio de 200 Kilometros",
    color="red",
    fill=True,
    opacity=0.5,
    fill_opacity=0.1,
    fill_color="red",
).add_to(mapa1)

folium.Circle(
    radius=300000,
    location=[-24.397486, -69.161143],
    popup="Radio de 300 Kilometros",
    color="yellow",
    fill=True,
    opacity=0.5,
    fill_opacity=0.1,
    fill_color="yellow",
).add_to(mapa1)


folium.Marker(
    [-24.397486, -69.161143], popup="<i>Coordenadas Tranque -24.397486, -72.161143</i>",
    icon=folium.Icon(color="red",icon="home", prefix='fa'),
    tooltip=tooltip
).add_to(mapa1)
        
        
mapa1.save('mapa.html')
mapa.save('Cluster_Map.html')
