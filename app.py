import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Encabezado principal
st.header('Analisis de vehiculos: Cuadro de mandos interactivo')

# Leer datos desde archivo CSV
car_data = pd.read_csv('vehicles_us.csv')


# Checkbox para histograma
build_histogram = st.checkbox('Mostrar histograma de odometro')

# Cundo el boton se presiona 
if build_histogram:
    st.write('Creacion de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear grafico de histograma con plotly 
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Personalizar el grafico 
    fig.update_layout(title_text='Distribucion del Odometro')

    # Mostrar grafico en la app 
    st.plotly_chart(fig, use_container_width=True)
    
# Checkbox para grafico de dispersion
build_scatter = st.checkbox('Mostrar grafico de dispersion: Precio vs Año')
# Cuando el boton se presiona
if build_scatter:
    st.write('Creacion de un grafico de dispersion: precio vs Año')
    # Crear grafico de dispersion con plotly
    fig2 = go.Figure(data=go.Scatter(x=car_data['model_year'], y=car_data['price'], mode='markers', marker=dict(color='blue', size=5)))
    # Personalizar el grafico
    fig2.update_layout(title_text='Grafico de dispersion: Precio vs Año', xaxis_title='Año', yaxis_title='Precio')
    # Mostrar grafico en la app
    st.plotly_chart(fig2, use_container_width=True)
