# Passo 1: Entrar no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time
import os
import pandas as pd

pyautogui.PAUSE = 0.5

# ----------------------------
# PASSO 1 - Abrir Chrome no Mac
# ----------------------------
os.system("open -a 'Google Chrome'")
time.sleep(3)

# Ir para barra de endereço
pyautogui.hotkey("Cmd")

# Digitar o link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login", interval=0.05)
pyautogui.press("enter")
time.sleep(0.5)

# ----------------------------
# PASSO 2 - Fazer login
# ----------------------------

# Clicar no campo de email (AJUSTAR COORDENADA SE PRECISAR)
pyautogui.click(x=564, y=401)

pyautogui.write("matheuseduard_04@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua_senha_aqui")

# Clicar no botão login (AJUSTAR SE PRECISAR)
pyautogui.click(x=727, y=568)

time.sleep(3)

# ----------------------------
# PASSO 3 - Importar base
# ----------------------------

tabela = pd.read_csv("produtos.csv", sep="\t")


# ----------------------------
# PASSO 4 - Cadastrar produtos
# ----------------------------

for linha in tabela.index:

    pyautogui.click(x=534, y=290)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)
