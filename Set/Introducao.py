#Introducao aos Sets
''' Tem a mesma função dos conjuntos da matematica'''
#Set vazio
s = set()
print(type(s))
print(s)

#Set com elementos
s = {1, 2, 3, 4}
print(type(s))
print(s)

#REGRAS 
#1- Sets não garantem a ordem dos elementos
s = {1, 2, 3, 4}
print(s)
#2- Sets não aceitam elementos duplicados
try:
    s = {1, 2, 3, 4, 4}
    print(s)
except:
    print('Nao pode ter elementos duplicados')

#3- Sets não aceitam elementos mutaveis (apenas tuplas podem ser usadas)
try:
    s = {1, 2, [3, 4]}
    print(s)
except:
    print('Nao pode ter elementos mutaveis')

#4- Sets são iteráveis(for, in, not in)
s = {1, 2, 3, 4}
for i in s:
    print(i)

#5- Sets não possuem indices 
s = {1, 2, 3, 4}
try:
    print(s[0])
except:
    print('Nao tem indices')

#6- Sets não possuem metodos
s = {1, 2, 3, 4}
try:
    s.append(5)
except:
    print('Nao tem metodos')

#Como não possuem indices, para eliminar um valor do Set se usa o próprio valor invés do indice para remover 
s = {1, 2, 3, 4}
s.remove(2)
print(s)

#outra forma de deletar um valor do Set
s = {1, 2, 3, 4}
s.discard(2)
print(s)

#operadores aritmeticos no Set

s = {1, 2, 3, 4}
S2 = {3, 4, 5, 6}

#union - vai mostrar todos os elementos de ambos os Sets
print(s | S2)
print(s.union(S2))

#intersection - vai mostrar apenas os elementos comuns dos Sets
print(s & S2) 
print(s.intersection(S2))

#difference - vai mostrar apenas os elementos do Set da esquerda que não estão no Set da direita
print(s - S2) 
print(s.difference(S2))

#symmetric difference - vai mostrar apenas os elementos que não estão em ambos os Sets
print(s ^ S2) 
print(s.symmetric_difference(S2))

#Adicionar elementos em um Set
s.add(5)
print(s)