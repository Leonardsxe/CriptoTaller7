import random

"""
base => numero entero que se elige de base para los calculos exponenciales
exp => exponente de la operacion
mod => modulo de la operacion de exponenciacion, despues de base^exp, mod toma el resultado
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


c_publica_ana, c_privada_ana = generar_claves(q, alpha)
print("Clave publica Ana:", c_publica_ana)
print("Clave privada Ana:", c_privada_ana)
print()

c_publica_bob, c_privada_bob = generar_claves(q, alpha)
print("Clave publica Bob:", c_publica_bob)
print("Clave privada Bob:", c_privada_bob)
print()

c_calculada_ana = modulo(c_publica_bob, c_privada_ana, q)
c_calculada_bob = modulo(c_publica_ana, c_privada_bob, q)

print("Clave compartida Ana:", c_calculada_ana)
print("Clave compartida Bob:", c_calculada_bob)