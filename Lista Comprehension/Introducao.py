#Lista Normal
lista = []
for i in range(1, 11):
    lista.append(i)
print(lista)

#Lista Comprehension
lista = [i for i in range(1, 11)]
'''o i antes do for é o valor que será adicionado na lista
se tivesse um numero antes do for, seria o valor que seria adicionado na lista
o numero que o for está sendo iterado'''
print(lista)

#Exemplo 
lista = [i
    if i % 2 == 0 
    else i * 2
    for i in range(1, 11)]
print(lista)

#Ordem da lista Comprehension
#1 - Numero a ser adicionado na variável ou lista
#2 - Condição
#3 - Else
#4- Laço FOR
