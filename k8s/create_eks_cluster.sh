#!/bin/sh

eksctl create cluster \
  --name my-eks-cluster \
  --region us-east-1 \
  --nodes 2 \
  --node-type t3.micro \
  --managed