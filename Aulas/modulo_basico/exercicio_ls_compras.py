"""

Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista

"""
import clear


lista_compras = []
opcao = ''
indice = int
indice_str = ''
while True:
    clear.l_t()
    print("Selecione uma opção")
    opcao = input("[i]nserir [a]pagar [l]istar: ")

    if opcao == 'i':
        clear.l_t()
        lista_compras.append(input("Inserir item para comprar : "))
        print(f'{lista_compras[-1]} Inserido com sucesso!')
        clear.pausa()

    elif opcao == 'a':
        clear.l_t()
        for item in enumerate(lista_compras):
            numero, nome = item
            print (numero, nome)
        indice_str = (input("Indice para remover : "))
        try:
            indice = int(indice_str)
            del lista_compras[indice]
            print(f'{indice} removido com sucesso!')
        except ValueError:
            print('Indice deve ser um número inteiro')
        except IndexError:
            print('Indice não encontrado')
        except Exception:
            print('Sisi fufu')
        clear.pausa() 

    elif opcao == 'l':
        if not lista_compras:
            print('lista encontra-se vazia.')
            clear.pausa()
        else:
            for item in enumerate(lista_compras):
                numero, nome = item
                print (numero, nome)
            clear.pausa()

    elif opcao == 's':
        break

    else:
        clear.l_t()