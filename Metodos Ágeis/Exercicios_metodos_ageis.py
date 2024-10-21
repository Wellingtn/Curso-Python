def quiz(perguntas):
    cont_acertos = 0
    for pergunta in perguntas:
        print(f'{pergunta["Pergunta"]}')
        for cont in range(len(pergunta['Opções'])):
            print(f'{cont+1}) {pergunta["Opções"][cont]}')
        try:
            resposta = pergunta['Opções'][int(input('Qual a resposta? '))-1]
            if resposta == pergunta['Resposta']:
                print('Certa resposta!')
                cont_acertos += 1
            else:
                print('Resposta errada!')
        except:
            print('Resposta inválida!')

        print(f'Acertou {cont_acertos} de {len(perguntas)}')
        print('\n','='*50, '\n')


def main(): 
    perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
    
    quiz(perguntas)  


main()