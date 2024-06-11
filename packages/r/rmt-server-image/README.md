# The {self.title} Container Image
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

# Purpose

This chart deploys a SUSE Repository Mirroring Tool (RMT) server on Kubernetes.
It is tested on K3s but should work on any Kubernetes distribution.

## Overview

To deploy SUSE RMT on top of Kubernetes, each component of the stack is deployed in a dedicated container via a
Helm Chart.

### Repository Mirroring Tool (SUSE RMT) server

A containerized version of the SUSE RMT application that can pass its configuration via Helm values. Because persistent storage resides on a persistent volume, you need to adjust the volume size according to the number of repositories you need to mirror.

### MariaDB

The database back-end for SUSE RMT.
If needed, RMT creates the database and tables at startup, so no specific
post-installation task is required for it to be usable. Passwords are
self-generated, unless explicitly specified in the values file.

### NGINX

The web server with appropriate configuration for RMT routes. Having a correctly
configured web server right from the start allows you to target your ingress traffic
(for RMT) to directly to the server. You don't have to configure ingress for RMT specific
paths handling, as NGINX is configured to do that.

## Prerequisites

- a running Kubernetes cluster
- helm command configured to interact with the cluster

## Custom mandatory values

Certain values of the chart do not have any defaults:
- SCC mirroring credentials (refer to [more information](https://documentation.suse.com/sles/15-SP4/html/SLES-all/cha-rmt-mirroring.html#sec-rmt-mirroring-credentials) for more information)
- list of products to mirror
- list of products not to mirror
- DNS name used to reach the RMT server
- configured [storage](https://kubernetes.io/docs/concepts/storage/)

Before deploying the chart, you must fill a custom values file.

The following example enables ingress with TLS.
The create-certs.sh can be used to create self-signed certificates and
add them to Kubernetes as a usable TLS secret.

```
cat << EOF > myvalues.yaml
---
app:
  storage:
    class: my-storage-class
  scc:
    username: UXXXXXXX
    password: PASSXXXX
    products_enable:
      - SLES/15.3/x86_64
      - sle-module-python2/15.3/x86_64
    products_disable:
      - sle-module-legacy/15.3/x86_64
      - sle-module-cap-tools/15.3/x86_64
ingress:
  enabled: true
  hosts:
    - host: chart-example.local
      paths:
        - path: "/"
          pathType: Prefix
  tls:
  - secretName: rmt-cert
    hosts:
    - chart-example.local
db:
  storage:
    class: my-storage-class
EOF
```

## Deploying

`helm install rmt ./helm -f myvalues.yaml`

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
