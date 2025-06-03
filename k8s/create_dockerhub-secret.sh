kubectl create secret docker-registry dockerhub-secret \
  --docker-server=https://index.docker.io/v1/ \
  --docker-username=man4ish \
  --docker-password=$#Hanuman007\
  --docker-email=mandecent.gupta@gmail.com --dry-run=client -o yaml > docker-secret.yaml
