import pyautogui
import pyperclip
import time


def posicao_cursor():
    """Função responsável por
    encontrar a posição do cursor
    na tela.

    Coordenadas x, y.
    """
    time.sleep(5)
    print(pyautogui.position())


def abrir_navegador():
    """Abrir o navegador caso ele não
    esteja aberto."""

    browser = str(input("Qual browser abrir? \n").lower())
    pyautogui.press("win")
    pyautogui.write(browser)
    pyautogui.press("enter")


def copiar_colar():
    """Recebe um texto e cola."""

    texto = str(input("Insira o texto: \n"))
    pyperclip.copy(texto)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(5)


# Essa linha é para escolher o perfil do usuário do google chrome.
# pyautogui.click(x=592, y=317, clicks=1)
