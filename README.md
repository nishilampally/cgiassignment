# cgiassignment

This code is solving the problem in various phases

*******************************************************************************************

## **Phase 1: Creating basic infrastructure**

1. Setup installation of basic infrastructure

2. Installation of kubectl, eksctl, configuration of aws cli and all other required softwares like git.

3. Create the EKS Cluster using automation and also create the EKS node group.

```
[root@ip-172-31-20-248 ekscluster]# eksctl create nodegroup --config-file=nodegrop.yaml
2021-10-27 17:58:10 [ℹ]  eksctl version 0.70.0
2021-10-27 17:58:10 [ℹ]  using region us-east-2
2021-10-27 17:58:10 [ℹ]  will use version 1.20 for new nodegroup(s) based on control plane version
2021-10-27 17:58:11 [ℹ]  nodegroup "ng-1-workers" will use "" [AmazonLinux2/1.20]
2021-10-27 17:58:11 [ℹ]  nodegroup "ng-2-builders" will use "" [AmazonLinux2/1.20]
2021-10-27 17:58:12 [ℹ]  3 existing nodegroup(s) (ng-1,ng-1-workers,ng-2) will be excluded
2021-10-27 17:58:12 [ℹ]  1 nodegroup (ng-2-builders) was included (based on the include/exclude rules)
2021-10-27 17:58:12 [ℹ]  will create a CloudFormation stack for each of 1 managed nodegroups in cluster "assignment-cluster"
2021-10-27 17:58:12 [ℹ]
2 sequential tasks: { fix cluster compatibility, 1 task: { 1 task: { create managed nodegroup "ng-2-builders" } }
}
2021-10-27 17:58:12 [ℹ]  checking cluster stack for missing resources
2021-10-27 17:58:12 [!]  retryable error (Throttling: Rate exceeded
        status code: 400, request id: 219f1a2c-47b9-453c-937d-8e6e1d7a428b) from cloudformation/DescribeStacks - will retry after delay of 5.843318366s
2021-10-27 17:58:18 [ℹ]  cluster stack has all required resources
2021-10-27 17:58:18 [ℹ]  building managed nodegroup stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 17:58:18 [ℹ]  deploying stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 17:58:18 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 17:58:35 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 17:58:51 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 17:59:11 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 17:59:28 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 17:59:48 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:00:07 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:00:26 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:00:43 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:01:01 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:01:17 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:01:34 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:01:52 [ℹ]  waiting for CloudFormation stack "eksctl-assignment-cluster-nodegroup-ng-2-builders"
2021-10-27 18:01:52 [ℹ]  no tasks
2021-10-27 18:01:52 [✔]  created 0 nodegroup(s) in cluster "assignment-cluster"
2021-10-27 18:01:52 [ℹ]  nodegroup "ng-2-builders" has 2 node(s)
2021-10-27 18:01:52 [ℹ]  node "ip-192-168-103-77.us-east-2.compute.internal" is ready
2021-10-27 18:01:52 [ℹ]  node "ip-192-168-186-132.us-east-2.compute.internal" is ready
2021-10-27 18:01:52 [ℹ]  waiting for at least 2 node(s) to become ready in "ng-2-builders"
2021-10-27 18:01:52 [ℹ]  nodegroup "ng-2-builders" has 2 node(s)
2021-10-27 18:01:52 [ℹ]  node "ip-192-168-103-77.us-east-2.compute.internal" is ready
2021-10-27 18:01:52 [ℹ]  node "ip-192-168-186-132.us-east-2.compute.internal" is ready
2021-10-27 18:01:52 [✔]  created 1 managed nodegroup(s) in cluster "assignment-cluster"
2021-10-27 18:01:53 [ℹ]  checking security group configuration for all nodegroups
2021-10-27 18:01:53 [ℹ]  all nodegroups have up-to-date configuration

```

 

3. Updated local kubectl with the cluster kubeconfig using the command

  aws eks --region us-east-2 update-kubeconfig --name assignment-cluster

4. Connected to the cluster and verified

```
NAME                                            STATUS   ROLES    AGE    VERSION
ip-192-168-1-180.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-103-77.us-east-2.compute.internal    Ready    <none>   31h    v1.20.10-eks-3bcdcd
ip-192-168-17-234.us-east-2.compute.internal    Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-186-132.us-east-2.compute.internal   Ready    <none>   31h    v1.20.10-eks-3bcdcd
ip-192-168-3-120.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-38-57.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-42-145.us-east-2.compute.internal    Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-51-160.us-east-2.compute.internal    Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-51-49.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-65-69.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-66-37.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-67-74.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-94-147.us-east-2.compute.internal    Ready    <none>   2d6h   v1.20.10-eks-3bcdcd
ip-192-168-94-48.us-east-2.compute.internal     Ready    <none>   2d6h   v1.20.10-eks-3bcdcd

```


