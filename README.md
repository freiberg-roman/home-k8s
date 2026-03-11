# home-k8s

A test homelab Kubernetes cluster managed with GitOps via ArgoCD.

## Overview

Single-cluster setup using the **ArgoCD App of Apps** pattern. The root application (`root_app.yaml`) bootstraps everything by pointing ArgoCD at the `argocd-apps/` directory, which contains Application definitions that sync automatically.

## What's Deployed

| App | Description |
|---|---|
| Docker Registry | Local container registry (TLS, 50Gi PVC, NodePort) |
| Node Feature Discovery | Detects hardware features and labels nodes |
| NVIDIA Device Plugin | Exposes GPUs to the cluster |
| Local Path Provisioner | Dynamic local PV provisioning (Rancher) |

## Repo Structure

```
root_app.yaml          # ArgoCD root app (bootstrap)
argocd-apps/           # ArgoCD Application definitions
apps/                  # Workload manifests
cluster-addons/        # Infrastructure addons
```
