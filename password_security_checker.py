"""
Verificador de Contraseñas Seguras
Autor: Juan Sandoval
Descripción: Evalúa la fortaleza de una contraseña según su longitud, caracteres y complejidad.
"""

import re

def verificar_contraseña(password):
    criterios = {
        "longitud": len(password) >= 8,
        "mayuscula": bool(re.search(r"[A-Z]", password)),
        "minuscula": bool(re.search(r"[a-z]", password)),
        "numero": bool(re.search(r"[0-9]", password)),
        "especial": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    score = sum(criterios.values())
    niveles = {5: "Muy segura", 4: "Segura", 3: "Moderada", 2: "Débil", 1: "Muy débil"}
    return niveles.get(score, "Insegura")

if __name__ == "__main__":
    pwd = input("Introduce una contraseña para analizar: ")
    print("Nivel de seguridad:", verificar_contraseña(pwd))
