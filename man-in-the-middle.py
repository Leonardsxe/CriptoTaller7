import random

"""
base => número entero que se elige de base para los cálculos exponenciales
exp => exponente de la operación
mod => módulo de la operación de exponenciación, después de base^exp, mod toma el resultado
"""
def modulo(base, exp, mod):
    result_final = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1:
            result_final = (result_final * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result_final

def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def R_primitiva(q):
    raices_primitvas = []
    for i in range(2, q):
        if es_primo(i) and pow(i, (q-1)//2, q) != 1:
            raices_primitvas.append(i)
            if len(raices_primitvas) == 10:
                break
    return raices_primitvas

def generar_claves(q, alpha):
    calve_privada = random.randint(2, q-1)
    calve_publica = modulo(alpha, calve_privada, q)

    return calve_publica, calve_privada

q = 65537
primitivas = R_primitiva(q)

print("Raices primitivas encontradas:")
for i, raiz in enumerate(primitivas, 1):
    print(f"Raiz {i} => ", raiz)

alpha = random.choice(primitivas)
print("\nRaiz primitiva seleccionada:", alpha, "\n")

# Generación de claves de Ana y Bob
c_publica_ana, c_privada_ana = generar_claves(q, alpha)
c_publica_bob, c_privada_bob = generar_claves(q, alpha)

print("Clave privada de Ana:", c_privada_ana)
print()

print("Clave privada de Bob:", c_privada_bob)
print()

anonymous_publica_ana = c_publica_ana
anonymous_publica_bob = c_publica_bob

anonymous_privada_ana = random.randint(2, q-1)
anonymous_privada_bob = random.randint(2, q-1)

print("Clave privada del atacante para Ana:", anonymous_privada_ana)
print()

print("Clave privada del atacante para Bob:", anonymous_privada_bob)
print()

c_calculada_anonymous_ana = modulo(anonymous_publica_ana, anonymous_privada_ana, q)
c_calculada_anonymous_bob = modulo(anonymous_publica_bob, anonymous_privada_bob, q)

print("Clave compartida del atacante con Ana:", c_calculada_anonymous_ana)
print("Clave compartida del atacante con Bob:", c_calculada_anonymous_bob)

c_calculada_ana = modulo(anonymous_publica_bob, c_privada_ana, q)
c_calculada_bob = modulo(anonymous_publica_ana, c_privada_bob, q)

print("Clave compartida Ana:", c_calculada_ana)
print("Clave compartida Bob:", c_calculada_bob)
print()

print("Clave pública de Ana:", c_publica_ana)
print("Clave pública del atacante para Ana:", anonymous_publica_ana)
print("Clave pública de Bob:", c_publica_bob)
print("Clave pública del atacante para Bob:", anonymous_publica_bob)

if c_publica_ana == anonymous_publica_ana and c_publica_bob == anonymous_publica_bob:
    print("El atacante pudo inteceptar la clave y mensaje")
else:
    print("El ataque ha fallado")