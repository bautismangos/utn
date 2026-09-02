# ==========================================
# TRABAJO PRÁCTICO N°1 - PYTHON
# Alumno: bautitititi el más pro
# ==========================================

import math

# --- TP1 ACT 1 ---
print("\n--- ACTIVIDAD 1 ---")
print("Hola mundo!")

# --- TP1 ACT 2 ---
print("\n--- ACTIVIDAD 2 ---")
nombre = input("¿Cómo es tu nombre? ")
print(f"Hola {nombre}, bienvenido")

# --- TP1 ACT 3 ---
print("\n--- ACTIVIDAD 3 ---")
nombre_3 = input("¿Cuál es tu nombre? ")
apellido_3 = input("¿Cuál es tu apellido? ")
edad_3 = input("¿Cuántos años tienes? ")
residencia_3 = input("¿Cuál es tu residencia? ")
print(f"Soy {nombre_3} y mi apellido es {apellido_3}, tengo {edad_3} años y vivo en {residencia_3}")

# --- TP1 ACT 4 ---
print("\n--- ACTIVIDAD 4 ---")
radio = float(input("¿Cuál es el radio del círculo? "))
area = math.pi * (radio ** 2)
perimetro = 2 * math.pi * radio 
print("----RESULTADOS----")
print(f"El área es: {area:.2f}")
print(f"El perímetro es: {perimetro:.2f}")

# --- TP1 ACT 5 ---
print("\n--- ACTIVIDAD 5 ---")
segundos = int(input("Dime los segundos: "))
horas = segundos / 3600 
print(f"Eso equivale a {horas:.2f} horas")

# --- TP1 ACT 6 ---
print("\n--- ACTIVIDAD 6 ---")
numero_6 = int(input("Ingresa un número para ver su tabla: "))
for i in range(1, 11):
    resultado = numero_6 * i
    print(f"{numero_6} x {i} = {resultado}")

# --- TP1 ACT 7 ---
print("\n--- ACTIVIDAD 7 ---")
num1_7 = int(input("Coloca el primer número: "))
num2_7 = int(input("Coloca el segundo número: "))
print("---RESULTADOS---")
print(f"Suma: {num1_7 + num2_7}")
print(f"Resta: {num1_7 - num2_7}")
print(f"Multiplicación: {num1_7 * num2_7}")
print(f"División: {num1_7 / num2_7}")

# --- TP1 ACT 8 ---
print("\n--- ACTIVIDAD 8 ---")
print("--- Medición de IMC ---")
peso_8 = float(input("Ingrese su peso en kg: "))
altura_8 = float(input("Ingrese su altura en metros: "))
imc_8 = peso_8 / (altura_8 ** 2)
print("---RESULTADO---")
print(f"Su índice de masa corporal es: {imc_8:.2f}")

# --- TP1 ACT 9 ---
print("\n--- ACTIVIDAD 9 ---")
print("Conversion de Celsius a Fahrenheit")
celsius_9 = float(input("Ingrese los grados Celsius: "))
fahrenheit_9 = (celsius_9 * 9/5) + 32
print(f"Los {celsius_9}°C equivalen a {fahrenheit_9:.2f}°F")

# --- TP1 ACT 10 ---
print("\n--- ACTIVIDAD 10 ---")
num1_10 = float(input("Coloca el primer número: "))
num2_10 = float(input("Coloca el segundo número: "))
num3_10 = float(input("Coloca el tercer número: "))
promedio_10 = (num1_10 + num2_10 + num3_10) / 3 
print("---RESULTADO---")
print(f"El promedio es: {promedio_10:.2f}")