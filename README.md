# developerhub-agentic-demo

First you need an OpenShift cluster with the required dependencies, it can be installed with the validated patter at:
https://github.com/luis5tb/multicloud-gitops/tree/rhdh-demo (note the `rhdh-demo` branch):

```bash
$ git clone https://github.com/luis5tb/multicloud-gitops/tree/rhdh-demo
$ cd multicloud-gitops

# Adjust secrets as needed
$ cp values-secret.yaml.template ~/.config/hybrid-cloud-patterns/values-secret-multicloud-gitops.yaml
$ ./pattern.sh make install 

# Copy admin.password from secret hub-gitops-cluster at multiclod-gitops-hub namespace and replace it on values-secret.yaml
$ cp values-secret.yaml.template ~/.config/hybrid-cloud-patterns/values-secret-multicloud-gitops.yaml
$ ./pattern.sh make load-secrets
```

Then, you can import the template into your deployed Red Hat Developer Hub and instantiate it. It will create
- gitops repo with the resources being created
- git repo with the code for the agent
- argocd applications to deploy:
  - Building pipeline for the agent image
  - LLM at OpenShift AI
  - Agent at OpenShift
