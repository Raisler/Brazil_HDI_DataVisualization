import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


def load_data(data):
 data=pd.read_csv(data)
 return data

df = load_data('hdi.csv')
st.title('Human Development Index in Brazil')

select = st.sidebar.selectbox('Choose', ['Home', 'Analysis by Year', 'Analysis by State'])

if select == 'Home':

    st.write('That is a dashboard to see the HDI of all states in Brazil, you can see graphics and values!')
    st.write('In soon, more improvements. #Version 1')
    st.write('In the sidebar, choose your option for the better view for you!')
    st.write('Author: Raisler Voigt | suggestions? raisler.dev@gmail.com')
    st.markdown('''<p align="center">
  <a href="https://www.instagram.com/raislervoigt/" target="_blank" rel="noopener noreferrer">Instagram</a> •
  <a href="https://twitter.com/VoigtRaisler" target="_blank" rel="noopener noreferrer">Twitter</a> •
  <a href="https://www.linkedin.com/in/raisler-voigt7/" target="_blank" rel="noopener noreferrer">Linkedin</a> •
  <a href="https://github.com/Raisler" target="_blank" rel="noopener noreferrer">GitHub</a>
</p>''', unsafe_allow_html=True)



if select == 'Analysis by Year':
    
    select1 = st.sidebar.selectbox('Análise por Ano', [2017, 2010, 2000, 1991])

    fig1 = px.scatter(df, x="HDI Health {0}".format(select1), y="HDI Education {0}".format(select1), size="HDI {0}".format(select1), color="UF")
    fig2 = px.histogram(df, x="UF", y = "HDI {0}".format(select1)).update_xaxes(categoryorder='total descending')
    fig3 = px.histogram(df, x="UF", y = "HDI Education {0}".format(select1)).update_xaxes(categoryorder='total descending')
    fig4 = px.histogram(df, x="UF", y = "HDI Health {0}".format(select1)).update_xaxes(categoryorder='total descending')
    fig5 = px.histogram(df, x="UF", y = "HDI Wealth {0}".format(select1)).update_xaxes(categoryorder='total descending')
    fig6 = df[['UF', "HDI Education {0}".format(select1), "HDI Health {0}".format(select1), "HDI Wealth {0}".format(select1)]]
    
    st.write(fig1)
    st.write(fig2)
    st.subheader('HDI Education')
    st.write(fig3)
    st.subheader('HDI Health')
    st.write(fig4)
    st.subheader('HDI Wealth')
    st.write(fig5)
    st.write(fig6)

if select == 'Analysis by State':
    select2 = st.sidebar.selectbox('Choose the State', df['UF'])
    cdf = df
    cdf.index = cdf['UF']
    state = cdf.index == '{}'.format(select2)
    state = cdf[state]
    trans = state.transpose()
    trans = trans.sort_index(ascending = False)
    
    fig1 = px.histogram(x = trans.index, y = trans['{}'.format(select2)]).update_xaxes(categoryorder='total descending')
    fig2 = state.transpose()
    
    st.write(fig1)
    st.write(fig2)
   
