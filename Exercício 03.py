#Nome: Rafael Rodrigues Przygodzinski
# Início da função metragem_limpeza()
def metragem_limpeza():
    print(83 * '*');
    print(23 * '-', ' Menu 1 de 3 - Metragem da Limpeza', 24 * '-');
    while True:
      try:
        metragemL = int(input('Digite a metragem da casa (m²):'))
        if 30 <= metragemL < 300:
            print('Será necessário(a) um(a) funcionário(a) para a limpeza!')
            return 60 + (0.3 * metragemL)
        elif 300 <= metragemL < 700:
            print('Serão necessários(as) dois(duas) funcionário(a) para a limpeza!')
            return 120 + (0.5 * metragemL)
        else:
            print('Não aceitamos casas com metragem menor que 30² ou maior que 700² !! ')
            continue #VOLTAR PARA O INÌCIO
      except ValueError: # Caso o usuário digitar letras ou números flutuantes irá ocorrer um erro, o except é para evitar que isso aconteça e dar uma dica!
        print('Digite somente números inteiros!')

# FIM da função metragem_limpeza()

# Início da função tipo_limpeza()
def tipo_limpeza():
    print(83 * '*');
    print(23 * '-', ' Menu 2 de 3 - Tipo de Limpeza', 28 * '-');
    while True:
        tipoL = (input('                      OPÇÕES: \n'+
                        'B – Básica - Indicada para sujeiras semanais ou quinzenais; \n'+
                        'C – Completa - Indicada para sujeiras antigas e/ou não rotineiras.\n'+
                        'Selecione digitando as opções desejada:'));
        tipoL = tipoL.upper()
        if tipoL == 'B':
            print('Você selecionou a limpeza Básica!')
            return 1.00
        elif tipoL == 'C':
            print('Você selecionou a limpeza Completa!')
            return 1.30
        else:
            print('Opção Inválida!!')
            continue #VOLTAR PARA O INÌCIO
# FIM da função tipo_limpeza()

# Início da função adicional_limpeza()
def adicional_limpeza():
    print(83 * '*');
    print(23 * '-', ' Menu 3 de 3 - Adicional de Limpeza', 23 * '-');
    acumular = 0
    while True:
        adicionalL = input('------ Deseja mais algum adicional? ------ \n' +
                           '0- Não desejo mais nada (encerrar)\n' +
                           '1- Passar 10 peças de roupas - R$ 10.00\n' +
                           '2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n' +
                           '3- Limpeza de 1 Geladeira/Freezer - R$ 20,00\n' +
                           '>>');
        if adicionalL == '0':
            return acumular
        elif adicionalL == '1':
            acumular += 10
        elif adicionalL == '2':
            acumular += 12
        elif adicionalL == '3':
            acumular += 20
        else:
            print('Digite apenas as opções existentes!!');
# FIM da função adicional_limpeza()

#PROGRAMA PRINCIPAL
print('  Bem-vindo ao Programa de Serviços de limpeza do Rafael Rodrigues Przygodzinski ');
metragem = metragem_limpeza();
tipo = tipo_limpeza();
adicional = adicional_limpeza();
total = (metragem * tipo) + adicional
print('TOTAL: R$ {:.2f} (Metragem: R$ {:.2f} * Tipo: R$ {:.2f} + Adicional {:.2f}) ' .format(total, metragem, tipo, adicional));