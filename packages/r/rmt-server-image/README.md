# The {self.title} Container Image
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)


# Purpose

This chart deploys a SUSE Repository Mirroring Tool (RMT) server on Kubernetes.
It is tested on K3s but should work on any Kubernetes distribution.

## Overview

Every component of the stack is deployed in a dedicated container via a
Helm Chart to ease deployment on top of Kubernetes.

### Repository Mirroring Tool (SUSE RMT) server

A containerized version of the SUSE RMT application, with the ability to pass its configuration via Helm values.  Persistent storage is on a Persistent Volume, thus you need to adapt its size depending on the number of repositories you need to mirror.

### MariaDB

The database backend for RMT.
RMT does create the database/tables at startup if needed so no specific
post-installation task is required for it to be usable.  Passwords are
self-generated unless explicitly specified in the values file.

### NGINX

The web server with proper configuration for RMT routes.  Having a properly
configured web server out of the box allows you to target your ingress traffic
(for RMT) to it directly. You don't have to configure ingress for RMT specific
paths handling, as NGINX is configured to do so.

## Prerequisites

- a running kubernetes cluster
- helm (v3) command configured to interact with this cluster

## Custom mandatory values

Some values of this chart do not have any sensible defaults:
- SCC mirroring credentials, please have a look here for [more information](https://documentation.suse.com/sles/15-SP4/html/SLES-all/cha-rmt-mirroring.html#sec-rmt-mirroring-credentials)
- list of products to mirror
- list of products to not mirror
- DNS name the RMT server should be reachable at
- Configured [storage](https://kubernetes.io/docs/concepts/storage/)

You should fill a custom values file before deploying the chart.

Below example also enables ingress with TLS.
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

The build recipe and this documentation is licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
