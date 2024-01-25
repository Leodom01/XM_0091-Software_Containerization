#!/bin/bash 
microk8s kubectl delete pv mongo-pv
microk8s kubectl delete configmap mongo-config
microk8s kubectl delete secret mongo-secret
microk8s kubectl delete statefulset db-tier
microk8s kubectl delete service db-svc