#por padrão o sep vem com espaço para separar os argumentos pode ser alterado assim:
print(1, 2, sep="-")
#Por padrão no win o fim de linha quebra assim no linux quebra com o '\n'
# \r\n -> CLRF
# \n -> LF
print(3, 4, end='\r\n')

print('A','B', end="---")
print('C','D')