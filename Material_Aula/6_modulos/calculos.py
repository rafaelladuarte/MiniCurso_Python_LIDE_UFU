# Arquivo: calculos.py
import datetime
import pandas as pd
from time import sleep


def calcular_juros_simples(principal, taxa_de_juros, tempo):
    juros = (principal * taxa_de_juros * tempo) / 100
    return principal + juros


def calcular_juros_compostos(principal, taxa_de_juros, tempo):
    montante = principal * (1 + taxa_de_juros / 100) ** tempo
    return montante - principal


def obter_data_atual():
    data_atual = datetime.datetime.now()
    return data_atual


def criar_dataframe(lista_de_dados):
    df = pd.DataFrame(lista_de_dados)
    return df


def esperar(tempo):
    sleep(tempo)
    print("Esperei por", tempo, "segundos.")
