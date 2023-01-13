# Escreva um programa que converta uma temperatura digitada em °C e converta em °F

celsius = float(input('Digite o valor em Celsius °C: '))

#fahrenheit = 9 * celsius / 5 + 32
fahrenheit = celsius * 1.8 + 32

print('{:.1f}°C equivale a {:.1f}°F'.format(celsius, fahrenheit))