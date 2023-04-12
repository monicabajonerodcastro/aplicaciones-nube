# aplicaciones-nube

### Ejecución
docker-compose up --build

### Puertos
- 5001: Ngnix
- 5002: Microservice-API
- 5003: Cola de mensajes


### APi api/auth/signup
Request:
**api/auth/signup**
{
 "username":"username",
 "password1":"password1",
 "password2":"123456",
 "email":"prueba@hotmail.com"

}

Response:

{
    "id": 2,
    "mensaje": "usuario creado exitosamente"
}


### APi api/auth/login
Request:
{
 "username":"username",
 "password":"password",
 
}

Response:

{
    "id": 1,
    "mensaje": "Inicio de sesión exitoso",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY4MTI3NjgzOCwianRpIjoiNDZjNTYzYzctYjYxYi00MmQ3LWJiZTctMjMzZWVjMGYxMDVlIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjgxMjc2ODM4LCJleHAiOjE2ODEyNzc3Mzh9.N2D0PI9OmDIZkm_nUubHhC-Kl33ddnk22yWzJ8OO0M8"
}
