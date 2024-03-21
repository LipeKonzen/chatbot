from cupodre import limparterminal
from random import choice

limparterminal()


def limpar(lista, termo = '\n', reposicao = ''):
    lista2 = []
    for c in lista:
        lista2.append(c.replace(termo, reposicao))
    return lista2


def escreverlinhas(arquivo, lista):
    arq = open(arquivo, 'w')
    arq.writelines(lista)
    arq.close()


msgajuda = '''
        \033[1;32m-\033[m Esse chatbot é um experimento. Ao digitar algo, o programa busca por respostas registradas e caso não haja nenhuma, o programa te pedirá para ensiná-lo.

        \033[1;32m-\033[m Quanto mais o programa for usado, mais respostas serão registradas e melhor o programa responderá.
        
        \033[1;32m-\033[m Todas as entradas e respostas são registradas em minúsculo.
        
        \033[1;32m-\033[m Mesmo a menor mudança na frase enviada vai causar o programa a dar uma resposta nova.

        \033[1;32m-\033[m Quando o programa pedir uma nova frase, apenas digite o que ele deve dizer.

        \033[1;32m-\033[m Seta amarela [\033[1;33m>> \033[m] quer dizer que você está iniciando uma conversa/pergunta e está conversando normalmente.
        
        \033[1;32m-\033[m Seta verde [\033[1;32m>> \033[m] quer dizer que você está ensinando uma nova resposta.

        \033[1;32m-\033[m Caso tiver enviado algo errado, você pode digitar "\033[1;31mcancelar\033[m" quando o programa pedir por uma resposta.

        \033[1;32m-\033[m Enquanto estiver conversando, mesmo que o programa tenha uma resposta já registrada, há uma chance de 1/5 de que o programa vai pedir por uma resposta mais adequada para o contexto.
        '''

entradas = open('entradas.txt', 'r')

entradaslista = entradas.readlines()
    
entradas.close()
    
entradaslista2 = limpar(entradaslista)
    
dialogo = open('dialogo.txt', 'r')
    
listadialogo = dialogo.readlines()
    
dialogo.close()
    
listadialogo2 = limpar(listadialogo)

caminho = ''


print('Digite algo para iniciar a conversa ou digite "ajuda" para ver mais informações.')

while True:
    print(f'caminho: {caminho}')
    if len(caminho) > 10:
        caminho = ''
    entrada = str(input('\033[1;33m\n>> ')).lower()
    if entrada == 'ajuda':
        print(msgajuda)
        
    elif entrada in entradaslista2:
        posicao = entradaslista2.index(entrada)
        caminho += f'[{posicao}]'
        print('\033[1;32m\n', listadialogo2[posicao], '\033[m')
        
    else:
        resp = str(input('\033[mNão entendi. Como devo responder a isso?\n\n\033[1;32m>> ')).lower()
        if resp == 'cancelar':
            pass
        else:
            print(f'\033[mCerto. Na próxima vez que for dito "\033[1;33m{entrada}\033[m", vou responder "\033[1;32m{resp}\033[m"')
            entradaslista.append(f'{entrada}\n')
            entradaslista2.append(entrada)
            escreverlinhas('entradas.txt', entradaslista)
            listadialogo.append(f'{resp}\n')
            listadialogo2.append(resp)
            escreverlinhas('dialogo.txt', listadialogo)
            caminho += f'[{entradaslista2.index(entrada)}]'