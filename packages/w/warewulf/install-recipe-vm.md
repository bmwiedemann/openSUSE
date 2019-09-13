# Configure libvirt and kvm to act as a Master System and Compute Node
This document is a companion to the primary install recipe document. It provides details on how to configure libvirt and kvm to act as a Master System and a Compute Node. If you follow these directions, you should have two systems that can be used to continue the primary install recipe document.

## Install libvirt
The virtualization host will have SLES 15 installed and will be using kvm for the virtual machine manager. Using a fresh install of SLES 15, install the following packages:
* libvirt-client
* libvirt-daemon-qemu

```bash
sudo zypper install libvirt-client libvirt-daemon-qemu
```

After the packages are installed, grant an unprivileged user permission to libvirt and kvm functionality. Replace <userid> in the following command with the id of the user that will be creating the virtual machines.

```bash
sudo usermod -a -G kvm,libvirt <userid>
```

For the operating user, add the following environment variable to the users .profile configuration file.

```bash
export LIBVIRT_DEFAULT_URI=qemu:///system
```

The alternative to setting the LIBVIRT_DEFAULT_URI environment variable is to add the `--connect=qemu:///system` option to all executions of the libvirt shell `virsh`.

After changing these user settings, the user will need to log out and log back in for the settings to be effective.

## Setup of libvirt networks
Two networks will be running in libvirt for this setup.
* The `default` network will provide the outbound connection for the master warewulf system.
* The `internal` network will be isolated from any external networks and will be used between the master and compute nodes for DHCP and PXE interactions.

### Start and enable autostart for the `default` network
The `default` network is not enabled by default. The following commands will enable the network now, and cause it to start automatically in the future.

```bash
virsh net-start default
virsh net-autostart default
```

### Add static address for `master` (optional)
Creating a static address for the master node on the default network will make it possible to log into the master node without having to "guess" the address. The address can be added to the virtualization hosts `/etc/hosts` configuration file for convienience.

Edit the `default` network by executing the command `virsh net-edit default` and add the `host` element. The XML should look like this:

```xml
<network>
  <name>default</name>
  <uuid>5884536d-64fd-4d56-b677-b85b450b1369</uuid>
  <forward mode='nat'/>
  <bridge name='virbr0' stp='on' delay='0'/>
  <mac address='52:54:00:e6:e9:13'/>
  <ip address='192.168.122.1' netmask='255.255.255.0'>
    <dhcp>
      <range start='192.168.122.2' end='192.168.122.254'/>
      <host mac='12:34:56:78:90:01' name='master' ip='192.168.122.2'/>
    </dhcp>
  </ip>
</network>
```

### Create, start, and enable autostart for the `internal` network
The `internal` network is just a bridge between VMs and will have no packet forwarding or DHCP functionality. To create the `internal` network, you will need to create an XML file (named `internal.xml` for this example) with the following:

```xml
<network>
  <name>internal</name>
</network>
```

This file will be used to define the `internal` network within libvirt. The `internal` network will also need to be set to autostart and be started:

```bash
virsh net-define internal.xml
virsh net-autostart internal
virsh net-start internal
```

If all has gone well, you should be able to see the following after running the command `virsh net-list`:

```
 Name                 State      Autostart     Persistent
----------------------------------------------------------
 default              active     yes           yes
 internal             active     yes           yes
```

## Setup of libvirt VMs
This installation will have two VMs defined, a `master` system and a compute `node`. The master system will be installed with openSUSE Tumbleweed, and the compute node will simply be cloned from the master node and modified.

The master system can be installed with openSUSE Tumbleweed distribution with the following command:

```bash
virt-install --location http://download.opensuse.org/tumbleweed/repo/oss/ --extra-args="console=ttyS0,115200" --name master --memory 4096 --virt-type kvm --disk size=20 --graphics none --network="network=default,mac=12:34:56:78:90:01" --network="network=internal,model=rtl8139,mac=12:34:56:78:91:00"
```

After the install is complete, log in to the node long enough to shut down the virtual machine using `shutdown now` at the command line.

### Install tips
* Disable causing the swap file size the same as the memory size. This is unnecessarily wasted virtual disk space.
* Skip the creation of a system user. All work done on the master system will be done using the root user, and the compute node will not use the configured user.
* Disable the firewall.
* Enable the SSH server.

### Cloning and editing the compute node
With the master system created and shut down, the compute node can be cloned from the master system by using the following command:

```bash
virt-clone --auto-clone -o master -n compute
```

A few changes need to be made to the compute node. Edit the node by executing `virsh edit compute` and make the following changes:

* Set the node to boot to network. Within /domain/os/boot, make sure `dev` is set to `network`, like this:  
````xml
<boot dev='network'/>
````
* Remove the interface section for the network device attached to the `default` network. The lines to remove look like this:  
```xml
<interface type='network'>
  <mac address='52:54:00:63:6a:c3'/>
  <source network='default'/>
  <model type='virtio'/>
  <address type='pci' domain='0x0000' bus='0x00' slot='0x02' function='0x0'/>
</interface>
```
* Edit the `internal` network interface to have an easy-to-use MAC address. For this example, use this:
```xml
<mac address='12:34:56:78:91:01'/>
```
* For a stateful node (as in this example), modify the disk to be a `scsi` device and remove the address element. The disk target should look like this:  
```xml
<disk type='file' device='disk'>
  <driver name='qemu' type='qcow2'/>
  <source file='/var/lib/libvirt/images/compute.qcow2'/>
  <target dev='sda' bus='scsi'/>
  <address type='pci' domain='0x0000' bus='0x00' slot='0x05' function='0x0'/>
</disk>
```
  * If a purely stateless node is necessary, then the `disk` section can be removed. Do not remove the disk section if you intend to create a stateful node:

## Boot to the Master System
Now it is time to install the warewulf packages. Start the master system and, after startup has completed, login to the mode.
```bash
virsh start master
ssh root@192.168.122.2
```


