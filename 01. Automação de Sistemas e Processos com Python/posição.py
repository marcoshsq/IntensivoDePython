def posicao_cursor():
    """Função responsável por
    encontrar a posição do cursor
    na tela.

    Coordenadas x, y.
    """

    import pyautogui
    from time import sleep

    sleep(5)
    print(pyautogui.position())
