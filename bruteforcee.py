import time

contraseña = "Ab3"
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros    = "0123456789"
signos     = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~ "
alfabeto = minusculas + mayusculas + numeros + signos

tiempo_inicio = time.time()
intentos = 0
encontrada = False

def generar(intentos_actuales, longitud, actual=""):
    global intentos, encontrada, tiempo_inicio
    if encontrada:
        return
    if len(actual) == longitud:
        intentos += 1
        if actual == contraseña:
            encontrada = True
            tiempo_final = time.time()
            print(f"Contraseña acertada: {actual}")
            print(f"Intentos: {intentos}")
            print(f"Tiempo transcurrido: {tiempo_final - tiempo_inicio:.4f} segundos")
        return
    for c in alfabeto:
        generar(intentos_actuales, longitud, actual + c)

for longitud in range(1, len(contraseña) + 1):
    if encontrada:
        break
    generar(intentos, longitud)
