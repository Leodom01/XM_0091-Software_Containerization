# XM_0091-Software_Containerization
This repository contains the source code of a 3-tier application that is containerized using Docker and deployed on Kubernetes. The application is a simple reminder app that allows users to add reminders.

## Contributors
You can find the repository at https://github.com/Leodom01/XM_0091-Software_Containerization

Contributors:
- Leonardo Dominici
- Dalvie Benu
- Minh Duc Nguyen

## Running the Application
In order to run the app reachable at http://localhost:30002/, you need to follow the steps below.
### 1. Setting Up Persistent Volume
```bash
kubectl apply -f dbTier/dbPersistentVolume.yaml
```

### 2. Installation of 3-tier Application using Helm
```bash
helm install -g app-deployment/
```

### 3. Enabling TLS
Add "127.0.0.1 reminder.com" to /etc/hosts in order to access the app via http://reminder.com and 
```bash
helm install -g tls/
```

## Application Architecture
pic

## Requirements
### Persestent Layer

### REST API
scaling by hpa


### Web Frontend
scaling by hpa


### TLS

### Helm Chart


### Security - Network Policies

### Security - RBAC


### Google Cloud Platform



