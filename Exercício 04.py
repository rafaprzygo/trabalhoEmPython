#Nome: Rafael Rodrigues Przygodzinski
# ---------- Início das variáveis Globais ---------- #
lista_funcionario = []
id_funcionario = 0

# ---------- Fim das Variáveis Globais ---------- #

# ---------- Início de cadastrar_funcionario() ---------- #
def cadastrar_funcionario(id):
    print(76 * '*');
    print(24 * '-', 'MENU CADASTRAR FUNCIONÁRIO', 24 * '-');
    print('Código do Funcionário: {}'.format(id));
    nome = input('Digite o NOME do funcionário:');
    setor = input('Digite o SETOR do funcionário:');
    salario = int(input('Digite o SALÁRIO do funcionário R$:'));
    dicionario_funcionario = {'id'      : id,
                              'nome'    : nome,
                              'setor'   : setor,
                              'salario' : salario}
    lista_funcionario.append(dicionario_funcionario.copy())
# ---------- Fim de cadastrar_funcionario() ---------- #

# ---------- Início de consultar_funcionario() ---------- #
def consultar_funcionario():
    print(76 * '*');
    print(24 * '-', 'MENU CONSULTAR FUNCIONÁRIO', 24 * '-');
    while True:
        opcao_consultar = input('Escolha a opção desejada:\n'+
                                '1 - Consultar todos os Funcionários\n'+
                                '2 - Consultar funcionários por ID\n'+
                                '3 - Consultar funcionários por SETOR\n'+
                                '4 - Retornar\n'+
                                '>>')
        if opcao_consultar == '1':
            for funcionario in lista_funcionario:
                print('----------------------');
                for key, value in funcionario.items():
                    print('{}: {}'.format(key,value));
                print('----------------------');

        elif opcao_consultar == '2':
            valor_desejado = int(input('Digite o ID do funcionário:'))
            for funcionario in lista_funcionario:
                if funcionario['id'] == valor_desejado:
                    print('----------------------');
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value));
                print('----------------------');
        elif opcao_consultar == '3':
            valor_desejado = input('Digite o SETOR do(s) funcionário(s):')
            for funcionario in lista_funcionario:
                if funcionario['setor'] == valor_desejado:
                    print('----------------------');
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value));
                print('----------------------');

        elif opcao_consultar == '4':
            return
        else:
            print('Opção inválida. Tente novamente!');
            continue  # Volta para o início do laço.

# ---------- Fim de consultar_funcionario() ---------- #

# ---------- Início de remover_funcionario() ---------- #
def remover_funcionario():
    print(76 * '*');
    print(24 * '-', 'MENU REMOVER FUNCIONÁRIO', 24 * '-');
    valor_desejado = int(input('Digite o cógido do funcionário a ser removido:'))
    for funcionario in lista_funcionario:
        if funcionario['id'] == valor_desejado:
            lista_funcionario.remove(funcionario)
            print('Funcionário Removido!');
# ---------- Fim de remover_funcionario() ---------- #

# ---------- INÍCIO DO PROGRAMA PRINCIPAL ---------- #
print('\nBem-Vindo ao Controle de funcionários do Rafael Rodrigues Przygodzinski.');
while True:
    print(76 * '*');
    print(29 * '-', 'MENU PRINCIPAL', 31 * '-');
    opcao_principal = input('Escolha a opção desejada:\n'+
                            '1 - Cadastrar Funcionário\n'+
                            '2 - Consultar Funcionário(s)\n'+
                            '3 - Remover Funcionário\n'+
                            '4 - Sair.\n'+
                            '>>');
    if opcao_principal == '1':
        id_funcionario += 1
        cadastrar_funcionario(id_funcionario)
    elif opcao_principal == '2':
        consultar_funcionario()
    elif opcao_principal == '3':
        remover_funcionario()
    elif opcao_principal == '4':
        break
    else:
        print('Opção inválida. Tente novamente!');
        continue # Volta para o início do laço.

# ---------- FIM DO PROGRAMA PRINCIPAL ---------- #