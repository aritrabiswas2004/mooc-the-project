# TODO List Application

Divided into `todo-app` for frontend and `todo-backend` for backend.

## Using Kustomize

Deploying application is best and safest with Kustomize.

This can be done by `kubectl apply -k .` (assuming you are in the root directory of the project)

## Other Ways

### Deployment

The following can be created with `kubectl apply -f manifests/`

- Deployment (both containers)
- Service (x2)
- Ingress
- ConfigMap
- StatefulSet
- Secret (encrypted)

### Volumes

Persistent Volume and Volume Claim (if the exercise requires to create) can be created with `kubectl apply -f volumes/`

> On GKE, persistent disk is created automatically so only the `persistentvolumeclaim.yaml` file is required
> to be applied. 
