x = float(input('Digite o valor de X: '))

y = float(input('Digite o valor de Y: '))

if x and y > 0:
    print('O ponto está no primeiro quadrante')
elif x < 0 and y > 0:
    print('O ponto está no segundo quadrante')
elif x and y < 0:
    print('O ponto está no terceiro quadrante')
else:
    print('O ponto está localizado no eixo ou origem')