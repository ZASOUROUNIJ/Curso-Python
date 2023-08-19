import os

def l_t():
    sistema = os.name
    if sistema == 'posix':
        os.system('clear')  # Limpar terminal em sistemas Unix-like
    elif sistema == 'nt':
        os.system('cls')    # Limpar terminal no Windows
    else:
        pass  # Caso o sistema não seja reconhecido

def pausa():
    input()
