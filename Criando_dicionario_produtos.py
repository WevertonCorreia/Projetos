dic_produtos = {}

while True:
    nome_prod = input('Digite o nome do produto: ').lower()
    valor_prod = float(input('Digite o valor do produto: '))
    
    if nome_prod and valor_prod == '':
        print('Voce nao digitou nada programa encerrado')
        print(dic_produtos)

    if nome_prod:
        dic_produtos [nome_prod] = [valor_prod]
        print('Adicionado com sucesso')
        print(dic_produtos)

    if valor_prod:
        novo_valor = valor_prod * 1.1
        dic_produtos [nome_prod] = novo_valor
    print(dic_produtos)
