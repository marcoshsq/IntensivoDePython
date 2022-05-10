# Automação de Sistemas e Processos com Python

"""
Desafio: Todos os dias, o nosso sistema atualiza as vendas do dia anterior.

O seu trabalho diário, como analista, é enviar um e-mail para a diretoria, assim que 
começar a trabalhar, com o faturamento e a quantidade de produtos vendidos no dia anterior

Para resolver isso, vamos usar o pyautogui, uma biblioteca de automação 
de comandos do mouse e do teclado

"""

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy(
    "https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing"
)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

time.sleep(5)

# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(x=878, y=676, clicks=2)
time.sleep(2)

# Passo 3: Fazer o download do relatório
pyautogui.click(x=1000, y=919)
pyautogui.click(x=3323, y=406)
pyautogui.click(x=2748, y=1529)
time.sleep(5)

"""
Lendo o arquivo baixado para pegar os indicadores

- Faturamento
- Quantidade de Produtos
"""

# Passo 4: Calcular os indicadores
import pandas as pd

tabela = pd.read_excel(r"C://Users/joaol/Downloads/Vendas - Dez.xlsx")
display(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

"""
Enviar um e-mail pelo gmail
"""

# Passo 5: Entrar no email
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)

# Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=217, y=483)
time.sleep(7)

pyautogui.write("pythonimpressionador+diretoria@gmail.com")
pyautogui.press("tab")  # seleciona o email
# escreve outro email
# tab
# escreve outro email
# tab
pyautogui.press("tab")  # pula pro campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")  # escrever o assunto
pyautogui.press("tab")  # pular pro corpo do email

texto = f"""
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
"""

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# clicar no botão enviar

# apertar Ctrl Enter
pyautogui.hotkey("ctrl", "enter")

"""#### Use esse código para descobrir qual a posição de um item que queira clicar

- Lembre-se: a posição na sua tela é diferente da posição na minha tela
"""

time.sleep(5)
pyautogui.position()
