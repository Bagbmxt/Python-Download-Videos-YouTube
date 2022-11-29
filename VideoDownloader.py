import PySimpleGUI as sg
from pytube import YouTube

layout = [[sg.Text('Informe o link do video: '), sg.InputText()], # Primeira linha
         [sg.Button('Baixar'), sg.Button('Cancelar')] # Segunda Linha
         ]

janela = sg.Window("VideoDownloader", layout)

while True:
    event, values = janela.read()
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        video = YouTube(values[0])
        video.streams.get_highest_resolution().download()
        sg.popup_ok("Download concluido com Sucesso! ")

janela.close()