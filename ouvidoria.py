import os

menu = """
Ouvidoria.gg

[a] adicionar
[e] excluir
[l] listar
[t] alterar
[s] sair

digite a opção:
"""
mensagens = []

while True:

    opcao = input(menu).lower()
    
    if opcao == "a": #adicionar

        novaMensagem = input("Digite uma nova mensagem para a ouvidoria: ").strip().title()

        if novaMensagem == "": 
                    print(f'Digite uma mensagem válida! ')
                    
        else:
                mensagens.append(novaMensagem)

                print(f'Mensagem enviada!')
    
    elif opcao == "e": #excluir

        if not mensagens: 

                print(f'Não tem mensagens para excluir')
        
        else:
            
            excluirMensagem = input('\ndigite a mensagem que voce deseja excluir: ').strip().title()

            if excluirMensagem in mensagens: 
                mensagens.remove(excluirMensagem)
                print(f'mensagem apagada com sucesso\n')
            else:
                print('A mensagem não foi encontrada')         

    elif opcao == "l": #listar

            numero = 1
            if not mensagens: 
                print("Não existem mensagens para listar")
            else:
                print('============LISTA DE MENSAGENS==============')
                print('\n'.join( mensagens))
                print('==========================================')
            
    elif opcao == "t": #alterar

        if not mensagens:

                print(f'Não existem mensagens para alterar.')
        else:

            try:

                indexAlterar = int(input('\nDigite o índice da mensagem que você quer alterar: '))

            except:
                
                print('a mensagem não foi alterada. \nDigite apenas numero inteiro!')
                continue

            if indexAlterar < 1 or indexAlterar > len(mensagens): #se digitar um indice menor/maior do que a quantidade de indices na lista

                    print("Índice inválido.")
            else:

                    addMensagem = input("Digite a nova mensagem: ").strip().title()

                    if addMensagem == "": 

                        print(f'Digite uma mensagem valida\n')

                    else:
                        mensagens[indexAlterar - 1] = addMensagem

                        print(f'Mensagem alterada com sucesso.')
    
    elif opcao == "q": #sair
        
        os.system('cls' if os.name == 'nt' else 'clear')
        #print('\n' * 2000) 
        #os.system('cls')       
        print('Ouvidoria Finalizada!\n')
        print(f'Obrigado por usar a Ouvidoria!') 
        break

    else:
        print('Opção invalida! Tente novamente.')