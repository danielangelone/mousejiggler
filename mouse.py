import pyautogui
import time
import random
from pynput import keyboard
import os
import threading

# Desativa a proteção de segurança do PyAutoGUI
pyautogui.FAILSAFE = False

movendo = True  # Variável para controlar o movimento do mouse
programa_rodando = True  # Variável para controlar o loop principal

def on_press(key):
    global movendo, programa_rodando
    try:
        if key.char == 'm':  # Verifica se a tecla 'M' foi pressionada
            movendo = not movendo  # Alterna o estado de movimento
            print("Movimento do mouse " + ("pausado." if not movendo else "retomado."))
    except AttributeError:
        if key == keyboard.Key.esc:  # Verifica se a tecla 'Esc' foi pressionada
            print("Saindo do programa...")
            programa_rodando = False  # Altera a variável para encerrar o loop principal
            listener.stop()  # Para o listener
            os._exit(0)  # Encerra o programa completamente

# Inicia o listener para a tecla
listener = keyboard.Listener(on_press=on_press)
listener.start()

print("Pressione 'M' para pausar ou retomar o movimento do mouse.")
print("Pressione 'Esc' para sair do programa.")

while programa_rodando:  # Loop principal controlado pela variável programa_rodando
    if movendo:
        # Move o mouse para uma posição aleatória na tela
        x = random.randint(0, 1440)  # Ajuste a largura da tela
        y = random.randint(0, 810)  # Ajuste a altura da tela
        pyautogui.moveTo(x, y, duration=0.5)  # Move com uma duração de 0.5 segundos
        time.sleep(1)  # Espera 1 segundo antes de mover novamente
