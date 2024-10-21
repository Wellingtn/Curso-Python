# Definição de uma função lambda que recebe dois parâmetros, x e y, e retorna a soma de x e y.
'''A Função lambda pode ser usada para reduzir a escrita de funcões de uma vez por vez. '''

#Exemplo de Função normal
def soma(x, y):
    return x+y

#Exemplo de Função lambda
soma = lambda x, y: x+y

#lambda => função anonima (mesma coisa que def)
#A função lambda não tem parênteses, pois é uma função anonima
#x, y => parametros
#x+y => corpo da função

#Exemplo de Função lambda
soma = lambda x, y: x+y
print(soma(1, 2))

#Exemplo de Função Normal
def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

#Transformando a Função normal em Função lambda
cria_multiplicador = lambda mult: lambda num: num * mult