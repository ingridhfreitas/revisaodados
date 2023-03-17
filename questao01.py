#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

f = float (input("Informe a temperatura em ºF:"))
c = 5 * ((f - 32) / 9)

print("A temperatura de {} ºF corresponde a {} ºC" .format(f, c))