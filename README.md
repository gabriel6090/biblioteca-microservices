# 📚 Biblioteca Microservices

> Projeto acadêmico demonstrando arquitetura de microserviços com Docker, Kubernetes e CI/CD.

---

## 🏗️ Arquitetura

```
Cliente
   │
   ▼
┌──────────────┐
│  API Gateway │  :5000
│  (porta 5000)│
└──────┬───────┘
       │
  ┌────┴────┐
  ▼         ▼
┌──────┐  ┌──────┐
│ User │  │ Book │
│ Svc  │  │ Svc  │
│:5001 │  │:5002 │
└──────┘  └──────┘
```

O **API Gateway** centraliza o acesso e roteia as requisições para os serviços internos. Cada serviço expõe também um endpoint `/health` para as probes do Kubernetes.

---

## 🛠️ Tecnologias

| Tecnologia | Uso |
|---|---|
| Python + Flask | Implementação dos serviços |
| Docker | Conteinerização |
| Docker Compose | Orquestração local |
| Kubernetes | Orquestração em produção |
| GitHub Actions | Pipeline CI/CD |

---

## 📁 Estrutura do Projeto

```
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
```

---

## 🚀 Executando com Docker Compose

### Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Subir os serviços

```bash
docker compose up --build
```

### Endpoints disponíveis

| Serviço | URL |
|---|---|
| API Gateway | http://localhost:5000 |
| User Service | http://localhost:5001 |
| Book Service | http://localhost:5002 |

### Testando

```bash
curl http://localhost:5000/users
curl http://localhost:5000/books
```

---

## ☸️ Executando com Kubernetes

### Pré-requisitos

- [Kubernetes](https://kubernetes.io/docs/setup/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

### Aplicar todos os recursos

```bash
kubectl apply -f k8s/
```

### Verificar o status

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

### Acessar o Gateway (NodePort)

Após aplicar os recursos, o gateway estará disponível via NodePort:

```
http://localhost:30000/users
http://localhost:30000/books
```

---

## ⚙️ Configurações

### ConfigMap

Armazena variáveis de ambiente **não sensíveis**:

- `USER_SERVICE_URL`
- `BOOK_SERVICE_URL`

### Secret

Armazena informações **sensíveis**, injetadas via variáveis de ambiente:

- `API_KEY`

---

## 🩺 Health Checks

Todos os serviços implementam o endpoint `/health`, utilizado pelas probes do Kubernetes:

| Probe | Função |
|---|---|
| **Readiness Probe** | Verifica se o container está pronto para receber tráfego |
| **Liveness Probe** | Verifica se o container continua saudável durante a execução |

---

## 📈 Escalabilidade

Configurado um **Horizontal Pod Autoscaler (HPA)** baseado em utilização de CPU:

| Parâmetro | Valor |
|---|---|
| Réplicas mínimas | 2 |
| Réplicas máximas | 5 |
| Métrica | Utilização de CPU |

---

## 🔄 Estratégia de Deploy

Utilizada a estratégia **Rolling Update** do Kubernetes:

- ✅ Zero downtime
- ✅ Atualização gradual dos pods
- ✅ Possibilidade de rollback

---

## 🔍 Observabilidade

### Logs

```bash
kubectl logs deployment/api-gateway
kubectl logs deployment/user-service
kubectl logs deployment/book-service
```

### Métricas (previstas)

- CPU
- Memória
- Latência

### Tracing (futuro)

Integração prevista com **OpenTelemetry** para rastreamento distribuído entre os microserviços.

---

## 🔁 CI/CD

Pipeline automatizado com **GitHub Actions**:

1. Checkout do código
2. Build das imagens Docker
3. Execução de validações
4. Publicação de artefatos

---

## 👤 Autor

**Gabriel Leal**
