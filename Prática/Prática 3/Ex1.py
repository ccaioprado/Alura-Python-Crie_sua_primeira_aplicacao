#Exercício 1
numeros = [1,2,3,4,5,6,7,8,9,10]

nomes = ['Caio', 'Ryan', 'Prado', 'Sobral']

anos = [2003, 2026]

#Exercício 2

for numero in numeros:
    print(numero)

#Exercício 3
soma = 0 

for numero in numeros:
    if numero % 2 == 1:
        soma = soma + numero

print(soma)

#Exercício 4
for i in range(10,0,-1):
    print(i)

#Exercício 5
numero_tabuada = int(input("Digite um número para a tabuada: "))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f"{numero_tabuada} x {i} = {resultado}")

#Exercício 6
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

#Exercício 7
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")