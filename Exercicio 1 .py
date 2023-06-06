# Quantidade	                         Custo de embalagem para frete
#0 <= quantidade < 11	                 R$ 30.00
#11 <= quantidade < 101	                 R$ 60.00
#101 <= quantidade < 1001	             R$ 120.00
#quantidade >= 1001	                     R$ 240.00

print('Bem-Vindo a loja do Rafael Rodrigues Przygodzinski!'); #MeuNome
valor = float(input('Entre com o valor do produto:'));
qtd = int(input('Entre com a quantidade desse produto:'));
total = (valor * qtd)
f1 = 30 #frete
f2 = 60
f3 = 120
f4 = 240

if (0 <= qtd < 11):
    valorfinal = total + f1
    frete = valorfinal - total #valorfinal - total vai dar o valor do frete.
elif (11 <= qtd < 101):        # elif == else+if
    valorfinal = total + f2
    frete = valorfinal - total
elif (101 <= qtd < 1001):
    valorfinal = total + f3
    frete = valorfinal - total
else: #senão        -          Se o valor for maior ou igual a 1001, entra nesse else. (Mesmo que elif (qtd >= 1001): )
    valorfinal = total + f4
    frete = valorfinal - total

print('O valor sem frete foi: R${:.2f}' .format(total));
print('O valor com frete foi: R${:.2f}  (frete de R${:.2f})' .format(valorfinal, frete));