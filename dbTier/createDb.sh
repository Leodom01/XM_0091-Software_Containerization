#!/bin/bash 
microk8s kubectl apply -f db-chart/templates/persistentVolume.yaml
microk8s kubectl apply -f db-chart/templates/dbConfigMap.yaml
microk8s kubectl apply -f db-chart/templates/dbSecret.yaml
microk8s kubectl apply -f db-chart/templates/dbStatefulSet.yaml
microk8s kubectl apply -f db-chart/templates/dbService.yaml