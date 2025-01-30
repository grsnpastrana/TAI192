from fastapi import FastAPI
from typing import Optional

app = FastAPI(
    title='My FastAPI 192', 
    description='API de Gerson',
    version='1.0.1',
)

usuarios = [
    {'id': 1, 'nombre': 'ivan', 'edad': 37},
    {'id': 2, 'nombre': 'isay', 'edad': 15},
    {'id': 3, 'nombre': 'luis', 'edad': 18},
    {'id': 4, 'nombre': 'ana', 'edad': 37}
]

# Endpoint home
@app.get('/', tags=['Hola Mundo'])
def home():
    return {'hello': 'world FastAPI'}

# Endpoint promedio
@app.get('/promedio', tags=['Mi Calificacion Parcial'])
def promedio():
    return {'promedio': 10}

# Endpoint con parámetro obligatorio
@app.get('/usuario/{id}', tags=['Parametro obligatorio'])
def consulta_usuario(id: int):
    return {'Se encontró el usuario': id}

# Endpoint con parámetro opcional
@app.get('/usuario/', tags=['Parametro Opcional'])
def consulta_usuario_opcional(id: Optional[int] = None):
    if id is not None:
        for usu in usuarios:
            if usu["id"] == id:
                return {'mensaje': 'Usuario encontrado', 'usuario': usu}
        return {'mensaje': f'No se encontró usuario con id: {id}'}
    else:
        return {'mensaje': 'No se proporcionó un id'}
