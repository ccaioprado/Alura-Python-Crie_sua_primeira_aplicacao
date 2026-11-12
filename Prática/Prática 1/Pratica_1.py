print("""
    A
    L
    U
    R
    A
""")

print('Python na Escola de Programação da Alura')

nome = 'Caio'

idade = 23

print(f'Meu nome é {nome} e eu tenho {idade} anos')

pi_arredondado = 3.14

print(f'O valor de pi é: {pi_arredondado}')

#  ----------------- Métodos para arredondar um número ------------------------------------
pi = 3.14159

# Abordagem de f-string
print(f'O valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print('O valor arredondado de pi é:', round(pi, 2))