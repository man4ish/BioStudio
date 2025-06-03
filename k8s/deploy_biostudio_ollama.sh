#!/bin/bash

set -e

echo "Applying DockerHub secret..."
kubectl apply -f docker-secret.yaml

echo "Deploying biostudio app..."
kubectl apply -f biostudio-deployment.yaml
kubectl apply -f biostudio-service.yaml

echo "Deploying ollama app..."
kubectl apply -f ollama-deployment.yaml
kubectl apply -f ollama-service.yaml

echo "Waiting for pods to be ready..."
sleep 15  # Wait a bit for pods to start

echo "Listing pods:"
kubectl get pods

echo "Listing services:"
kubectl get svc

echo "Deployment script completed."
