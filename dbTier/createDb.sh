#!/bin/bash 
microk8s kubectl apply -f persistentVolume.yaml
microk8s kubectl apply -f dbConfigMap.yaml
microk8s kubectl apply -f dbSecret.yaml
microk8s kubectl apply -f dbStatefulSet.yaml
microk8s kubectl apply -f dbService.yaml