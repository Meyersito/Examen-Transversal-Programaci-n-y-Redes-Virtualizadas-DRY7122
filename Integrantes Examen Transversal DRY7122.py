integrantes = [
    {"nombre": "Benjamin", "apellido": "Gallardo"},
    {"nombre": "Benjamin", "apellido": "Gonzalez"},
    {"nombre": "Diego", "apellido": "Palestro"},
]

nombres_apellidos = [f"{integrante['nombre']} {integrante['apellido']}" for integrante in integrantes]

print(nombres_apellidos)