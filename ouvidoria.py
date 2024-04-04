import os
mensagens = []
def menu():
    return input( """
===============MENU==============
    [a] adicionar
    [e] excluir
    [l] listar
    [t] alterar
    [s] sair
================================  
escolha uma opção: 
    """).strip().lower()

def adicionar():
    global mensagens
    novaMensagem = input("Digite uma nova mensagem para a ouvidoria: ").strip().title()

    if novaMensagem: 
        mensagens.append(novaMensagem)

        print(f'Mensagem enviada!')
                        
    else:
        print(f'Digite uma mensagem válida! ')

def excluir():
    global mensagens
    if not mensagens: 

        print(f'Não tem mensagens para excluir')
        
    else:
            
        excluirMensagem = input('\ndigite a mensagem que voce deseja excluir: ').strip().title()

        if excluirMensagem in mensagens: 
            mensagens.remove(excluirMensagem)
            print(f'mensagem apagada com sucesso\n')
        else:
            print('A mensagem não foi encontrada') 

def listar():
    global mensagens
    if not mensagens: 
        print("Não existem mensagens para listar")
    else:
        print('============LISTA DE MENSAGENS==============')
        #print('\n'.join( mensagens))
        for indice, mensagem in enumerate(mensagens, start=1):
            print(f'{indice} -- mensagem --> {mensagem}')
        print('==========================================')

def alterar():
    global mensagens
    if not mensagens:

                print(f'Não existem mensagens para alterar.')
    else:

        try:

            indexAlterar = int(input('\nDigite o índice da mensagem que você quer alterar: '))
            
            if indexAlterar < 1 or indexAlterar > len(mensagens):

                print('indice invalido')
                #se digitar um indice menor/maior do que a quantidade de indices na lista 
            else:
                addMensagem = input("Digite a nova mensagem: ").strip().title()

                if not addMensagem : 

                    print(f'Digite uma mensagem valida\n')

                else:
                    mensagens[indexAlterar - 1] = addMensagem

                    print(f'Mensagem alterada com sucesso.')
        except:
                
            print('a mensagem não foi alterada. \nDigite apenas numero inteiro!')

        

            print("Índice inválido.")

def sair():
    os.system('cls' if os.name == 'nt' else 'clear')
        #print('\n' * 2000) 
        #os.system('cls')       
    print('Ouvidoria Finalizada!\n')
    print(f'Obrigado por usar a Ouvidoria!') 

def main():
    
    while True:

        opcao = menu()

        if opcao == "a":
            adicionar()

        elif opcao == "e":
            excluir()
        elif opcao == "l":
            listar()
        elif opcao == "t": 
            alterar()
        elif opcao == "s":
            sair()
        else:
            print('Valor invalido!')

main()