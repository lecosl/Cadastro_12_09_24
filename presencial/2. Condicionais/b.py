quantidadedeusuarios = int (input("Quantos usuários você deseja cadastrar? "))


#variável
nome = [""] * quantidadedeusuarios
idade = [0] * quantidadedeusuarios
email = [""] * quantidadedeusuarios
usuarios_cadastrados = 0
i = 0


#Função
def exibir_menu():
    print("\n Menu")
    print("1- Cadastra novo usuário")
    print("2- Listar todos os usuários")
    print("3- Sair do sistema")
    return int(input("Escolher uma opção: "))

#inicio do loop principal

#Estrutura de repetição
while True: 
    opcao = exibir_menu() #Chamando função e recebendo na variável opcao dado digitado pelo usuário

    #Estrutura de condição
    if (opcao==1): #Lógica SE para cadastrar novo usuário
            

            if usuarios_cadastrados < quantidadedeusuarios: #verificando se ainda há espaço para mais cadastrsos 

                nome_usuario = input(f"Digite o nome do usuário: ")
                idade_usuario = int(input("Digite o idade do usuário: "))
                email_usuario = input("Digite o email do usuário: ") 

                nome[usuarios_cadastrados] = nome_usuario 
                idade[usuarios_cadastrados] = idade_usuario
                email[usuarios_cadastrados] = email_usuario 

                    
                #Atualiza o número de usuários
                usuarios_cadastrados += 1 #incremento

                print (f"Usuário {nome_usuario}, {idade_usuario}, {email_usuario} foram cadastrados com sucesso! ")

     elif (opcao==2): #Listar os usuários cadastrados
                if usuarios_cadastrados == 0: 
                    print ("Não há usuários cadastrados!")
                else:
                    for i in range(usuarios_cadastrados):
                        print(f"Nome: {nome_usuario[i]} , Idades: {idade_usuario[i]}, Emails: {email_usuario[i]}")

    elif (opcao==3):
                        print ("Saindo do programa...")

    else: 
                        print ("Opção inválida, encerrando programa.")
                        break