************************************************************************************************


## **Phase 2: REST API Coding and verification**

1. Created the REST API returing time and the static message using Python Flask module

2. Tested it on local and its working fine

http://3.85.37.126:5000/health

3. Python code is attached as part of submission.

************************************************************************************************


## **Phase 3: Containerization of application**

1. Written the Dockerfile code 

2. Create the custom image for the same

```
[root@ip-172-31-20-248 ekscluster]# docker build -t pythonrest .
Sending build context to Docker daemon   5.12kB
Step 1/11 : FROM ubuntu:18.04
 ---> 5a214d77f5d7
Step 2/11 : RUN apt-get -y update
 ---> Using cache
 ---> 38b66176ecb7
Step 3/11 : RUN apt-get -y install python3
 ---> Using cache
 ---> 652625a64d05
Step 4/11 : RUN apt-get -y install python3-pip
 ---> Using cache
 ---> fdcd6d43b895
Step 5/11 : RUN pip3 install flask
 ---> Using cache
 ---> 94a387a0c9e8
Step 6/11 : RUN pip3 install Flask-Cors
 ---> Using cache
 ---> 89bd1d3ee147
Step 7/11 : RUN pip3 install requests
 ---> Using cache
 ---> 99a4ff240e7e
Step 8/11 : RUN pip3 install pyyaml
 ---> Using cache
 ---> 010c4b132b41
Step 9/11 : RUN pip3 install datetime
 ---> Using cache
 ---> 21b86a365e26
Step 10/11 : COPY pythonAPI.py /
 ---> 385d3a27bfd4
Step 11/11 : CMD [ "python3", "pythonAPI.py" ]
 ---> Running in 99e92a621151
Removing intermediate container 99e92a621151
 ---> 5e678637e16b
Successfully built 5e678637e16b
Successfully tagged pythonrest:latest

```

3. Tested the image on local docker container

```

docker run -d -t -i -p 5000:5000 pythonrest
646d65b71349ab6d7988fd82ae279f2a3e23bb30d0cab166477069985725cb88
[root@ip-172-31-20-248 ekscluster]# docker ps
CONTAINER ID   IMAGE        COMMAND                  CREATED          STATUS          PORTS                                       NAMES
646d65b71349   pythonrest   "python3 pythonAPI.py"   23 seconds ago   Up 22 seconds   0.0.0.0:5000->5000/tcp, :::5000->5000/tcp   recursing_sinoussi
```

4. Created the ECR repository and pushing the code there

```

aws ecr create-repository --repository-name assignment-ecr --image-scanning-configuration scanOnPush=true  --region us-east-2
{
    "repository": {
        "repositoryUri": "332896030213.dkr.ecr.us-east-2.amazonaws.com/assignment-ecr",
        "imageScanningConfiguration": {
            "scanOnPush": true
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        },
        "registryId": "332896030213",
        "imageTagMutability": "MUTABLE",
        "repositoryArn": "arn:aws:ecr:us-east-2:332896030213:repository/assignment-ecr",
        "repositoryName": "assignment-ecr",
        "createdAt": 1635446689.0
    }
}
[root@ip-172-31-20-248 ekscluster]# docker tag kanban-backend:latest 386906331058.dkr.ecr.ca-central-1.amazonaws.com/manoj-assignment-ecr:latest
Error response from daemon: No such image: kanban-backend:latest
[root@ip-172-31-20-248 ekscluster]# aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 332896030213.dkr.ecr.us-east-2.amazonaws.com
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
[root@ip-172-31-20-248 ekscluster]# docker tag assignment-ecr:latest 332896030213.dkr.ecr.us-east-2.amazonaws.com/assignment-ecr:latest^C
[root@ip-172-31-20-248 ekscluster]# docker tag pythonrest:latest 332896030213.dkr.ecr.us-east-2.amazonaws.com/assignment-ecr:pythonrest
[root@ip-172-31-20-248 ekscluster]# docker push 332896030213.dkr.ecr.us-east-2.amazonaws.com/assignment-ecr:pythonrest
The push refers to repository [332896030213.dkr.ecr.us-east-2.amazonaws.com/assignment-ecr]
59a02f794a5f: Pushed
30a1faba5f23: Pushed
57f2dc41c736: Pushed
e81852148110: Pushed
1bb3c969552f: Pushed
ead442bf3927: Pushed
9f1345a406a4: Pushed
259270693759: Pushed
aa861a8bcaee: Pushed
824bf068fd3d: Pushed
pythonrest: digest: sha256:583f6cdedee27926f6077484bf9f0e1469a028fd6ac03df5959c30b96eb9ff33 size: 2426


```

