# kube-test-container

Python alpine container including all binaries from package.yaml to test kubernetes manifests.

```yaml
kubectl:
     version: v1.21.0
kubeval:
     version: v0.16.1
kube-score:
     version: v1.11.0
config-lint:
     version: v1.6.0
copper:
     version: 2.0.1
conftest:
     version: v0.24.0
polaris:
     version: 3.2.1
```

https://hub.docker.com/repository/docker/jonguijarro/kube-test

```bash
docker pull jonguijarro/kube-test:0.0.1
```
