import os
import time
from pathlib import Path

import pandas as pd
import pyautogui
from dotenv import load_dotenv

load_dotenv()

LOGIN_URL = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
CSV_PATH = Path(__file__).with_name("produtos.csv")

EMAIL = os.getenv("AUTOMACAO_EMAIL")
PASSWORD = os.getenv("AUTOMACAO_SENHA")

CAMPO_EMAIL_X = int(os.getenv("CAMPO_EMAIL_X", "564"))
CAMPO_EMAIL_Y = int(os.getenv("CAMPO_EMAIL_Y", "401"))
BOTAO_LOGIN_X = int(os.getenv("BOTAO_LOGIN_X", "727"))
BOTAO_LOGIN_Y = int(os.getenv("BOTAO_LOGIN_Y", "568"))
CAMPO_FORM_X = int(os.getenv("CAMPO_FORM_X", "534"))
CAMPO_FORM_Y = int(os.getenv("CAMPO_FORM_Y", "290"))
SCROLL_APOS_CADASTRO = int(os.getenv("SCROLL_APOS_CADASTRO", "5000"))

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True


def validar_configuracao():
    variaveis_obrigatorias = {
        "AUTOMACAO_EMAIL": EMAIL,
        "AUTOMACAO_SENHA": PASSWORD,
    }

    faltando = [nome for nome, valor in variaveis_obrigatorias.items() if not valor]
    if faltando:
        raise ValueError(
            "Defina as variaveis "
            f"{', '.join(faltando)} no arquivo .env antes de executar o script."
        )


def abrir_chrome_e_acessar_sistema():
    os.system("open -a 'Google Chrome'")
    time.sleep(3)

    pyautogui.hotkey("command", "l")
    pyautogui.write(LOGIN_URL, interval=0.05)
    pyautogui.press("enter")
    time.sleep(2)


def fazer_login():
    pyautogui.click(x=CAMPO_EMAIL_X, y=CAMPO_EMAIL_Y)
    pyautogui.write(EMAIL)
    pyautogui.press("tab")
    pyautogui.write(PASSWORD)
    pyautogui.click(x=BOTAO_LOGIN_X, y=BOTAO_LOGIN_Y)
    time.sleep(3)


def carregar_produtos():
    return pd.read_csv(CSV_PATH, sep="\t")


def cadastrar_produtos(tabela):
    for linha in tabela.index:
        pyautogui.click(x=CAMPO_FORM_X, y=CAMPO_FORM_Y)

        pyautogui.write(str(tabela.loc[linha, "codigo"]))
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

        observacao = tabela.loc[linha, "obs"]
        if pd.notna(observacao):
            pyautogui.write(str(observacao))

        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.scroll(SCROLL_APOS_CADASTRO)


def main():
    validar_configuracao()
    tabela = carregar_produtos()
    abrir_chrome_e_acessar_sistema()
    fazer_login()
    cadastrar_produtos(tabela)


if __name__ == "__main__":
    main()
