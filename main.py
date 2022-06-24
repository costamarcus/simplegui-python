import PySimpleGUI as sg
from cotacao import pegar_cotacoes

layout = [
    [sg.Text('Digite o código da moeda', font='24')],
    [sg.InputText(key='nome_cotacao', font='24', pad=(5, 5))],
    [sg.Button('Pegar Cotação', font='22', pad=(10,10)), sg.Button('Cancelar', font='22', pad=(10,10))],
    [sg.Text('', key='texto_cotacao', font='32')],
]

janela = sg.Window('Sistema de cotações', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Pegar Cotação':
        codigo_cotacao = valores['nome_cotacao']
        codigo_cotacao = codigo_cotacao.upper()
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela['texto_cotacao'].update(f'A cotação do {codigo_cotacao} e de R${cotacao} em relação ao BRL')

janela.close()