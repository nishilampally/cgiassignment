# cgiassignment

This code is solving the problem in various phases

Application url on EKS cluster:

http://a5f021272e73f46acb45ddb9964ad355-1238236638.us-east-2.elb.amazonaws.com/health

Application url on Docker container from EC2:

http://3.85.37.126:5000/health



Python REST API returining the code is written in:

pythonAPI.py

Infrastructure as a code, creating EKS Cluster

eksconfig.yaml

Infrastructure as a code, creating NodeGroup on EKS cluster

nodegrop.yaml

Dockerfile is written for the containerization

Kubernetes object for deployment of application on EKS

deployment-pythonrest.yaml

Kubernetes object for exposing application on ELB

loadbalancer-pythonhttp.yaml




