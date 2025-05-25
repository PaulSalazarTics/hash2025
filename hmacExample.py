# hmac_example.py
import hmac
import hashlib

# Datos iniciales
message = "mensaje a ser enviado"
secret_key = "clave secreta"

# Función para generar HMAC
def generate_hmac(key, msg):
    # Crear HMAC con SHA-256
    hmac_code = hmac.new(key.encode(), msg.encode(), hashlib.sha256)
    return hmac_code.hexdigest()

# Generar HMAC
hmac_code = generate_hmac(secret_key, message)

# Mostrar resultados
print("=== HMAC en Python ===")
print(f"Mensaje original: {message}")
print(f"Clave secreta: {secret_key}")
print(f"HMAC generado: {hmac_code}")

# Simular intercambio (como en tu ejemplo de clase)
output = f"{message}\n{hmac_code}"
print("\nDatos para 'archivo':")
print(output)

# Verificación
print("\n=== Verificación ===")
received_data = output.split('\n')
received_message = received_data[0]
received_hmac = received_data[1]

# Recalcular HMAC
new_hmac = generate_hmac(secret_key, received_message)

# Validar
is_valid = hmac.compare_digest(received_hmac, new_hmac)  # Comparación segura
print(f"¿El HMAC es válido? {is_valid}")