import pyautogui
import time  # importa a biblioteca pyautogui e time serve para pausas

time.sleep(3)  # espera 5 segundos para você abrir a tela desejada

print(pyautogui.position())  # mostra a posição atual do mouse

pyautogui.scroll(10000)  # rola a tela para cima (número negativo rola para baixo)