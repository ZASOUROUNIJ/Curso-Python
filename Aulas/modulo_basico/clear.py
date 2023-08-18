import os

def limpar_terminal():
    sistema = os.name
    if sistema == 'posix':
        os.system('clear')  # Limpar terminal em sistemas Unix-like
    elif sistema == 'nt':
        os.system('cls')    # Limpar terminal no Windows
    else:
        pass  # Caso o sistema não seja reconhecido