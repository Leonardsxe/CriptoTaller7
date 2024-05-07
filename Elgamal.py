import random

# Función para encontrar raíces primitivas módulo q
def primitive_root(q):
    roots = []
    for g in range(2, q):
        if pow(g, (q - 1), q) == 1:
            roots.append(g)
    return roots

# Función para generar una clave privada y pública
def generate_keys(q):
    g = random.choice(primitive_root(q))
    a = random.randint(2, q - 2)
    h = pow(g, a, q)
    return (g, q, h), a

# Función para cifrar un mensaje
def encrypt(msg, public_key):
    g, q, h = public_key
    k = random.randint(2, q - 2)
    s = pow(h, k, q)
    p = pow(g, k, q)
    ciphertext = []
    for char in msg:
        ciphertext.append((ord(char) * s) % q)
    return ciphertext, p

# Función para descifrar un mensaje
def decrypt(ciphertext, p, private_key):
    g, q, _ = private_key
    h = pow(p, private_key[1], q)
    plaintext = ''
    for char in ciphertext:
        plaintext += chr((char * pow(h, q - 2, q)) % q)
    return plaintext

# Función para encontrar la palabra de verificación
def find_verification_word(q):
    word = ''
    while True:
        word = input("Ingrese una palabra de verificación: ")
        ascii_sum = sum(ord(char) for char in word)
        if ascii_sum < q:
            break
        else:
            print("La suma ASCII de la palabra debe ser menor que q.")
    return word

# Main
if __name__ == "__main__":
    q = 4294967311
    public_key, private_key = generate_keys(q)
    print("Clave pública:", public_key)
    print("Clave privada:", private_key)

    verification_word = find_verification_word(q)
    print("Palabra de verificación:", verification_word)

    ciphertext, p = encrypt(verification_word, public_key)
    print("Mensaje cifrado:", ciphertext)
    plaintext = decrypt(ciphertext, p, private_key)
    print("Mensaje descifrado:", plaintext)
