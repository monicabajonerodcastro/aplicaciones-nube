# aplicaciones-nube

### Ejecución
docker-compose up --build

### Puertos
- 5001: Ngnix
- 5002: Microservice-API
- 5003: Cola de mensajes


### APi api/auth/signup
Request:
api/auth/signup
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
