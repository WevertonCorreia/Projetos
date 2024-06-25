"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input ('digite um numero: ')

try:
     numero_int = int (numero)
     if numero_int % 2 == 0:
         print (f'O numero {numero_int} e par')
     else:
         print(f'O numero {numero_int} e impar')
except ValueError:
     print('Você nao digitou um numero inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input ('Digite o horario: ')

try:
    hora_int = float(hora)
    if hora_int >= 0 and  hora_int <= 12:
      print('Bom dia ! ')
     
    elif hora_int >=12 and hora_int < 18:
        print ('Boa tarde !')
    
    else:
        print('Boa noite !')
except ValueError:
   print('Você nao digitou nada!')





"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')

try:
    nome_str = str(nome)
    if len(nome_str) <= 1:
        print('Digite mais de uma letra')
    else:
        if len(nome_str) <= 4:
            print("Seu nome é pequeno")
        elif len(nome_str) <= 6:
            print('Seu nome é normal')
        else:
            print('Seu nome é grande')
except ValueError:
    print('Algo deu errado. Tente novamente.')