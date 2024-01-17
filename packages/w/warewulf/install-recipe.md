# Install Warewulf 3.8 onto openSUSE Tumbleweed, openSUSE Leap, or SUSE Linux Enterprise Server Using Packages From The Open Build Service

## System Configuration
This installation recipe is written with the following system configuration in mind:

* Master System
  This system will have the Warewulf packages installed and will have the following configuration:
  * One network adapter (eth0) that will be physically connected to a network switch that has access to the software repository. This can be a local repository or a repository found on The Internet.
  * One network adapter (eth1) that will be physically connected to a network switch that is isolated from the external network and is connected to the compute node.
  * A clean installation of openSUSE Tumbleweed, openSUSE Leap, or SUSE Linux Enterprise Server.
* Compute Node
  This system will boot from the network using the services provided by the master system. While this document describes the creation of only one compute node within Warewulf, usually more than one will be created. The network adapter MAC address is necessary along with the assigned IP address for the node. Automatic discovery of node is also possible with the warewulf-cluster package, but is not discussed in this document.
  The compute node will have the following configuration:
  * One network adapter (eth0) that will be physically connected to a network switch that is isolated from the external network and is connected to the master system.

Additional documentation is provided that helps configure two virtual machines, using libvirt and kvm, to act as the master system and compute node, with all necessary virtual network configuration.

## Installation of Warewulf packages into the master system
Warewulf currently is divided up into several packages. Following is a description of each package and their purpose.

### Packages to install
* warewulf-common, perl-warewulf-common
  The warewulf-common package contains the base configuration and scripts that are used by all other warewulf modules. All other packages depend on warewulf-common.
  The perl-warewulf-common package contains the perl scripts necessary for the warewulf-common package.
* warewulf-provision, perl-warewulf-provision
  These packages provide the tools for provisioning bootstraps and filesystems to the nodes, along with tools to dynamically configure nodes.
* warewulf-provision-server, perl-warewulf-provision-server
  These packages provide the scripts that control dhcpd, tftp, and apache servers to provide boot services to the compute nodes
  These packages also may be installed seperately from the administrative master, but this configuration is untested and currently unsupported.
* warewulf-provision-x86_54-initramfs, warewulf-provision-arm64-initramfs
  These packages provide the bootstrap images that will be used by compute nodes of specific architectures to startup the compute nodes
* warewulf-provision-ipxe-images
  This package contains the ipxe images needed to access the compute node bootstrap via the http protocol
* warewulf-vnfs
  This package contains utilities necessary to create the bootable filesystems that will run the compute nodes. Several operating system templates are provided.
* warewulf-cluster, perl-warewulf-cluster
  These packages contain utilities that assist in the definition of nodes within the Warewulf database

From the command prompt of the master system, the warewulf packages can now be installed:
```bash
zypper install warewulf-cluster warewulf-provision warewulf-provision-server warewulf-vnfs warewulf-provision-x86_64-initramfs warewulf-provision-ipxe-images
```

## Warewulf initialization
With the warewulf packages installed, changes need to be made to the configuration:

* Set the IP address for the internal network. This can easily be done with YaST. For this setup, the address should be static and set to `192.168.123.254` with the netmask `255.255.255.0`

* Set the correct `network device` within `/etc/warewulf/provision.conf`. This should be set to the network interface attached to the `internal` network:
```
network device = eth1
```

* In the `/etc/sysconfig/dhcpd` configuration file, set the `DHCPD_INTERFACE` to the adapter connected to `internal`
```
DHCPD_INTERFACE="eth1"
```

With the configuration changes made, initialize warewulf:

```bash
wwinit ALL
```

## Creation of Virtual Node File System (VNFS)
Create the filesystem root:
```bash
wwmkchroot opensuse-tumbleweed /var/lib/warewulf/chroots/tumbleweed
```

Compile the VNFS. To create the tumbleweed vnfs from the filesystem root, execute this command:
```bash
wwvnfs -c /var/lib/warewulf/chroots/tumbleweed tumbleweed
```

## Stateless Node definition in Warewulf
Create the node.
```bash
wwsh node new compute --hwaddr="12:34:56:78:91:01" --ipaddr="192.168.123.1"
```

Add the local `shadow` file to the node in order to login
```bash
wwsh file import /etc/shadow shadow
```

Provision the node.
```bash
wwsh provision set compute --bootstrap=`uname -r` --vnfs=tumbleweed --console="ttyS0,115200" --fileadd shadow
```

Update the pxe configuration:
```bash
wwsh pxe update
```

Restart the services:
```bash
systemctl restart dhcpd
systemctl restart apache2
```

With the master system configured, log off the master system (back to the virtualization host)

## Boot
From the virtualization host, start the compute node:
```bash
virsh start --console compute
```

The compute node should start successfully

## Stateful Node definition in Warewulf
In order to cause a stateful installation of the compute node, a filesystem script needs to be added to the provisioning. A simple script may look like this:
```
# Parted specific commands
select /dev/sda
mklabel msdos
mkpart primary ext4 1MiB 513MiB
mkpart primary linux-swap 513MiB 50%
mkpart primary ext4 50% 100%
set 1 boot on

# mkfs NUMBER FS-TYPE [ARGS...]
mkfs 1 ext4 -L boot
mkfs 2 swap
mkfs 3 ext4 -L root

# fstab NUMBER fs_file fs_vfstype fs_mntops fs_freq fs_passno
fstab 3 / ext4 defaults 0 0
fstab 1 /boot ext4 defaults 0 0
fstab 2 swap swap defaults 0 0
```

This script should be stored in a file. For this example, the filename for the script will be `filesys.cmds`

To provision the node as a stateful node, run the following command:
```bash
wwsh provision set compute --bootloader=sda --filesystem=filesys.cmds
```


