# The {self.title} container image
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

# Purpose

This chart deploys a SUSE Repository Mirroring Tool (RMT) server on Kubernetes.
It is tested on K3s but should work on any Kubernetes distribution.

## Overview

To deploy SUSE RMT on top of Kubernetes, each component of the stack is deployed in a dedicated container using a
Helm chart.
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

The Helm chart can be obtained using the following command:

`helm pull oci://registry.suse.com/suse/rmt-helm`

## Custom mandatory values

Certain values of the chart do not have any defaults:
- SCC mirroring credentials (refer to [more information](https://documentation.suse.com/sles/html/SLES-all/cha-rmt-mirroring.html#sec-rmt-mirroring-credentials) for more information)
- list of products to mirror
- list of products not to mirror
- DNS name used to reach the RMT server
- configured [storage](https://kubernetes.io/docs/concepts/storage/)

Before deploying the chart, you must fill a custom values file.

The following example enables ingress with TLS. The `create-certs.sh` script
supplied with the Helm chart can be used
to create self-signed certificates and add them to Kubernetes as a usable TLS
secret.

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

The required values in the custom value file are as follows:

- `app.scc.password` SUSE Customer Center proxy password. The password string must be in quotes. If the quote character `"` is part of the string, it has to be escaped with `\`.
- `app.scc.username` SUSE Customer Center proxy user name. The user name string must be quotes. If the quote character `"` is part of the string, it has to be escaped with `\`.
- `app.scc.products_enable` List of products to enable for mirroring.
- `app.scc.products_disable` list of products to exclude from mirroring.
- `app.storage.class` Kubernetes storageclass.
- `db.storage.class` Kubernetes storageclass.
- `ingress.enabled` Enable or disable ingress.
- `ingress.hosts[0]` DNS name at which the RMT service is be accessible from clients.
- `ingress.tls[0].hosts[0]` DNS name at which the RMT service is be accessible from clients.
- `ingress.tls[0].secretName` TLS ingress certificate.

## Deploying

`helm install rmt ./helm -f myvalues.yaml`

## Further info

For more information on using RMT, refer to the [RMT Guide](https://documentation.suse.com/sles/html/SLES-all/book-rmt.html).

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
