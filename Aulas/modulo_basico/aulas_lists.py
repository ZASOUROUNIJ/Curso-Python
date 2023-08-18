# Tipo List Mutavel
# Indices de 0 até n-1 assim como negativos -1 pega o ultimo por exemplo
# Fatiamento
# Métodos
#append, insert, pop, clear, extend...

"""
    append - adiciona um item ao final
    insert - adiciona um item no indice escolhido
    pop    - remove do final ou indice escolhido
    del    - apaga um indice
    clear  - limpa a lista
    extend - estende a lista
    + -    - concatena a lista

    
"""
import clear

lista = [10, 20, 30, 40]

#append - adiciona valores ao final da lista
clear.limpar_terminal()
print(f'lista : {lista}')
lista.append(50)
print(f'Append adiciona valor ao final da lista (50) : {lista}')
input()

#pop - remove o ultimo elemento
clear.limpar_terminal()
print(f'lista : {lista}')
lista.pop()
print(f'pop remove ultimo valor (50) : {lista}')
input()
#pop remoção por indice
clear.limpar_terminal()
print(f'lista : {lista}')
lista.pop(0)
print(f'pop Remoção por indice do indice 0(10) {lista}')
input()

#insert
clear.limpar_terminal()
print(f'lista : {lista}')
print(lista)
lista.insert(2,5)
print(f'insert inserindo o valor 5 na posição 2 {lista}')
input()

#del
clear.limpar_terminal()
print(f'lista : {lista}')
del lista[-1]
print(f'del removendo o ultimo indice : {lista}')
input()

# concatenação, extend
clear.limpar_terminal()
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = []

lista_a.extend(lista_b)

print('c'
,lista_c)
print('a',lista_a)














