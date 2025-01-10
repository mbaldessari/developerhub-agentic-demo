# developerhub-agentic-demo

First you need an OpenShift cluster with the required dependencies, it can be installed with the validated patter at:
https://github.com/luis5tb/multicloud-gitops/tree/rhdh-demo (note the `rhdh-demo` branch):

```bash
$ git clone https://github.com/luis5tb/multicloud-gitops/tree/rhdh-demo
$ cd multicloud-gitops

# Adjust secrets as needed
$ cp values-secret.yaml.template ~/.config/hybrid-cloud-patterns/values-secret-multicloud-gitops.yaml
$ ./pattern.sh make install 

# Copy the output token to your values-secret.yaml.template with your github credentials
$ cat values-secret.yaml.template
  - name: rhdh-keys
    fields:
    - name: BACKEND_SECRET
      value: rhdh_1_2_3
    - name: GH_ACCESS_TOKEN
      value: XXXX
    - name: GH_CLIENT_ID
      value: XXX
    - name: GH_CLIENT_SECRET
      value: XXX

# Regenerate the vault with the secrets
$  cp values-secret.yaml.template ~/.config/hybrid-cloud-patterns/values-secret-multicloud-gitops.yaml
$  ./pattern.sh make load-secrets
```

The template will be automatically imported, but you can clone it, modify it and then import the template into your deployed Red Hat Developer Hub and instantiate it. It will create
- gitops repo with the resources being created
- git repo with the code for the agent
- argocd applications to deploy:
  - Building pipeline for the agent image
  - LLM at OpenShift AI
  - Agent at OpenShift

After everything is deployed, there is a need for another manual step (for now):
- Copy the token and the inference endpoint from the deployed model on OpenShift AI
- (Alternatively you can point to a different vLLM deployment if you wish)
- Make use of values-secret.yaml.template to create the information with it and update the vault so that the secret gets created in the agent application namespace:

  ```bash
  # Update the secret template with the information requested
  $ cat values-secret.yaml.template
  ...
    - name: llm-keys
      fields:
      - name: endpoint
        value: endpoint-url   # CHANGE ME
      - name: token
        value: super_secret_token   # CHANGE ME

  # Update the vaults
  $ cp values-secret.yaml.template ~/.config/hybrid-cloud-patterns/values-secret-multicloud-gitops.yaml
  $ ./pattern.sh make load-secrets
  ```
