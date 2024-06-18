# Node.js 22 development container image

![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description

[Node.js](https://nodejs.org/) is a free, open-source, cross-platform JavaScript run-time environment that lets developers write server-side applications and tools outside of a browser.

## Usage

To deploy an application, install dependencies, copy the sources, and configure the application's main script:

```Dockerfile
FROM registry.opensuse.org/opensuse/bci/nodejs:22

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD [ "node", "./server.js" ]
```

Build and run the container image:

```ShellSession
$ podman build -t my-node-app .
$ podman run -it -p 3000:3000 --rm my-node-app
```

The example above assumes that there is a `package-lock.lock` file in the application directory.
To generate a `package-lock.lock` file, use the following command:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/nodejs:22 npm i --package-lock-only
```

To run a single script inside a container, use the following command:

```ShellSession
$ podman run --rm -v "$PWD":/app:Z -w /app registry.opensuse.org/opensuse/bci/nodejs:22 node script.js
```

## Licensing

`SPDX-License-Identifier: MIT`

This documentation and the build recipe are licensed as MIT.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
