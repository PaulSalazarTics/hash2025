# hash_example.py
import hashlib

def generate_hash(text):
    # Crear un objeto hash SHA-256
    hash_object = hashlib.sha256(text.encode())
    # Obtener el hash en hexadecimal
    return hash_object.hexdigest()

# Mensaje original
original_message = "mensaje a ser enviado"

# Generar hash
message_hash = generate_hash(original_message)

# Mostrar resultados
print("=== Hash SHA-256 en Python ===")
print(f"Texto original: {original_message}")
print(f"Hash SHA-256: {message_hash}")