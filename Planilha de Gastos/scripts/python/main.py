import plotly as plt
import pandas as pd
import openpyxl
from scripts.python import read_data as rd, manage_data as md
from js import console, window

console.log('Rodou o script main.py')

action = window.prompt('O que deseja fazer? [1] Deletar tudo, [2] Deletar última entrada, [3] Deletar por índice, [4] Adicionar a base de dados: ')

md.terminal(action)
console.log(rd.sum_by_type('Comida'))