# TODO List Application

The Project (Todo List App) is done in this repo (and not the [main](https://github.com/aritrabiswas2004/devops-with-kubernetes) one) for the exercises below

> The below list is extended when more exercises of The Project are completed

- 3.6
- 3.7
- 3.8
- 3.9
- 3.10
- 3.11
- 3.12
- 4.2
- 4.5
- ~~4.6~~ (skipped)
- 4.8
- 4.9

## Notes on exercise `4.9`

To deploy the project with ArgoCD, run

<!--comment-->

```shell
kubectl apply -n argocd -f application.yaml
```

By default, the manifest points to the staging overlay.
To deploy to production, update `application.yaml` as below

```yaml
source:
  repoURL: https://github.com/aritrabiswas2004/mooc-the-project
  path: overlays/prod   # change from overlays/staging
  targetRevision: HEAD

destination:
  server: https://kubernetes.default.svc
  namespace: production # change from staging if desired
```
