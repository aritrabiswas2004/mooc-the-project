# TODO List Application

The Project (Todo List App) is done in this repo (and not the [main](https://github.com/aritrabiswas2004/devops-with-kubernetes) one) for the exercises below

> The below list is extended when more exercises are completed

- 3.6
- 3.7
- 3.8
- 3.9
- 3.10

## Notes on exercise `3.10`

The secret key to obtain access to the IAM service account responsible for Read/Write to Google Object Storage was dowloaded via the below command

```shell
gcloud iam service-accounts keys create pgkey.json --iam-account=pg-backup-sa@<PROJECT_ID>.iam.gserviceaccount.com
```

Then this key was used to create a kubernetes secret with the command below

```shell
kubectl create secret generic gcp-key --from-file=pgkey.json
```

Finally, a reference to this secret and secret key JSON file is given in the CronJob and monuted on the `/var/secrets` path.

## Answer to Exercise `3.9`

| Category                   | DBaaS                                                                                                                                                                                                                                                                                          | PVC (self-managed)                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Initialization & Setup** | Very easy with only a few clicks or API calls.                                                                                                                                                                                                                                                 | More complex. Setup complexity increases with more storage classes, PVC configs, DB containers etc.  (via helm or manifests)                                                                                                                                                                                                                                                                                                                   |
| **Initialization Time**    | Few minutes to a few hours                                                                                                                                                                                                                                                                     | Hours to days depending on complexity                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Costs**                  | **Initial Costs:** No initial costs <br><br> **Running Costs:** Higher than PVC sue to added management costs <br><br> [\$0.0454 / 1 hour](https://cloud.google.com/sql/pricing?hl=en#tg0-t1) for the vCPU and [\$0.0077 / 1 gibibyte hour](https://cloud.google.com/sql/pricing?hl=en#tg0-t1) | **Initial Costs:** No initial cost to set up persistent volume <br><br> **Running Costs:** Costs correlate highly to k8s cluster costs and storage volumes costs. In GKE, the cluster and the Compute Engine Disks used for persistent storage add to the costs. <br><br> 	[$0.000054795 / 1 GiB per hour](https://cloud.google.com/compute/disks-image-pricing?hl=en#tg1-t0) is the rate for standard zonal persistent disk (europe-north1-b) |
| **Maintenance**            | Almost completely managed by cloud provider with helpful tools for monitoring on dashboard.                                                                                                                                                                                                    | Almost entirely managed by the user including the updates, testing, downtimes and monitoring is done by Prometheus/Grafana.                                                                                                                                                                                                                                                                                                                    |
| **Backup Methods**         | Backup is automated completely by the cloud provider.                                                                                                                                                                                                                                          | Backup needs to be manually managed by the user.                                                                                                                                                                                                                                                                                                                                                                                               |
| **Ease of Use**            | Very easy and intuitive. One-click solutions to restore a new instance                                                                                                                                                                                                                         | Complex and usually need advanced users. Typically, professional expertise is required in managing code, configurations and maintaining DB infrastructure.                                                                                                                                                                                                                                                                                     |

> [!NOTE]
> For exercise `3.7` onwards the tag name of `3.X` (`X` is any number) causes the pipeline to fail since it is not a valid namespace name. 
> For all other branch names that are also valid namespace names, it works! 


