# Abstract

Docker is a lightweight "virtualization" method to run multiple virtual units
(containers, akin to “chroot”) simultaneously on a single control host.
Containers are isolated with Kernel Control Groups (cgroups) and Kernel Namespaces.

Docker provides an operating system-level virtualization where the Kernel
controls the isolated containers. With other full virtualization solutions
like Xen, KVM, or libvirt the processor simulates a complete hardware
environment and controls its virtual machines.

# Terminology

## chroot

A change root (chroot, or change root jail) is a section in the file system
which is isolated from the rest of the file system. For this purpose, the chroot
command is used to change the root of the file system. A program which is
executed in such a “chroot jail” cannot access files outside the designated
directory tree.

## cgroups

Kernel Control Groups (commonly referred to as just “cgroups”) are a Kernel
feature that allows aggregating or partitioning tasks (processes) and all their
children into hierarchical organized groups to isolate resources.

## Image

A "virtual machine" on the host server that can run any Linux system, for
example openSUSE, SUSE Linux Enterprise Desktop, or SUSE Linux Enterprise Server.

A Docker image is made by a series of layers built one over the other. Each layer
corresponds to a permanent change committed from a container to the image.

For more details checkout [Docker's official documentation](http://docs.docker.com/terms/image/).

## Image Name

A name that refers to an image. The name is used by the docker commands.

## Container

A running Docker Image.

## Container ID

A ID that refers to a container. The ID is used by the docker commands.

## TAG

A string associated to a Image. It commonly used to identify a specific version
of a Image (like tags in version control systems). It is also possible to refer
the same Image with different TAGs.

## Kernel Namespaces

A Kernel feature to isolate some resources like network, users, and others for
a group of processes.

## Docker Host Server

The system that runs the Docker daemon, provides the images, and the management
control capabilities through cgroups.


# Overview

Docker is a platform that allows developers and sysadmins to manage the complete
lifecycle of images.

Docker makes incredibly easy to build, ship and run images containing
applications.

Benefits of Docker:

  * Isolating applications and operating systems through containers.
  * Providing nearly native performance as Docker manages allocation of resources
    in real-time.
  * Controlling network interfaces and applying resources inside containers through cgroups. 
  * Versioning of images.
  * Building images based on existing ones.
  * Sharining/storing on [public](http://docs.docker.com/docker-hub/) or
    [private](http://docs.docker.com/userguide/dockerrepos/#private-repositories)
    repositories.

Limitations of Docker:

  * All Docker containers are running inside the host system's Kernel and not with
    a different Kernel.
  * Only allows Linux "guest" operating systems.
  * Docker is not a full virtualization stack like Xen, KVM, or libvirt.
  * Security depends on the host system. Refer to the [official documentation](http://docs.docker.com/articles/security/)
    for more details.

## Container drivers

Docker has different backend drivers to handle the containers. The recommended
on is [libcontainer](https://github.com/docker/libcontainer), which is also the
default choice. This driver provides direct access with cgroups.

The Docker packages ships also a LXC driver which handles containers using the
LXC tools.

At the time of writing, upstream is working on a `libvirt-lxc` driver.

## Storage drivers

Docker supports different storage drivers:

  * `vfs`: this driver is automatically used when the Docker host filesystem
    does not support copy-on-write. This is a simple driver which does not offer
    some of the advantages of Docker (like sharing layers, more on that in the
    next sections). It is highly reliable but also slow.
  * `devicemapper`: this driver relies on the device-mapper thin provisioning
    module. It supports copy-on-write, hence it offers all the advantages of
    Docker.
  * `btrfs`: this driver relies on Btrfs to provide all the features required
    by Docker. To use this driver the `/var/lib/docker` directory must be on a
    btrfs filesystem.
  * `AUFS`: this driver relies on AUFS union filesystem. Neither the upstream
    kernel nor the SUSE one supports this filesystem. Hence the AUFS driver is
    not built into the SUSE Docker package.

It is possible to specify which driver to use by changing the value of the
`DOCKER_OPTS` variable defined inside of the `/etc/sysconfig/docker` file.
This can be done either manually or using &yast; by browsing to:
  * System
  * /etc/sysconfig Editor
  * System
  * Management
  * DOCKER_OPTS
menu and entering the `-s storage_driver` string.

For example, to force the usage of the `devicemapper` driver
enter the following text:
```
DOCKER_OPTS="-s devicemapper
```

It is recommended to have `/var/lib/docker` mounted on a different filesystem
to not affect the Docker host OS in case of a filesystem corruption.

# Setting up a Docker host

Prepare the host:

  1. Install the `docker` package.
  2. Automatically start the Docker daemon at boot:
     `sudo systemctl enable docker`
  3. Start the Docker daemon:
     `sudo systemctl start docker`

The Docker daemon listens on a local socket which is accessible only by the `root`
user and by the members of the `docker` group.

The `docker` group is automatically created at package installation time. To
allow a certain user to connect to the local Docker daemon use the following
command:

```
sudo /usr/sbin/usermod -aG docker <username>
```

The user will be able to communicate with the local Docker daemon upon his next
login.

## Networking

If you want your containers to be able to access the external network you must
enable the `net.ipv4.ip_forward` rule.
This can be done using YaST by browsing to the
`Network Devices -> Network Settings -> Routing` menu and ensuring that the
`Enable IPv4 Forwarding` box is checked.

This option cannot be changed when networking is handled by the Network Manager.
In such cases the `/etc/sysconfig/SuSEfirewall2` file needs to be edited by
hand to ensure the `FW_ROUTE` flag is set to `yes` like so:

```
    FW_ROUTE="yes"
```


# Basic Docker operations

Images can be pulled from [Docker's central index](http://index.docker.io) using
the following command:

```
docker pull <image name>
```

Containers can be started using the `docker run` command.

Please refer to the [official documentation](http://docs.docker.com/)
for more details.


# Building Docker containers using KIWI

Starting from version 5.06.8 KIWI can be used to build Docker images.
Please refer to KIWI's [official documentation](https://doc.opensuse.org/projects/kiwi/doc/#chap.lxc).
The official `kiwi-doc` package contains examples of Docker images.

## Docker build system versus KIWI

Docker has an [internal build system](http://docs.docker.com/reference/builder/)
which makes incredibly easy to create new images based on existing ones.

Some users might be confused about what to use. The right approach is to build
the [base images](http://docs.docker.com/terms/image/#base-image-def) using KIWI
and then use them as foundation blocks inside of your Docker's build system.

That two advantages:

  1. Be able to use docker specific directives (like `ENTRYPOINT`, `EXPOSE`, ...).
  2. Be able to reuse already existing layers.

Sharing the common layers between different images makes possible to:

  * Use less disk space on the Docker hosts.
  * Make the deployments faster: only the requested layers are sent over the
    network (it is like upgrading installed packages using delta rpms).
  * Take full advantage of caching while building Docker images: this will result
    in faster executions of `docker build` command.

To recap: KIWI is not to be intended as a replacement for Docker's build system.
It rather complements with it.

