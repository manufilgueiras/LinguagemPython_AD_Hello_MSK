import streamlit as st

import requests
import urllib3
from io import BytesIO
from urllib3 import request
import pandas as pd

import datetime
from datetime import datetime
from datetime import date
import pytz
import time

datetime_br= datetime.now(pytz.timezone('America/Sao_Paulo'))
#t = datetime_br.strftime('%d:%m:%Y %H:%M:%S %Z %z')
current_time = datetime_br.strftime('%d/%m/%Y %H:%M')
c = datetime.now()
D = pd.to_datetime(c,format='%Y-%m-%d')
c = datetime.now()
H = pd.to_datetime(c,format='%Y-%m-%d')
if H.month <10:
  Hoje = str(H.day) + "/0" + str(H.month) + "/" + str(H.year)
  #MES = "0" + str(D.month)
else:
  Hoje = str(H.day) + "/" + str(H.month) + "/" + str(H.year)

MES = D.month


import matplotlib.pyplot as plt
#https://discuss.streamlit.io/t/how-to-draw-pie-chart-with-matplotlib-pyplot/13967/2

# Page setting
st.set_page_config(layout="wide", page_title="Hello_MSK")


#REF: https://www.geeksforgeeks.org/bar-plot-in-matplotlib/

def Grafico_Pizza(Rotulos, Quantias, Legenda, posExplode, LocLEG, Larg = 16, Alt = 9):
    # Rotulos: etiquetamento dos dados
    # Quantias: dados numéricos referente a cada rótulo
    # Legenda: etiquetamento da legenda
    # posExplode: posição na qual se encontra a fatia da pizza que se deseja ressaltar (explodir)
    # LocLEG: Localização onde será posicionada a Legenda do Gráfico (Ref: https://www.geeksforgeeks.org/change-the-legend-position-in-matplotlib/)

    #fig, ax = plt.subplots(figsize =(16, 9))
    fig, ax = plt.subplots(figsize =(Larg, Alt))
    explode = []
    for i in range(len(Rotulos)):
        if i !=posExplode:
            explode.append(0)
        else:
            explode.append(0.1)
    ax.pie(Quantias,
        explode=explode,
        labels=Legenda,
        autopct='%1.1f%%',
        shadow=True, startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(title='Disciplinas',
            loc=LocLEG,
            bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig)
    
#https://www.geeksforgeeks.org/bar-plot-in-matplotlib/
import numpy as np
#!pip install deep_translator
from deep_translator import GoogleTranslator
tradutor = GoogleTranslator(source= "pt", target= "en")
traducao = tradutor.translate("azul")

def Grafico_Barra_Mono(Rotulos, Quantias, Legenda, estilo = 'horizontal', corPT = 'azul',  Larg = 16, Alt = 9):
    #A fazer: mudar conceito para declaracao classes e colocar objetos nos títulos dos eixos para facilitar uso da função

    tradutor = GoogleTranslator(source= "pt", target= "en")
    corEN = tradutor.translate(corPT)

    Vmax = np.array(Quantias)
    max_value = Vmax.max()
    fig, ax = plt.subplots(figsize =(Larg, Alt))
    if estilo == 'horizontal' or 'Horizontal':
      hbars = ax.barh(Rotulos, Quantias, label=Legenda, color = corEN)
    elif estilo == 'vertical' or 'Vertical':
      hbars = ax.bar(Rotulos, Quantias, label=Legenda, color = corEN)
    else:
      hbars = ax.bar(Rotulos, Quantias, label=Legenda, color = corEN)

    ax.set_ylabel('QTD de tarefas por Disciplina')
    ax.set_title('Tarefas por Disciplina')
    ax.legend(title = 'Disciplinas')

    ax.bar_label(hbars, fmt='%d')
    ax.set_xlim(right=max_value+1)  # adjust xlim to fit labels
    st.pyplot(fig)
    
def main():         

    Titulo = '<p style="font-weight: bolder; color:black; font-size: 48px;">Análise dos Dados Hello_MSK</p>'
    st.markdown(Titulo, unsafe_allow_html=True)
    mystyle1 =   '''<style> p{text-align:left;}</style>'''
    st.markdown(mystyle1, unsafe_allow_html=True) 
     
    urlCSV = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSFFYsOgcKvQnAhXuDWGzmeNvTYGg2J-3xvRTibsgui9aYceElOWbe09zj2zKVV42UJENlUfRNVhgDZ/pub?gid=580720259&single=true&output=csv"
    rD = requests.get(urlCSV)
    dataD = rD.content
    db = pd.read_csv(BytesIO(dataD), index_col=0)
    db.columns = ['Tem_Experiencia', 'Linguagens_Conhecidas', 'Grau_Conhecimento', 'Faixa_Etaria', 'Preferencias_Pessoais','Expectativas', 'Nao_gostaria']
    db['Linguagens_Conhecidas'].fillna('', inplace=True)
    db['Grau_Conhecimento'].fillna('', inplace=True)
    db['Expectativas'].fillna('', inplace=True)
    db['Nao_gostaria'].fillna('', inplace=True)
    
    resumoEXP = db["Tem_Experiencia"].value_counts()
    ListaEXP = list(resumoEXP)    
    Sim = ListaEXP[0]
    Nao = ListaEXP[1]
    RotulosEXP = ['Sim', 'Não']
    
    Python = db[db['Linguagens_Conhecidas'].str.contains('Python')]
    JavaGeral = db[db['Linguagens_Conhecidas'].str.contains('Java')]
    JavaScript = db[db['Linguagens_Conhecidas'].str.contains('JavaScript')]
    Java = len(JavaGeral) - len(JavaScript)
    Cgeral = db[db['Linguagens_Conhecidas'].str.contains("C")]
    Cmaismais = db[db['Linguagens_Conhecidas'].str.contains('C\+\+')]
    Ccharp = db[db['Linguagens_Conhecidas'].str.contains("C#")]
    HTML_CSS = db[db['Linguagens_Conhecidas'].str.contains("HTML/CSS")]
    C =  len(Cgeral) - (len(Ccharp)+len(HTML_CSS))
    SQL = db[db['Linguagens_Conhecidas'].str.contains("SQL")]
    Go = db[db['Linguagens_Conhecidas'].str.contains("Go")]
    TypeScript = db[db['Linguagens_Conhecidas'].str.contains("TypeScript")]
    R = db[db['Linguagens_Conhecidas'].str.contains("R ")]
    SHELL = db[db['Linguagens_Conhecidas'].str.contains("SHELL")]
    PHP = db[db['Linguagens_Conhecidas'].str.contains("PHP")]
    Ruby = db[db['Linguagens_Conhecidas'].str.contains("Ruby")]
    SAS = db[db['Linguagens_Conhecidas'].str.contains("SAS")]
    Swift = db[db['Linguagens_Conhecidas'].str.contains("Swift")]
    Dart = db[db['Linguagens_Conhecidas'].str.contains("Dart")]
    Rust = db[db['Linguagens_Conhecidas'].str.contains("Rust")]
    Kotlin = db[db['Linguagens_Conhecidas'].str.contains("Kotlin")]
    Matlab = db[db['Linguagens_Conhecidas'].str.contains("Matlab")]
    Scala = db[db['Linguagens_Conhecidas'].str.contains("Scala")]
    Assembly = db[db['Linguagens_Conhecidas'].str.contains("Assembly")]
    Visual_Basic = db[db['Linguagens_Conhecidas'].str.contains("Visual Basic")]
    Lua = db[db['Linguagens_Conhecidas'].str.contains("Lua")]
    Fortran = db[db['Linguagens_Conhecidas'].str.contains("Fortran")]
    Julia = db[db['Linguagens_Conhecidas'].str.contains("Julia")]
    Ladder_Logic = db[db['Linguagens_Conhecidas'].str.contains("Ladder Logic")]
    Outra = db[db['Linguagens_Conhecidas'].str.contains("Outra, Nenhuma das opções")]
  
    tab1, tab2 = st.tabs(["DataFrame", "Gráficos"])
    with tab1:   
        st.dataframe(db)
        st.divider()
        st.write(db.describe())
    with tab2:  
        st.subheader("Já fiz algum Hello World (Tenho conhecimento prévio de Prog?)")
        st.write(Grafico_Pizza(RotulosEXP, ListaEXP, RotulosEXP, 0, "upper left", 16, 9))
        labels = ['Python', 'Java', 'C++', 'C', 'JavaScript', 'C#', 'SQL','Go','TypeScript','HTML/CSS','R','SHELL','PHP','Ruby','SAS', 'Swift', 'Dart','Rust','Kotlin','Matlab','Scala','Assembly','Visual Basic','Lua','Fortran', 'Julia','Ladder Logic','Outra']
        QTD = [len(Python), Java, len(Cmaismais), C, len(JavaScript), len(Ccharp), len(SQL), len(Go), len(TypeScript), len(HTML_CSS), len(R), len(SHELL), len(PHP), len(Ruby), len(SAS), len(Swift), len(Dart), len(Rust), len(Kotlin), len(Matlab), len(Scala), len(Assembly), len(Visual_Basic), len(Lua), len(Fortran), len(Julia), len(Ladder_Logic), len(Outra)]
        st.subheader("Já tive algum contato com a(s) seguinte(s) linguagens:")
        Grafico_Barra_Mono(labels, QTD, labels, 'Vertical', 'azul', 16, 9)

    st.divider()
    
    Rodape = '<p style="font-weight: bolder; color:DarkBlue; font-size: 16px;">Desenv. por Massaki de O. Igarashi</p>'
    st.sidebar.markdown(Rodape, unsafe_allow_html=True)
    mystyle1 =   '''<style> p{text-align:center;}</style>'''
    st.sidebar.markdown(mystyle1, unsafe_allow_html=True)
    
if __name__ == '__main__':
	main()
