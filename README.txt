    BIBLIOTECA MICROSEVICES

Projeto acadêmico desenvolvido para demonstrar conceitos de arquitetura de microserviços, conteinerização com Docker, orquestração com Kubernetes, CI/CD e observabilidade básica.

    ARQUITETURA

O sistema é composto por três serviços:

- API Gateway
- User Service
- Book Service

Fluxo da aplicação:

Cliente > API Gateway > User Service e Book Service

    APU GATEWAY

Responsável por centralizar o acesso aos serviços internos.

Endpoints:

- `/users`
- `/books`
- `/health`

    USER SERVICE

Responsável por fornecer informações de usuários.

Endpoints:

- `/`
- `/health`

    BOOK SERVICE

Responsável por fornecer informações de livros.

Endpoints:

- `/`
- `/health`

    TECNOLOGIAS UTILIZADAS

- Python
- Flask
- Docker
- Docker Compose
- Kubernetes
- GitHub Actions

    ESTRUTURA DO PROJETO
biblioteca-microservices/
│
├── api-gateway/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── user-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── book-service/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/
│   ├── users-deployment.yaml
│   ├── users-service.yaml
│   ├── books-deployment.yaml
│   ├── books-service.yaml
│   ├── gateway-deployment.yaml
│   ├── gateway-service.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   └── hpa.yaml
│
├── docker-compose.yml
└── README.md

    EXECUÇÃO COM DOCKER COMPOSE

Pré-requisitos

- Docker
- Docker Compose

Executar

docker compose up --build


Serviços disponíveis:

| Serviço | URL |
|----------|----------|
| Gateway | http://localhost:5000 |
| Users | http://localhost:5001 |
| Books | http://localhost:5002 |

Testes:

curl http://localhost:5000/users


curl http://localhost:5000/books


    EXECUÇÃO COM KUBERNETES

    Pré-requisitos

- Kubernetes
- kubectl

    Aplicar recursos

kubectl apply -f k8s/

    Verificar Deployments:

kubectl get deployments

    Verificar Pods:

kubectl get pods

    Verificar Services:

kubectl get services


    ACESSO AO GATEWAY

O gateway é exposto através de um Service do tipo NodePort.

    Exemplo:

kubectl get services

    Saída:

api-gateway   NodePort   10.96.x.x   <none>   5000:30000/TCP

Acesso(no navegador):

http://localhost:30000/users

http://localhost:30000/books

    CONFIGMAP

Utilizado para armazenar configurações não sensíveis.

Exemplos:

- USER_SERVICE_URL
- BOOK_SERVICE_URL

    SECRET

Utilizado para armazenar informações sensíveis.

Exemplo:

- API_KEY

O Secret é injetado na aplicação através de variáveis de ambiente.


    HEALTH CHECKS

Todos os serviços implementam endpoint:

/health

Utilizado pelas probes do Kubernetes.


    READINES PROBE

Verifica se o container está pronto para receber tráfego.

    LIVENESS PROBE

Verifica se o container continua saudável durante a execução.

    ESCALABILIDADE

Foi configurado um Horizontal Pod Autoscaler (HPA).

Configuração:

- Mínimo: 2 réplicas
- Máximo: 5 réplicas
- Métrica: utilização de CPU


    ESTRATEGIA DE DEPLOY

Foi utilizada a estratégia Rolling Update fornecida pelo Kubernetes.

Benefícios:

- Zero downtime
- Atualização gradual dos pods
- Possibilidade de rollback


    OBSERVABILIDADE

    logs

Logs gerados pelos serviços Flask.

    Visualização:

kubectl logs deployment/api-gateway


kubectl logs deployment/user-service


kubectl logs deployment/book-service


    METRICAS

Monitoramento previsto para:

- CPU
- Memória
- Latência

    TRACING

A arquitetura prevê integração futura com OpenTelemetry para rastreamento distribuído entre microserviços.


    CI/CD

Pipeline automatizado utilizando GitHub Actions.

Etapas:

1. Checkout do código
2. Build das imagens Docker
3. Execução de validações
4. Publicação de artefatos


AUTOR: Gabriel Leal