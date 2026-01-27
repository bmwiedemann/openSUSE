# kubectl Container Image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

Kubectl is a command line tool for communicating with a Kubernetes cluster's control plane, using the Kubernetes API.

## How to use this Container Image

To run commands inside the container for the current cluster for which the kubeconfig is available in `/root/.kube.config`:

```ShellSession
podman run --rm --name kubectl \
      registry.opensuse.org/opensuse/kubectl:1.34 get nodes
```

To pass configuration of a remote cluster to the container:

```ShellSession
podman run --rm --name kubectl \
      -v /localpath/to/kubeconfig:/root/.kube/config:Z
      registry.opensuse.org/opensuse/kubectl:1.34 get nodes
```

This container also includes Helm, the package manager for Kubernetes and Helm charts.
You can use `kubectl customize --enable-helm` for charts:

```ShellSession
podman run --rm --name kubectl \
      -v /localpath/to/customize:/home/user:Z
      registry.opensuse.org/opensuse/kubectl:1.34 kustomize --enable-helm
```


## Licensing

`SPDX-License-Identifier: Apache-2.0`

This documentation and the build recipe are licensed as Apache-2.0.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
