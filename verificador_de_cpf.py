# Verificador de CPF!
import os

continuar = 1
while continuar == 1:
    # Recebendo a entrada do CPF:
    cpf_str = input('Entre com um CPF: ')

    cpf_sem_ponto_str = cpf_str.replace('.', '').replace('-', '')

    cpf_repetido = cpf_sem_ponto_str == (cpf_sem_ponto_str[0] * len(cpf_sem_ponto_str))

    # Verificando se a entrada do usuário é válida:
    if not cpf_sem_ponto_str.isdigit():
        print('Digite um CPF para executar a verificação.')
    elif len(cpf_sem_ponto_str) != 11 or cpf_repetido:
        print('O CPF digitado é inválido.')

    else:
            # Verificando o primeiro digito final:
            i = 0
            cpf_remodelado = ''
            while(i < 9):
                cpf_remodelado += cpf_sem_ponto_str[i]
                i += 1

            i = 10
            j = 0
            soma_digitos_cpf_1 = 0
            while(i >= 2):
                soma_digitos_cpf_1 += i * int(cpf_remodelado[j])
                i -= 1
                j += 1

            mult_div_soma_digitos_cpf_1 = (soma_digitos_cpf_1 * 10) % 11

            if mult_div_soma_digitos_cpf_1 > 9:
                resultado_1 = 0
            else: 
                resultado_1 = mult_div_soma_digitos_cpf_1

            if int(cpf_sem_ponto_str[9]) == resultado_1:
                verificador_1 = True
            else: 
                verificador_1 = False

            # Verificando o segundo digito final:
        
            i = 0
            cpf_remodelado = ''
            while(i < 9):
                cpf_remodelado += cpf_sem_ponto_str[i]
                i += 1

            cpf_remodelado += str(resultado_1)

            i = 11
            j = 0
            soma_digitos_cpf_2 = 0
            while(i >= 2):
                soma_digitos_cpf_2 += i * int(cpf_remodelado[j])
                i -= 1
                j += 1

            mult_div_soma_digitos_cpf_2 = (soma_digitos_cpf_2 * 10) % 11

            if mult_div_soma_digitos_cpf_2 > 9:
                resultado_2 = 0
            else: 
                resultado_2 = mult_div_soma_digitos_cpf_2

            if int(cpf_sem_ponto_str[10]) == resultado_2:
                verificador_2 = True
            else: 
                verificador_2 = False

            # Verificando se os digitos finais estão certos e imprimindo o resultado:
        
            if verificador_1 and verificador_2:
                print('O CPF digitado é válido.')
            else:
                print('O CPF digitado é inválido.')

    # Perguntando ao usuário se quer rodar o programa novamente:
    continuar_str = input('[1]Rodar novamente [0]Sair do programa: ')

    # Verificação de entrada:
    if continuar_str.isdigit():
        if int(continuar_str) == 0 or int(continuar_str) == 1:
            continuar = int(continuar_str)
        else:
            print('Você digitou uma opção inválida.')
            continue
    else: 
        print('Você digitou uma opção inválida.')
        continue

# Fim do programa:
os.system('cls')
print('Fim do programa.')
