dicionario = {
    'nome': 'Gustavo',
    'idade': 22
}
#len => Retorna o tamanho do dicionário
print('len de dicionario: ', len(dicionario))
#values => Retorna os valores do dicionário
print('values de dicionario: ', dicionario.values())
#keys => Retorna as chaves do dicionário
print('keys de dicionario: ', dicionario.keys())
#items => Retorna oas chaves e valores do dicionário
print('items de dicionario: ', dicionario.items())
#setdefault => Retorna o valor da chave ou adiciona caso ainda nao exista
dicionario.setdefault('peso', 80)
print(dicionario)
#get => Retorna o valor da chave ou mostra um valor padrao caso ainda nao exista
dicionario.get('idade', 15) 

#===================================================

#copy => Retorna uma copia do dicionário
dicionario_copy = dicionario.copy()
dicionario_copy['nome'] = 'Pedro'
print(dicionario_copy)

import copy
#deepcopy => Retorna uma copia profunda do dicionário
dicionario_deepcopy = copy.deepcopy(dicionario)
dicionario_deepcopy['nome'] = 'Joao'
print(dicionario_deepcopy)

#===================================================

#pop => Remove um item do dicionario
dicionario.pop('peso')
print(dicionario)

#popitem => Remove um item aleatorio do dicionario
dicionario.popitem()
print(dicionario)

#update => Atualiza o dicionário
dicionario.update({'idade': 23})
print(dicionario)

dicionario.update(nome='Gustavo', idade=22)
print(dicionario) 

