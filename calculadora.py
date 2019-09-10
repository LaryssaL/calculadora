#Complete as funcoes a seguir

def soma(a, b):
	x = a + b
    	print( "A soma dos parâmetros é: ", x)

def subtrai(a, b):
	x = a - b
    	print( "A subtração dos parâmetros é: ", x)

	
def multiplica(a, b):
	x = a * b
    	print( "A multiplicação dos parâmetros é: ", x)

def divide(a, b):
if (b != 0):
	x = a / b
    	print( "A divisão dos parâmetros é: ", x)
else:
	print("Digite outro número para b diferente de 0. Obrigada")


#Programa principal

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

soma(num1, num2)
subtrai(num1, num2)
multiplica(num1, num2)
divide(num1, num2)

