#Empacotamento e Desempacotamento de dicionarios
'''a, b = 1, 2
a, b  = b, a
print(a, b)'''

#Empacotamento
pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2)
print(b1, b2)

#Desempacotamento

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa = {**pessoa, **dados_pessoa}
print(pessoa_completa)

#args => argumentos não nomeados
#kwargs => argumentos nomeados

def mostra_argumentos_nomeados(*args, **kwargs):
    print('Não nomeados', args)
    print('Nomeados', kwargs)

mostra_argumentos_nomeados(1, 2, 3, nome='Aline', sobrenome='Souza')