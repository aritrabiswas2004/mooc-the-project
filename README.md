# TODO List Application

The Project (Todo List App) is done in this repo (and not the [main](https://github.com/aritrabiswas2004/devops-with-kubernetes) one) for the exercises below

> The below list is extended when more exercises are completed

- 3.6
- 3.7
- 3.8

## Deploying the Application

This application automatically deploys to the GKE cluster from the deployment pipeline in `.github/workflows/main.yaml` (see GitHub actions)

The images are stored in a Docker repository on Artifact Registry on GCP

> [!NOTE]
> For exercise `3.7` onwards the tag name of `3.X` (`X` is any number) causes the pipeline to fail since it is not a valid namespace name. 
> For all other branch names that are also valid namespace names, it works! 

### Using Kustomize

You can deploy it using the `kustomization.yaml` file with the below commands

```shell
kustomize edit set image PROJECT/IMAGE_DIR1=$PATH_TO_IMAGE1 # todo-app
kustomize edit set image PROJECT/IMAGE_DIR2=$PATH_TO_IMAGE2 # todo-backend
kustomize build . | kubectl apply -f -
```



