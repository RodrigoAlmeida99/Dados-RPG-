from random import randint
import time
import PySimpleGUI as sg

class TelaPython:
    def __init__ (self):
        
       #layou
        layout = [
            [sg.Text('Escolha o Dadp')],
            [sg.Checkbox('D4'), sg.Checkbox('D6')],
            [sg.Checkbox('D8'), sg.Checkbox('D12')],
            [sg.Checkbox('D20')],
            [sg.Button('OK')]
        ]

       #jaela
        janela = sg.Window("Dado RPG").layout(layout)


        
        #dados da janela 
        self.button, self.values = janela.Read()
    def Iniciar(self):
         print(self.values)

tela = TelaPython()
tela.Iniciar() 

'''
quantidade_lado = int (input("digite o número de de lados do dados"))

time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")

print(randint(1,quantidade_lado))
'''
