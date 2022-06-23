import PySimpleGUI as sg
from cotacao import pegar_cotacoes

layout = [
    [sg.Text('Digite o código da moeda')],
    [sg.InputText(key='nome_cotacao')],
    [sg.Button('pegar cotação'), sg.Button('cancelar')],
    [sg.Text('', key='texto_cotacao')],
]

janela = sg.Window('Sistema de cotações', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'cancelar':
        break
    if evento == 'pegar cotação':
        codigo_cotacao = valores['nome_cotacao']
        codigo_cotacao = codigo_cotacao.upper()
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].update(f'A cotação do {codigo_cotacao} e de R${cotacao}')

janela.close()