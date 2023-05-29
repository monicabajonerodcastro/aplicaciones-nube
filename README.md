# aplicaciones-nube

### Ejecución
1. docker buildx build --platform linux/amd64 -t gcr.io/cloud-apps-387203/worker:worker-latest .
2. docker push gcr.io/cloud-apps-387203/worker:worker-latest 
3. Desplegar el contenedor en GCP
4. docker buildx build --platform linux/amd64 -t gcr.io/cloud-apps-387203/api:api-latest .
5. docker push gcr.io/cloud-apps-387203/api:api-latest 
6. Crear un cron que consuma el endpoint {{api_url}}/publish-pending-tasks


### Puertos
- 5002: Microservice-API
- 5003: Cola de mensajes
- 5004: Worker