************************************************************************************************


## **Phase 4: Deployment  of application on EKS**

1. Create the deployment object with YAML for deployment on kubernetes, deployment yaml is attached.

2. Created the loadbalancer yaml for exposing the service to make it accessible from browser, code is attached

```
 kubectl create -f deployment-pythonrest.yaml
deployment.apps/pythonhttp-deployment created
[root@ip-172-31-20-248 ekscluster]# kubectl get pods
NAME                                     READY   STATUS              RESTARTS   AGE
pythonhttp-deployment-765678666c-4twmx   0/1     ContainerCreating   0          7s
pythonhttp-deployment-765678666c-75r6j   0/1     ContainerCreating   0          7s
[root@ip-172-31-20-248 ekscluster]# kubectl get pods
NAME                                     READY   STATUS              RESTARTS   AGE
pythonhttp-deployment-765678666c-4twmx   0/1     ContainerCreating   0          10s
pythonhttp-deployment-765678666c-75r6j   0/1     ContainerCreating   0          10s
[root@ip-172-31-20-248 ekscluster]# kubectl get pods
NAME                                     READY   STATUS    RESTARTS   AGE
pythonhttp-deployment-765678666c-4twmx   1/1     Running   0          12s
pythonhttp-deployment-765678666c-75r6j   1/1     Running   0          12s

```

3. Testing of application on EKS

```
 kubectl logs -f pythonhttp-deployment-765678666c-75r6j
 * Serving Flask app 'pythonAPI' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://192.168.71.161:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 119-668-793

```

4. Checking through the load balancer url

```

```

kubectl create -f loadbalancer-pythonhttp.yaml
service/pythonhttp-service-loadbalancer created
[root@ip-172-31-20-248 ekscluster]# kubectl get svc
NAME                              TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)        AGE
kubernetes                        ClusterIP      10.100.0.1      <none>                                                                    443/TCP        2d
pythonhttp-service-loadbalancer   LoadBalancer   10.100.119.48   a5f021272e73f46acb45ddb9964ad355-1238236638.us-east-2.elb.amazonaws.com   80:31775/TCP   5s
[root@ip-172-31-20-248 ekscluster]# kubectl get svc
NAME                              TYPE           CLUSTER-IP      EXTERNAL-IP                                                               PORT(S)        AGE
kubernetes                        ClusterIP      10.100.0.1      <none>                                                                    443/TCP        2d
pythonhttp-service-loadbalancer   LoadBalancer   10.100.119.48   a5f021272e73f46acb45ddb9964ad355-1238236638.us-east-2.elb.amazonaws.com   80:31775/TCP   33s
[root@ip-172-31-20-248 ekscluster]# kubectl get pods
NAME                                     READY   STATUS    RESTARTS   AGE
pythonhttp-deployment-765678666c-4twmx   1/1     Running   0          2m27s
pythonhttp-deployment-765678666c-75r6j   1/1     Running   0          2m27s
[root@ip-172-31-20-248 ekscluster]# curl http://a5f021272e73f46acb45ddb9964ad355-1238236638.us-east-2.elb.amazonaws.comhealth
curl: (6) Could not resolve host: a5f021272e73f46acb45ddb9964ad355-1238236638.us-east-2.elb.amazonaws.comhealth
** [root@ip-172-31-20-248 ekscluster]# curl http://a5f021272e73f46acb45ddb9964ad355-1238236638.us-east-2.elb.amazonaws.com/health**
Automate All The Things 18:49:11[root@ip-172-31-20-248 ekscluster]# ls

```

************************************************************************************************


## **Final Notes**

1. Entire Infrastructure and Deployment could be fully automated using any CI/CD tool

2. Flow could be like this

GIT Commit --- Create new image -- Test it and scan it --- Push to ECR --- Deploy as rolling update on EKS

3. Final urls are as follows"

Application url on EKS cluster:

http://a5f021272e73f46acb45ddb9964ad355-1238236638.us-east-2.elb.amazonaws.com/health

Application url on Docker container from EC2:

http://3.85.37.126:5000/health

4. Code details are as follows

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




