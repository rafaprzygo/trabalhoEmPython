print('Bem-vindo a sorveteria do Rafael Rodrigues Przygodzinski')
print(48 * '_','Cardápio', 48 * '_');
print('|' + 2 * ' ' + 1 * ' ' + 'Código' + 3 * ' ' + '|' + 2 * ' ' + 5 * ' ' + 'Descrição' + 8 * ' ' + '|' + 2 * ' ' + 'Tamanho P (500ml)' + 2 * ' ' + '|' + 2 * ' ' + 'Tamanho M (1000ml)' + 2 * ' ' + '|' + 2 * ' ' + 'Tamanho G (2000ml)' + 2 * ' ' + '|' + 2 * ' ');
print('|' + 5 * ' ' + 'TR' + 5 * ' ' + '|' + 2 * ' ' + 'Sabores Tradicionais' + 2 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 6.00' + 8 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 10.00' + 8 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 18.00' + 8 * ' ' + '|');
print('|' + 5 * ' ' + 'ES' + 5 * ' ' + '|' + 2 * ' ' + 'Sabores Especiais' + 5 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 7.00' + 8 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 12.00' + 8 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 21.00' + 8 * ' ' + '|');
print('|' + 5 * ' ' + 'PR' + 5 * ' ' + '|' + 2 * ' ' + 'Sabores Premium' + 7 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 8.00' + 8 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 14.00' + 8 * ' ' + '|' + 2 * ' ' + 4 * ' ' + 'R$ 24.00' + 8 * ' ' + '|');
print(106 * '_');

acumular = 0
while True:
    tam = input('1.	Entre com o tamanho do pote de sorvete desejado (P, M, G): ');
    if (tam != 'P') and (tam != 'p') and (tam != 'M') and (tam != 'm') and (tam != 'G') and (tam != 'g'):
        print('Opção inválida. O tamanho digitado não existe!');
        continue # se digitar algo invalído, voltará para o começo do While

    cod = input('2.	Entre com o código do sorvete desejado (TR, ES, PR): ');
    if (cod != 'TR' and cod != 'tr' and cod != 'ES' and cod != 'es' and cod != 'PR' and cod != 'pr'):
        print('Opção inválida. O código digitado não existe!');
        continue # se digitar algo invalído, voltará para o começo do While

    if (cod == 'tr' or cod == 'TR') and (tam == 'p' or tam == 'P'):
        print('Você escolheu o Sabor Tradicional, tamanho P de R$ 6.00.');
        acumular = acumular + 6.00 #Valor da variavel que é 0 + o valor do sorvete.

    elif (cod == 'tr' or cod == 'TR') and (tam == 'm' or tam == 'M'):
        print('Você escolheu o Sabor Tradicional, tamanho M de R$ 10.00.')
        acumular = acumular + 10.00

    elif (cod == 'tr' or cod == 'TR') and (tam == 'g' or tam == 'G'):
        print('Você escolheu o Sabor Tradicional, tamanho G de R$ 18.00.')
        acumular = acumular + 18.00

    elif (cod == 'es' or cod == 'ES') and (tam == 'p' or tam == 'P'):
        print('Você escolheu o Sabor Especial, tamanho P de R$ 7.00.')
        acumular = acumular + 7.00

    elif (cod == 'es' or cod == 'ES') and (tam == 'm' or tam == 'M'):
        print('Você escolheu o Sabor Especial, tamanho M de R$ 12.00.')
        acumular = acumular + 12.00

    elif (cod == 'es' or cod == 'ES') and (tam == 'g' or tam == 'G'):
        print('Você escolheu o Sabor Especial, tamanho G de R$ 21.00.')
        acumular = acumular + 21.00

    elif (cod == 'pr' or cod == 'PR') and (tam == 'p' or tam == 'P'):
        print('Você escolheu o Sabor Premium, tamanho P de R$ 8.00.')
        acumular = acumular + 8.00

    elif (cod == 'pr' or cod == 'PR') and (tam == 'm' or tam == 'M'):
        print('Você escolheu o Sabor Premium, tamanho M de R$ 14.00.')
        acumular = acumular + 14.00

    elif (cod == 'pr' or cod == 'PR') and (tam == 'g' or tam == 'G'):
        print('Você escolheu o Sabor Premium, tamanho G de R$ 24.00.')
        acumular = acumular + 24.00

    mais = (input('Deseja pedir mais alguma coisa? (SIM/NAO)'));
    mais = mais.upper() #Maiúscula ou Minúscula
    if (mais == 'SIM'):
        continue
    else:
        print('O valor a ser pago é : R$ {:.2f}'.format(acumular))
        break # Encerrar programa.