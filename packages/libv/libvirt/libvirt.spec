#
# spec file for package libvirt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# libvirt does not support building in srcdir
%define _vpath_builddir %{_target_platform}

# The hypervisor drivers that run in libvirtd
%define with_qemu          0%{!?_without_qemu:1}
%define with_lxc           0%{!?_without_lxc:1}
%define with_libxl         0%{!?_without_libxl:1}
%define with_vbox          0%{!?_without_vbox:0}

# Then the hypervisor drivers that run outside libvirtd, in libvirt.so
%define with_openvz        0%{!?_without_openvz:1}
%define with_vmware        0%{!?_without_vmware:1}
%define with_phyp          0%{!?_without_phyp:0}
%define with_esx           0%{!?_without_esx:1}
%define with_hyperv        0%{!?_without_hyperv:0}

# Then the secondary host drivers, which run inside libvirtd
%define with_storage_rbd   0%{!?_without_storage_rbd:0}
%define with_storage_sheepdog 0
%define with_storage_gluster  0%{!?_without_storage_gluster:1}
%define with_storage_iscsi_direct 0%{!?_without_storage_iscsi_direct:0}
%define with_apparmor      0%{!?_without_apparmor:1}

# Optional bits on by default
%define with_sanlock       0%{!?_without_sanlock:1}
%define with_polkit_rules  1
%define with_wireshark     0%{!?_without_wireshark:1}
%define with_libssh2       0%{!?_without_libssh2:1}

# A few optional bits off by default, we enable later
%define with_numactl       0%{!?_without_numactl:0}
%define with_numad         0%{!?_without_numad:0}
%define with_firewalld     0%{!?_without_firewalld:0}
%define with_firewalld_zone 0%{!?_without_firewalld_zone:0}
%define with_libssh        0%{!?_without_libssh:0}
%define with_bash_completion 0%{!?_without_bash_completion:0}

# Set the OS / architecture specific special cases

# Xen is available only on x86_64, armv7 and aarch64
%ifnarch x86_64 armv7hl aarch64
    %define with_libxl     0
%endif

# For SLE, further restrict Xen support to x86_64 only
%if ! 0%{?is_opensuse}
    %ifarch %arm aarch64
        %define with_libxl 0
    %endif
%endif

# Enable numactl for most architectures. Handle aarch64 separately
%ifnarch s390 s390x %arm %ix86 aarch64
    %define with_numactl   0%{!?_without_numactl:1}
%endif

# For aarch64, numactl is only available on newer than 1320, or SLE12
# family newer than 120100
%ifarch aarch64
    %if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && ( 0%{?sle_version} > 120100 ) )
        %define with_numactl 0%{!?_without_numactl:1}
    %endif
%endif

# vbox is available only on i386 x86_64
%ifnarch %{ix86} x86_64
    %define with_vbox      0
%endif

# Disable hypervisor drivers not supported in SLE
%if ! 0%{?is_opensuse}
    %define with_openvz    0
    %define with_vbox      0
    %define with_vmware    0
    %define with_hyperv    0
%endif

# Enable phyp driver for IBM Power systems
%ifarch ppc64
    %define with_phyp      1
%endif

# Enable firewalld support in newer code bases
%if 0%{?suse_version} >= 1500
    %define with_firewalld 1
%endif

# The 'libvirt' zone must be used with firewalld >= 0.7.0
%if 0%{?suse_version} >= 1550
    %define with_firewalld_zone 1
%endif

# Enable libssh support in newer code bases
%if 0%{?suse_version} >= 1500
    %define with_libssh    1
%endif

%if 0%{?suse_version} >= 1500
    %define with_bash_completion  0%{!?_without_bash_completion:1}
%endif

# rbd enablement is a bit tricky. For x86_64
%ifarch x86_64
# enable on anything newer than 1320, or SLE12 family newer than 120100
# use librbd-devel as build dependency
    %if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && ( 0%{?sle_version} > 120100 ) )
        %define with_storage_rbd 0%{!?_without_storage_rbd:1}
        %define with_rbd_lib     librbd-devel
    %endif
# enable for SLE12 family <= 120100 (SLE12GA/SP1, Leap 42.1)
# use ceph-devel as build dependency
    %if 0%{?suse_version} == 1315 && 0%{?sle_version} <= 120100
        %define with_storage_rbd 0%{!?_without_storage_rbd:1}
        %define with_rbd_lib     ceph-devel
    %endif
%endif

# For arm
%ifarch aarch64
# enable on anything newer than 1320, or SLE12 newer than 120100
# use librbd-devel as build dependency
    %if 0%{?suse_version} > 1320 || ( 0%{?is_opensuse} == 0 && 0%{?sle_version} > 120100 )
        %define with_storage_rbd 0%{!?_without_storage_rbd:1}
        %define with_rbd_lib     librbd-devel
    %endif
%endif

# gluster storage backend is not supported in SLE
%if ! 0%{?is_opensuse}
    %define with_storage_gluster 0
%endif

# libiscsi storage backend needs libiscsi >= 1.18.0 which is only available
# in suse_version >= 1500
%if 0%{?suse_version} > 1500
    %define with_storage_iscsi_direct 1
%endif

# numad is used to manage the CPU and memory placement dynamically for
# qemu and lxc drivers
%if %{with_qemu} || %{with_lxc}
# Enable numad for most architectures. Handle aarch64 separately
    %ifnarch s390 s390x %arm %ix86 aarch64
        %define with_numad 0%{!?_without_numad:1}
    %endif
# For aarch64, enable on anything newer than 1320, or SLE12 family newer
# than 120100
    %ifarch aarch64
        %if 0%{?suse_version} > 1320 || ( 0%{?suse_version} == 1315 && 0%{?sle_version} > 120100 )
            %define with_numad 0%{!?_without_numad:1}
        %endif
    %endif
%endif

# Force QEMU to run as qemu:qemu
%define qemu_user          qemu
%define qemu_group         qemu

%if %{with_firewalld}
    %define _fwdefdir %{_prefix}/lib/firewalld/services
%else
    %define _fwdefdir /etc/sysconfig/SuSEfirewall2.d/services
%endif

%if %{with_wireshark}
    %define wireshark_plugindir %(pkg-config --variable plugindir wireshark)/epan
%endif

Name:           libvirt
URL:            http://libvirt.org/
Version:        5.10.0
Release:        0
Summary:        Library providing a virtualization API
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++

Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-daemon-config-network = %{version}-%{release}
Requires:       %{name}-daemon-config-nwfilter = %{version}-%{release}
%if %{with_libxl}
Requires:       %{name}-daemon-driver-libxl = %{version}-%{release}
%endif
%if %{with_lxc}
Requires:       %{name}-daemon-driver-lxc = %{version}-%{release}
%endif
%if %{with_qemu}
Requires:       %{name}-daemon-driver-qemu = %{version}-%{release}
%endif
%if %{with_vbox}
Requires:       %{name}-daemon-driver-vbox = %{version}-%{release}
%endif
Requires:       %{name}-client = %{version}-%{release}
Requires:       %{name}-daemon-driver-interface = %{version}-%{release}
Requires:       %{name}-daemon-driver-network = %{version}-%{release}
Requires:       %{name}-daemon-driver-nodedev = %{version}-%{release}
Requires:       %{name}-daemon-driver-nwfilter = %{version}-%{release}
Requires:       %{name}-daemon-driver-secret = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

# All build-time requirements. Run-time requirements are
# listed against each sub-RPM
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  libtool
# Needed for virkmodtest in 'make check'
BuildRequires:  modutils
BuildRequires:  pkgconfig(systemd)
%if %{with_libxl}
BuildRequires:  xen-devel
%endif
%if %{with_qemu}
# For managing ACLs
BuildRequires:  libacl-devel
%endif
%if %{with_bash_completion}
BuildRequires:  bash-completion-devel >= 2.0
%endif
BuildRequires:  fdupes
BuildRequires:  glib2-devel >= 2.48
BuildRequires:  libattr-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libgnutls-devel
BuildRequires:  libtasn1-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt
BuildRequires:  perl
BuildRequires:  python3
BuildRequires:  readline-devel
# rpcgen is needed since we have a patch touching remote_protocol.x
BuildRequires:  rpcgen
# For pool-build probing for existing pools
BuildRequires:  libblkid-devel >= 2.17
BuildRequires:  libpciaccess0-devel >= 0.10.9
BuildRequires:  libudev-devel >= 145
BuildRequires:  libyajl-devel
%if %{with_sanlock}
BuildRequires:  sanlock-devel >= 2.4
%endif
BuildRequires:  libnl3-devel
BuildRequires:  libpcap-devel
BuildRequires:  libselinux-devel
%if 0%{?suse_version} >= 1330
BuildRequires:  libtirpc-devel
%endif
%if %{with_apparmor}
BuildRequires:  apparmor-rpm-macros
BuildRequires:  libapparmor-devel
%endif
BuildRequires:  cyrus-sasl-devel
BuildRequires:  dnsmasq >= 2.41
BuildRequires:  ebtables
BuildRequires:  iptables
BuildRequires:  polkit >= 0.112
BuildRequires:  radvd
# Communication with the firewall and polkit daemons use DBus
BuildRequires:  dbus-1-devel
# For mount/umount in FS driver
BuildRequires:  util-linux
# For LVM drivers
BuildRequires:  lvm2
# For pool type=iscsi
BuildRequires:  open-iscsi
%if %{with_storage_iscsi_direct}
# For pool type=iscsi-direct
BuildRequires:  libiscsi-devel
%endif
# For disk driver
BuildRequires:  parted-devel
# For Multipath support
BuildRequires:  device-mapper-devel
# For XFS reflink clone support
BuildRequires:  xfsprogs-devel
%if %{with_storage_rbd}
BuildRequires:  %{with_rbd_lib}
%endif
%if %{with_storage_gluster}
BuildRequires:  glusterfs-devel >= 3.4.1
%endif
%if %{with_numactl}
# For QEMU/LXC numa info
BuildRequires:  libnuma-devel
%endif
BuildRequires:  fuse-devel >= 2.8.6
BuildRequires:  libcap-ng-devel >= 0.5.0
BuildRequires:  libnetcontrol-devel >= 0.2.0
%if %{with_libssh2}
BuildRequires:  libssh2-devel
%endif
%if %{with_esx}
BuildRequires:  libcurl-devel
%endif
%if %{with_hyperv}
BuildRequires:  libwsman-devel >= 2.2.3
%endif
BuildRequires:  audit-devel
# we need /usr/sbin/dtrace
BuildRequires:  systemtap-sdt-devel
%if %{with_numad}
BuildRequires:  numad
%endif
%if %{with_wireshark}
BuildRequires:  wireshark-devel >= 2.4.0
%endif
%if %{with_libssh}
BuildRequires:  libssh-devel >= 0.7.0
%endif
%if %{with_firewalld}
BuildRequires:  firewall-macros
%endif

Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        libvirtd-relocation-server.fw
Source4:        libvirt-supportconfig
Source5:        suse-qemu-domain-hook.py
Source6:        libvirtd-relocation-server.xml
Source99:       baselibs.conf
Source100:      %{name}-rpmlintrc
# Upstream patches
Patch0:         0a65cba4-news-fix.patch
# Patches pending upstream review
Patch100:       libxl-dom-reset.patch
Patch101:       network-don-t-use-dhcp-authoritative-on-static-netwo.patch
# Need to go upstream
Patch150:       libvirt-power8-models.patch
Patch151:       ppc64le-canonical-name.patch
Patch152:       libxl-set-migration-constraints.patch
Patch153:       libxl-set-cach-mode.patch
Patch154:       0001-Extract-stats-functions-from-the-qemu-driver.patch
Patch155:       0002-lxc-implement-connectGetAllDomainStats.patch
Patch156:       0001-libxl-add-support-for-BlockResize-API.patch
# Our patches
Patch200:       suse-libvirtd-disable-tls.patch
Patch201:       suse-libvirtd-sysconfig-settings.patch
Patch202:       suse-libvirt-guests-service.patch
Patch203:       suse-virtlockd-sysconfig-settings.patch
Patch204:       suse-virtlogd-sysconfig-settings.patch
Patch205:       suse-qemu-conf.patch
Patch206:       suse-ovmf-paths.patch
Patch207:       suse-apparmor-libnl-paths.patch
Patch208:       support-managed-pci-xen-driver.patch
Patch209:       libxl-support-block-script.patch
Patch210:       qemu-apparmor-screenshot.patch
Patch211:       libvirt-suse-netcontrol.patch
Patch212:       lxc-wait-after-eth-del.patch
Patch213:       suse-libxl-disable-autoballoon.patch
# SLES-Only patches
%if ! 0%{?is_opensuse}
Patch400:       virt-create-rootfs.patch
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libvirt is a C toolkit to interact with the virtualization
capabilities of Linux. Virtualization of the Linux Operating System means
the ability to run multiple instances of Operating Systems concurrently
on a single hardware system where the basic resources are driven by a
Linux instance. The library aims to provide long term stable C API
to interact with Linux virtualization technologies.

%package doc
Summary:        API reference and website documentation for libvirt
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
The API reference for the libvirt C library, and a
copy of the libvirt.org website documentation.

%package daemon
Summary:        Server side daemon and supporting files for libvirt
Group:          System/Management

# All runtime requirements for the libvirt package (runtime requirements
# for subpackages are listed later in those subpackages)

Requires:       %{name}-libs = %{version}-%{release}

# for modprobe of pci devices
Requires:       modutils
# for /sbin/ip & /sbin/tc
Requires:       iproute
Requires:       logrotate
Requires:       udev >= 145
Recommends:     polkit >= 0.112
%ifarch %ix86 x86_64 ia64
# For virConnectGetSysinfo
Requires:       dmidecode
%endif
# For service management
%{?systemd_requires}
%if %{with_numad}
Requires:       numad
%endif
# libvirtd depends on 'messagebus' service
Requires:       dbus-1

# libvirt is configured with paths to UEFI firmwares in %build,
# hence add a dependency to the firmware packages
%ifarch x86_64
Requires:       qemu-ovmf-x86_64
%endif
%ifarch aarch64
Requires:       qemu-uefi-aarch64
%endif
%if %{with_apparmor}
Requires:       apparmor-abstractions
%endif

%description daemon
Server side daemon required to manage the virtualization capabilities
of recent versions of Linux. Requires a hypervisor specific sub-RPM
for specific drivers.

%package daemon-hooks
Summary:        Hook scripts for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       python3-lxml

%description daemon-hooks
Default hook scripts for the libvirt daemon

%package daemon-config-network
Summary:        Default configuration files for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-daemon-driver-network = %{version}-%{release}

%description daemon-config-network
Default configuration files for setting up NAT based networking

%package daemon-config-nwfilter
Summary:        Network filter configuration files for the libvirtd
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-daemon-driver-nwfilter = %{version}-%{release}

%description daemon-config-nwfilter
Network filter configuration files for the libvirt daemon, used for
cleaning guest network traffic.

%package daemon-driver-network
Summary:        Network driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       dnsmasq >= 2.41
Requires:       iptables
Requires:       radvd

%description daemon-driver-network
The network driver plugin for the libvirtd daemon, providing
an implementation of the virtual network APIs using the Linux
bridge capabilities.

%package daemon-driver-nwfilter
Summary:        A nwfilter driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       ebtables
Requires:       iptables

%description daemon-driver-nwfilter
The nwfilter driver plugin for the libvirtd daemon, providing
an implementation of the firewall APIs using the ebtables,
iptables and ip6tables capabilities

%package daemon-driver-nodedev
Summary:        Nodedev driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-nodedev
The nodedev driver plugin for the libvirtd daemon, providing
an implementation of the node device APIs using the udev
capabilities.

%package daemon-driver-interface
Summary:        Interface driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-interface
The interface driver plugin for the libvirtd daemon, providing
an implementation of the network interface APIs using the
netcontrol library

%package daemon-driver-secret
Summary:        Secret driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}

%description daemon-driver-secret
The secret driver plugin for the libvirtd daemon, providing
an implementation of the secret key APIs.

%package daemon-driver-storage-core
Summary:        Storage driver plugin including base backends for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       nfs-utils
# For mkfs
Requires:       util-linux
%if %{with_qemu}
# From QEMU RPMs
Requires:       /usr/bin/qemu-img
%endif

%description daemon-driver-storage-core
The storage driver plugin for the libvirtd daemon, providing
an implementation of the storage APIs using files, local disks, LVM, SCSI,
iSCSI, and multipath storage.

%package daemon-driver-storage-logical
Summary:        Storage driver plugin for lvm volumes
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       lvm2

%description daemon-driver-storage-logical
The storage driver backend adding implementation of the storage APIs for block
volumes using lvm.

%package daemon-driver-storage-disk
Summary:        Storage driver plugin for disk
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       device-mapper
Requires:       parted

%description daemon-driver-storage-disk
The storage driver backend adding implementation of the storage APIs for block
volumes using the host disks.

%package daemon-driver-storage-scsi
Summary:        Storage driver plugin for local scsi devices
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-storage-scsi
The storage driver backend adding implementation of the storage APIs for scsi
host devices.

%package daemon-driver-storage-iscsi
Summary:        Storage driver plugin for iscsi
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       open-iscsi

%description daemon-driver-storage-iscsi
The storage driver backend adding implementation of the storage APIs for iscsi
volumes using the host iscsi stack.

%package daemon-driver-storage-iscsi-direct
Summary:        Storage driver plugin for iscsi-direct
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-storage-iscsi-direct
The storage driver backend adding implementation of the storage APIs for iscsi
volumes using libiscsi direct connection.

%package daemon-driver-storage-mpath
Summary:        Storage driver plugin for multipath volumes
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       device-mapper

%description daemon-driver-storage-mpath
The storage driver backend adding implementation of the storage APIs for
multipath storage using device mapper.

%package daemon-driver-storage-gluster
Summary:        Storage driver plugin for gluster
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-storage-gluster
The storage driver backend adding implementation of the storage APIs for gluster
volumes using libgfapi.

%package daemon-driver-storage-rbd
Summary:        Storage driver plugin for rbd
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-storage-rbd
The storage driver backend adding implementation of the storage APIs for rbd
volumes using the ceph protocol.

%package daemon-driver-storage-sheepdog
Summary:        Storage driver plugin for sheepdog
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       sheepdog

%description daemon-driver-storage-sheepdog
The storage driver backend adding implementation of the storage APIs for
sheepdog volumes using.

%package daemon-driver-storage
Summary:        Storage driver plugin including all backends for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon-driver-storage-core = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage-disk = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage-iscsi = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage-logical = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage-mpath = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage-scsi = %{version}-%{release}
%if %{with_storage_gluster}
Requires:       %{name}-daemon-driver-storage-gluster = %{version}-%{release}
%endif
%if %{with_storage_rbd}
Requires:       %{name}-daemon-driver-storage-rbd = %{version}-%{release}
%endif
%if %{with_storage_sheepdog}
Requires:       %{name}-daemon-driver-storage-sheepdog = %{version}-%{release}
%endif
%if %{with_storage_iscsi_direct}
Requires:       %{name}-daemon-driver-storage-iscsi-direct = %{version}-%{release}
%endif

%description daemon-driver-storage
The storage driver plugin for the libvirtd daemon, providing
an implementation of the storage APIs using LVM, iSCSI,
parted and more.

%package daemon-driver-qemu
Summary:        Qemu driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       /usr/bin/qemu-img
# For image compression
Requires:       bzip2
Requires:       gzip
Requires:       lzop
Requires:       qemu
Requires:       systemd-container
Requires:       xz

%description daemon-driver-qemu
The qemu driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using QEMU.

%package daemon-driver-lxc
Summary:        LXC driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
# There really is a hard cross-driver dependency here
Requires:       %{name}-daemon-driver-network = %{version}-%{release}
Requires:       systemd-container

%description daemon-driver-lxc
The LXC driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
the Linux kernel

%package daemon-driver-vbox
Summary:        VirtualBox driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-vbox
The vbox driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using
VirtualBox

%package daemon-driver-libxl
Summary:        Libxl driver plugin for the libvirtd daemon
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}

%description daemon-driver-libxl
The Libxl driver plugin for the libvirtd daemon, providing
an implementation of the hypervisor driver APIs using libxl.

%package daemon-qemu
Summary:        Server side daemon & driver required to run QEMU guests
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-daemon-driver-interface = %{version}-%{release}
Requires:       %{name}-daemon-driver-network = %{version}-%{release}
Requires:       %{name}-daemon-driver-nodedev = %{version}-%{release}
Requires:       %{name}-daemon-driver-nwfilter = %{version}-%{release}
Requires:       %{name}-daemon-driver-qemu = %{version}-%{release}
Requires:       %{name}-daemon-driver-secret = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage = %{version}-%{release}

%description daemon-qemu
Server side daemon and driver required to manage the virtualization
capabilities of the QEMU emulators

%package daemon-lxc
Summary:        Server side daemon & driver required to run LXC guests
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-daemon-driver-interface = %{version}-%{release}
Requires:       %{name}-daemon-driver-lxc = %{version}-%{release}
Requires:       %{name}-daemon-driver-network = %{version}-%{release}
Requires:       %{name}-daemon-driver-nodedev = %{version}-%{release}
Requires:       %{name}-daemon-driver-nwfilter = %{version}-%{release}
Requires:       %{name}-daemon-driver-secret = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage = %{version}-%{release}

%description daemon-lxc
Server side daemon and driver required to manage the virtualization
capabilities of LXC

%package daemon-xen
Summary:        Server side daemon & driver required to run XEN guests
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-daemon-driver-interface = %{version}-%{release}
Requires:       %{name}-daemon-driver-libxl = %{version}-%{release}
Requires:       %{name}-daemon-driver-network = %{version}-%{release}
Requires:       %{name}-daemon-driver-nodedev = %{version}-%{release}
Requires:       %{name}-daemon-driver-nwfilter = %{version}-%{release}
Requires:       %{name}-daemon-driver-secret = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage = %{version}-%{release}
Requires:       xen

%description daemon-xen
Server side daemon and driver required to manage the virtualization
capabilities of XEN

%package daemon-vbox
Summary:        Server side daemon & driver required to run VirtualBox guests
Group:          System/Management
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-daemon-driver-interface = %{version}-%{release}
Requires:       %{name}-daemon-driver-network = %{version}-%{release}
Requires:       %{name}-daemon-driver-nodedev = %{version}-%{release}
Requires:       %{name}-daemon-driver-nwfilter = %{version}-%{release}
Requires:       %{name}-daemon-driver-secret = %{version}-%{release}
Requires:       %{name}-daemon-driver-storage = %{version}-%{release}
Requires:       %{name}-daemon-driver-vbox = %{version}-%{release}
# Specify supported virtualbox API explicitly. See ./src/vbox
# Reference bsc#1017189 
Requires:       virtualbox < 5.3

%description daemon-vbox
Server side daemon and driver required to manage the virtualization
capabilities of VirtualBox

%package client
Summary:        Client side utilities of the libvirt library
Group:          System/Management
Requires:       %{name}-libs = %{version}-%{release}
Requires:       readline
# Needed by libvirt-guests init script.
Requires:       gettext-runtime
# Needed by virt-pki-validate script.
Requires:       cyrus-sasl
Requires:       gnutls
%if %{with_bash_completion}
Recommends:     %{name}-bash-completion = %{version}-%{release}
%endif

%description client
The client binaries needed to access the virtualization
capabilities of recent versions of Linux (and other OSes).

%package libs
Summary:        Client side libraries for libvirt
# So remote clients can access libvirt over SSH tunnel
# (client invokes 'nc' against the UNIX socket on the server)
Group:          System/Libraries
Requires:       netcat-openbsd
# Not technically required, but makes 'out-of-box' config
# work correctly & doesn't have onerous dependencies
Requires:       cyrus-sasl-digestmd5

%description libs
Shared libraries for accessing the libvirt daemon.

%package admin
Summary:        Set of tools to control libvirt daemon
Group:          System/Management
Requires:       %{name}-libs = %{version}-%{release}
Requires:       readline
%if %{with_bash_completion}
Recommends:     %{name}-bash-completion = %{version}-%{release}
%endif

%description admin
The client side utilities to control the libvirt daemon.

%package bash-completion
Summary:        Bash completion script
Group:          System/Shells
BuildArch:      noarch

%description bash-completion
Bash completion script stub.

%package devel
Summary:        Libraries, includes, etc. to compile with the libvirt library
Group:          Development/Libraries/C and C++
Requires:       %{name}-client = %{version}-%{release}
Suggests:       %{name}-doc = %{version}-%{release}
Requires:       pkg-config

%description devel
Include header files & development libraries for the libvirt C library.

%package lock-sanlock
Summary:        Sanlock lock manager plugin for QEMU driver
Group:          System/Management
Requires:       sanlock >= 2.4
# for virt-sanlock-cleanup require augeas
Requires:       %{name}-daemon = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
Requires:       augeas

%description lock-sanlock
Includes the Sanlock lock manager plugin for the QEMU driver

%package -n wireshark-plugin-libvirt
Summary:        Wireshark plugin for libvirt RPC protocol
Group:          Productivity/Networking/Diagnostic
Requires:       %{name}-libs = %{version}-%{release}
Requires:       wireshark >= 2.4.0

%description -n wireshark-plugin-libvirt
Wireshark dissector plugin for better analysis of libvirt RPC traffic.

%package nss
Summary:        Libvirt plugin for Name Service Switch
Group:          System/Management
Requires:       %{name}-daemon-driver-network = %{version}-%{release}

%description nss
libvirt plugin for NSS for translating domain names into IP addresses.

%prep
%setup -q
%patch0 -p1
%patch100 -p1
%patch101 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch200 -p1
%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch204 -p1
%patch205 -p1
%patch206 -p1
%patch207 -p1
%patch208 -p1
%patch209 -p1
%patch210 -p1
%patch211 -p1
%patch212 -p1
%patch213 -p1
%if ! 0%{?is_opensuse}
%patch400 -p1
%endif

%build
%if %{with_qemu}
    %define arg_qemu --with-qemu
%else
    %define arg_qemu --without-qemu
%endif
%if %{with_openvz}
    %define arg_openvz --with-openvz
%else
    %define arg_openvz --without-openvz
%endif
%if %{with_lxc}
    %define arg_lxc --with-lxc
%else
    %define arg_lxc --without-lxc
%endif
%if %{with_vbox}
    %define arg_vbox --with-vbox
%else
    %define arg_vbox --without-vbox
%endif
%if %{with_phyp}
    %define arg_phyp --with-phyp
%else
    %define arg_phyp --without-phyp
%endif
%if %{with_esx}
    %define arg_esx --with-esx
%else
    %define arg_esx --without-esx
%endif
%if %{with_vmware}
    %define arg_vmware --with-vmware
%else
    %define arg_vmware --without-vmware
%endif
%if %{with_hyperv}
    %define arg_hyperv --with-hyperv
%else
    %define arg_hyperv --without-hyperv
%endif
%if %{with_libxl}
    %define arg_libxl --with-libxl
%else
    %define arg_libxl --without-libxl
%endif
%if %{with_storage_rbd}
    %define arg_storage_rbd --with-storage-rbd
%else
    %define arg_storage_rbd --without-storage-rbd
%endif
%if %{with_storage_sheepdog}
    %define arg_storage_sheepdog --with-storage-sheepdog
%else
    %define arg_storage_sheepdog --without-storage-sheepdog
%endif
%if %{with_storage_gluster}
    %define arg_storage_gluster --with-storage-gluster
%else
    %define arg_storage_gluster --without-storage-gluster
%endif
%if %{with_storage_iscsi_direct}
    %define arg_storage_iscsi_direct --with-storage-iscsi-direct
%else
    %define arg_storage_iscsi_direct --without-storage-iscsi-direct
%endif
%if %{with_numactl}
    %define arg_numactl --with-numactl
%else
    %define arg_numactl --without-numactl
%endif
%if %{with_numad}
    %define arg_numad --with-numad
%else
    %define arg_numad --without-numad
%endif
%if %{with_apparmor}
    %define arg_apparmor --with-apparmor
    %define arg_apparmor_profiles --with-apparmor-profiles
%else
    %define arg_apparmor --without-apparmor
%endif
%if %{with_sanlock}
    %define arg_sanlock --with-sanlock
%else
    %define arg_sanlock --without-sanlock
%endif
%if %{with_firewalld}
    %define arg_firewalld --with-firewalld
%else
    %define arg_firewalld --without-firewalld
%endif
%if %{with_firewalld_zone}
    %define arg_firewalld_zone --with-firewalld-zone
%else
    %define arg_firewalld_zone --without-firewalld-zone
%endif
%if %{with_wireshark}
    %define arg_wireshark --with-wireshark-dissector
%else
    %define arg_wireshark --without-wireshark-dissector
%endif

%define arg_selinux_mount --with-selinux-mount="/selinux"

# UEFI firmwares
# For SLE15 SP2 (Leap 15.2) and newer, use firmware descriptor files from the
# firmware packages, otherwise define firmwares via configure option
%if ! (0%{?suse_version} > 1500 || 0%{?sle_version} > 150100)
    # x86_64 UEFI firmwares
    # To more closely resemble actual hardware, we use the firmwares with
    # embedded Microsoft keys
    #
    # The Windows HCK test requires a bigger variable store, so 4MB firmware
    # images have been introduced. They are advertised first and will be
    # used by default for new VM installations. The 2MB images are still
    # available for existing VMs, and can be selected for new installations
    # as well.
    LOADERS="/usr/share/qemu/ovmf-x86_64-ms-4m-code.bin:/usr/share/qemu/ovmf-x86_64-ms-4m-vars.bin"
    LOADERS="$LOADERS:/usr/share/qemu/ovmf-x86_64-ms-code.bin:/usr/share/qemu/ovmf-x86_64-ms-vars.bin"
    # aarch64 UEFI firmwares
    LOADERS="$LOADERS:/usr/share/qemu/aavmf-aarch64-code.bin:/usr/share/qemu/aavmf-aarch64-vars.bin"
    %define arg_loader_nvram --with-loader-nvram="$LOADERS"
%endif

autoreconf -f -i
%define _configure ../configure
mkdir %{_vpath_builddir}
cd %{_vpath_builddir}
export CFLAGS="%{optflags}"
export PYTHON=%{_bindir}/python3
%configure --disable-static \
	   --enable-dependency-tracking \
	   --with-runstatedir=%{_rundir} \
           %{?arg_qemu} \
           %{?arg_openvz} \
           %{?arg_lxc} \
           %{?arg_vbox} \
           %{?arg_libxl} \
           --with-sasl \
           --with-polkit \
           --with-libvirtd \
           %{?arg_phyp} \
           %{?arg_esx} \
           %{?arg_hyperv} \
           %{?arg_vmware} \
           --without-vz \
           --without-bhyve \
           --with-remote-default-mode=legacy \
           --with-interface \
           --with-network \
           --with-storage-fs \
           --with-storage-lvm \
           --with-storage-iscsi \
           --with-storage-scsi \
           --with-storage-disk \
           --with-storage-mpath \
           %{?arg_storage_rbd} \
           %{?arg_storage_sheepdog} \
           %{?arg_storage_gluster} \
           %{?arg_storage_iscsi_direct} \
           --without-storage-zfs \
           --without-storage-vstorage \
           %{?arg_numactl} \
           %{?arg_numad} \
           --with-capng \
           --with-fuse \
           --without-netcf \
           --with-netcontrol \
           --with-selinux \
           %{?arg_selinux_mount} \
           %{?arg_apparmor} \
           %{?arg_apparmor_profiles} \
           --with-udev \
           --with-yajl \
           %{?arg_sanlock} \
           --with-libpcap \
           --with-macvtap \
           --with-audit \
           --with-dtrace \
           --with-driver-modules \
           %{?arg_firewalld} \
           %{?arg_firewalld_zone} \
           %{?arg_wireshark} \
           --with-nss-plugin \
           --libexecdir=%{_libdir}/%{name} \
           --with-qemu-user=%{qemu_user} \
           --with-qemu-group=%{qemu_group} \
           %{?arg_loader_nvram} \
           --without-login-shell \
           --with-init-script=systemd \
           ac_cv_path_MODPROBE=/sbin/modprobe \
           ac_cv_path_UDEVADM=/sbin/udevadm \
           ac_cv_path_SHOWMOUNT=/usr/sbin/showmount \
           ac_cv_path_PARTED=/usr/sbin/parted \
           ac_cv_path_QEMU_BRIDGE_HELPER=/usr/lib/qemu-bridge-helper
%make_build HTML_DIR=%{_docdir}/%{name}

%install
cd %{_vpath_builddir}
%make_install SYSTEMD_UNIT_DIR=%{_unitdir} HTML_DIR=%{_docdir}/%{name}
cp ../examples/sh/virt-lxc-convert %{buildroot}/%{_bindir}
rm -f %{buildroot}/%{_libdir}/*.la
%if %{with_wireshark}
rm -f %{buildroot}/%{wireshark_plugindir}/libvirt.la
%endif
rm -f %{buildroot}/%{_libdir}/*.a
rm -f %{buildroot}/%{_libdir}/%{name}/lock-driver/*.la
rm -f %{buildroot}/%{_libdir}/%{name}/lock-driver/*.a
rm -f %{buildroot}/%{_libdir}/%{name}/connection-driver/*.la
rm -f %{buildroot}/%{_libdir}/%{name}/connection-driver/*.a
rm -f %{buildroot}/%{_libdir}/%{name}/storage-backend/*.la
rm -f %{buildroot}/%{_libdir}/%{name}/storage-backend/*.a
rm -f %{buildroot}/%{_libdir}/%{name}/storage-file/*.la
rm -f %{buildroot}/%{_libdir}/%{name}/storage-file/*.a
# remove currently unsupported locale(s)
for dir in %{buildroot}/usr/share/locale/*
do
  sdir=`echo $dir | sed "s|%{buildroot}||"`
  if test -d $sdir ; then continue ; fi
  rm -rfv "$dir"
done

mkdir -p %{buildroot}/%{_localstatedir}/lib/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}/hooks
%find_lang %{name}
# Add a README to the libvirt package with a note about the empty
# file list
cat > %{buildroot}/%{_docdir}/%{name}/libvirt.README << 'EOF'
The libvirt package no longer contains any files.  It exists now
only to fulfill its 'Provides' contract.
EOF
install -d -m 0755 %{buildroot}/%{_localstatedir}/lib/%{name}/dnsmasq/
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}/networks/
cp %{buildroot}/%{_sysconfdir}/%{name}/qemu/networks/default.xml \
   %{buildroot}/%{_datadir}/%{name}/networks/default.xml
rm -f %{buildroot}/%{_sysconfdir}/%{name}/qemu/networks/default.xml
rm -f %{buildroot}/%{_sysconfdir}/%{name}/qemu/networks/autostart/default.xml
# Strip auto-generated UUID - we need it generated per-install
sed -i -e "/<uuid>/d" %{buildroot}/%{_datadir}/%{name}/networks/default.xml
%if %{with_lxc}
cat > %{buildroot}/%{_docdir}/%{name}/libvirt-daemon-lxc.README << 'EOF'
Any empty package encapsulating requirements for a libvirtd capable
of managing LXC.
EOF
%else
rm -rf %{buildroot}/%{_sysconfdir}/%{name}/lxc.conf
rm -f %{buildroot}/%{_datadir}/augeas/lenses/libvirtd_lxc.aug
rm -f %{buildroot}/%{_datadir}/augeas/lenses/tests/test_libvirtd_lxc.aug
rm -rf %{buildroot}/%{_sysconfdir}/logrotate.d/libvirtd.lxc
%endif
%if %{with_qemu}
cat > %{buildroot}/%{_docdir}/%{name}/libvirt-daemon-qemu.README << 'EOF'
Any empty package encapsulating requirements for a libvirtd capable
of managing QEMU/KVM.
EOF
%else
rm -rf %{buildroot}/%{_sysconfdir}/%{name}/qemu.conf
rm -f %{buildroot}/%{_datadir}/augeas/lenses/libvirtd_qemu.aug
rm -f %{buildroot}/%{_datadir}/augeas/lenses/tests/test_libvirtd_qemu.aug
rm -rf %{buildroot}/%{_sysconfdir}/logrotate.d/libvirtd.qemu
%endif
%if %{with_vbox}
cat > %{buildroot}/%{_docdir}/%{name}/libvirt-daemon-vbox.README << 'EOF'
Any empty package encapsulating requirements for a libvirtd capable
of managing VirtualBox.
EOF
%endif
%if %{with_libxl}
cat > %{buildroot}/%{_docdir}/%{name}/libvirt-daemon-xen.README << 'EOF'
Any empty package encapsulating requirements for a libvirtd capable
of managing Xen.
EOF
%endif
%if ! %{with_libxl}
rm -f %{buildroot}/%{_sysconfdir}/%{name}/libxl.conf
rm -f %{buildroot}/%{_sysconfdir}/logrotate.d/libvirtd.libxl
rm -f %{buildroot}/%{_datadir}/augeas/lenses/libvirtd_libxl.aug
rm -f %{buildroot}/%{_datadir}/augeas/lenses/tests/test_libvirtd_libxl.aug
%endif
%if ! %{with_sanlock}
rm -f %{buildroot}/%{_datadir}/augeas/lenses/libvirt_sanlock.aug
rm -f %{buildroot}/%{_datadir}/augeas/lenses/tests/test_libvirt_sanlock.aug
%endif

# init scripts
mkdir -p %{buildroot}/%{_fillupdir}
rm -f %{buildroot}/usr/lib/sysctl.d/60-libvirtd.conf
mv %{buildroot}/%{_sysconfdir}/sysconfig/libvirtd %{buildroot}%{_fillupdir}/sysconfig.libvirtd
mv %{buildroot}/%{_sysconfdir}/sysconfig/virtlogd %{buildroot}/%{_fillupdir}/sysconfig.virtlogd
mv %{buildroot}/%{_sysconfdir}/sysconfig/virtlockd %{buildroot}/%{_fillupdir}/sysconfig.virtlockd
mv %{buildroot}/%{_sysconfdir}/sysconfig/libvirt-guests %{buildroot}/%{_fillupdir}/sysconfig.libvirt-guests
# Provide rc symlink backward compatibility
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rclibvirtd
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcvirtlogd
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcvirtlockd
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rclibvirt-guests

# install firewall services for migration ports
mkdir -p %{buildroot}/%{_fwdefdir}
%if %{with_firewalld}
install -m 644 %{S:6} %{buildroot}/%{_fwdefdir}/libvirtd-relocation-server.xml
%else
# Format described in /usr/share/SuSEfirewall2/services/TEMPLATE
install -m 644 %{S:3} %{buildroot}/%{_fwdefdir}/libvirtd-relocation-server
%endif

# install supportconfig plugin
mkdir -p %{buildroot}/usr/lib/supportconfig/plugins
install -m 755 %{S:4} %{buildroot}/usr/lib/supportconfig/plugins/libvirt

# install qemu hook script
install -m 755 %{S:5} %{buildroot}/%{_sysconfdir}/%{name}/hooks/qemu

%ifarch %{power64} s390x x86_64
mv %{buildroot}/%{_datadir}/systemtap/tapset/libvirt_probes.stp \
   %{buildroot}/%{_datadir}/systemtap/tapset/libvirt_probes-64.stp
%if %{with_qemu}
mv %{buildroot}/%{_datadir}/systemtap/tapset/libvirt_qemu_probes.stp \
   %{buildroot}/%{_datadir}/systemtap/tapset/libvirt_qemu_probes-64.stp
%endif
%endif
%fdupes -s %{buildroot}

%check
cd tests
SKIP_TESTS=""
# These tests don't current work in a mock build root
# virnetsockettest: needs unsupported linux-user syscalls
SKIP_TESTS="$SKIP_TESTS virnetsockettest"
# virportallocatortest fails on aarch64 due to unsupported IPV6_V6ONLY flag
%ifarch aarch64
SKIP_TESTS="$SKIP_TESTS virportallocatortest"
%endif
for i in $SKIP_TESTS
do
  rm -f $i
  printf 'int main(void) { return 0; }' > $i.c
done
cd ../%{_vpath_builddir}
if ! %make_build check VIR_TEST_DEBUG=1
then
  cat tests/test-suite.log || true
  exit 1
fi

%pre daemon
%{_bindir}/getent group libvirt >/dev/null || %{_sbindir}/groupadd -r libvirt
%service_add_pre libvirtd.service virtlockd.service virtlockd.socket virtlogd.service virtlogd.socket virtlockd-admin.socket virtlogd-admin.socket

%post daemon
/sbin/ldconfig
%if %{with_apparmor}
%apparmor_reload /etc/apparmor.d/usr.sbin.libvirtd
%endif
%if %{with_firewalld}
%firewalld_reload
%endif
%service_add_post libvirtd.service libvirtd.socket libvirtd-ro.socket libvirtd-admin.socket libvirtd-tcp.socket libvirtd-tls.socket virtlockd.service virtlockd.socket virtlogd.service virtlogd.socket virtlockd-admin.socket virtlogd-admin.socket virtproxyd.service virtproxyd.socket virtproxyd-ro.socket virtproxyd-admin.socket virtproxyd-tcp.socket virtproxyd-tls.socket
%{fillup_only -n libvirtd}
%{fillup_only -n virtlockd}
%{fillup_only -n virtlogd}
# The '--listen' option is incompatible with socket activation.
# We need to forcibly remove it from /etc/sysconfig/libvirtd.
# Also add the --timeout option to be consistent with upstream.
# See boo#1156161 for details
sed -i -e '/^\s*LIBVIRTD_ARGS=/s/--listen//g' %{_sysconfdir}/sysconfig/libvirtd
if ! grep -q -E '^\s*LIBVIRTD_ARGS=.*--timeout' %{_sysconfdir}/sysconfig/libvirtd ; then
    sed -i 's/^\s*LIBVIRTD_ARGS="\(.*\)"/LIBVIRTD_ARGS="\1 --timeout 120"/' %{_sysconfdir}/sysconfig/libvirtd
fi

%preun daemon
%service_del_preun libvirtd.service libvirtd.socket libvirtd-ro.socket libvirtd-admin.socket libvirtd-tcp.socket libvirtd-tls.socket virtlockd.service virtlockd.socket virtlogd.service virtlogd.socket virtlockd-admin.socket virtlogd-admin.socket

%postun daemon
/sbin/ldconfig
# On upgrade, defer restarting daemons until posttrans
if test $1 -eq 0 ; then
    for service in libvirtd virtlockd virtlogd ; do
        rm -f "/var/lib/systemd/migrated/$service" 2> /dev/null || :
    done
    /usr/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%service_del_postun libvirtd.service virtlockd.service virtlockd.socket virtlogd.service virtlogd.socket virtlockd-admin.socket virtlogd-admin.socket

%posttrans daemon
# All connection drivers should be installed post transaction.
# Time to restart libvirtd. With new socket activation we need to be a bit
# smarter on update. Old libvirtd owns the sockets and will delete them on
# shutdown. We can't use try-restart as libvirtd will own the sockets again
# after restart. So we must instead shutdown libvirtd, start the sockets,
# then start libvirtd.
if test "$YAST_IS_RUNNING" != "instsys" -a "$DISABLE_RESTART_ON_UPDATE" != yes ; then
    /usr/bin/systemctl is-active libvirtd.service >/dev/null 2>&1
    if test $? = 0 ; then
        /usr/bin/systemctl stop libvirtd.service >/dev/null 2>&1 || :

        /usr/bin/systemctl try-restart libvirtd.socket >/dev/null 2>&1 || :
        /usr/bin/systemctl try-restart libvirtd-ro.socket >/dev/null 2>&1 || :

        /usr/bin/systemctl start libvirtd.service >/dev/null 2>&1 || :
    fi
fi

%pre daemon-driver-network
%service_add_pre virtnetworkd.service virtnetworkd.socket virtnetworkd-ro.socket virtnetworkd-admin.socket

%post daemon-driver-network
%service_add_post virtnetworkd.service virtnetworkd.socket virtnetworkd-ro.socket virtnetworkd-admin.socket
%{fillup_only -n virtnetworkd}
%if %{with_firewalld_zone}
    %firewalld_reload
%endif

%preun daemon-driver-network
%service_del_preun virtnetworkd.service virtnetworkd.socket virtnetworkd-ro.socket virtnetworkd-admin.socket

%postun daemon-driver-network
%service_del_postun virtnetworkd.service virtnetworkd.socket virtnetworkd-ro.socket virtnetworkd-admin.socket
%if %{with_firewalld_zone}
    %firewalld_reload
%endif

%post daemon-config-network
# Install the default network if one doesn't exist
if test $1 -eq 1 && test ! -f %{_sysconfdir}/%{name}/qemu/networks/default.xml ; then
    UUID=`/usr/bin/uuidgen`
    sed -e "s,</name>,</name>\n  <uuid>$UUID</uuid>," \
         < %{_datadir}/%{name}/networks/default.xml \
         > %{_sysconfdir}/%{name}/qemu/networks/default.xml
    # libvirt saves this file with mode 0600
    chmod 0600 %{_sysconfdir}/libvirt/qemu/networks/default.xml
fi

%pre daemon-driver-nwfilter
%service_add_pre virtnwfilterd.service virtnwfilterd.socket virtnwfilterd-ro.socket virtnwfilterd-admin.socket

%post daemon-driver-nwfilter
%service_add_post virtnwfilterd.service virtnwfilterd.socket virtnwfilterd-ro.socket virtnwfilterd-admin.socket
%{fillup_only -n virtnwfilterd}

%preun daemon-driver-nwfilter
%service_del_preun virtnwfilterd.service virtnwfilterd.socket virtnwfilterd-ro.socket virtnwfilterd-admin.socket

%postun daemon-driver-nwfilter
%service_del_postun virtnwfilterd.service virtnwfilterd.socket virtnwfilterd-ro.socket virtnwfilterd-admin.socket

%pre daemon-driver-storage
%service_add_pre virtstoraged.service virtstoraged.socket virtstoraged-ro.socket virtstoraged-admin.socket

%post daemon-driver-storage
%service_add_post virtstoraged.service virtstoraged.socket virtstoraged-ro.socket virtstoraged-admin.socket
%{fillup_only -n virtstoraged}

%preun daemon-driver-storage
%service_del_preun virtstoraged.service virtstoraged.socket virtstoraged-ro.socket virtstoraged-admin.socket

%postun daemon-driver-storage
%service_del_postun virtstoraged.service virtstoraged.socket virtstoraged-ro.socket virtstoraged-admin.socket

%pre daemon-driver-interface
%service_add_pre virtinterfaced.service virtinterfaced.socket virtinterfaced-ro.socket virtinterfaced-admin.socket

%post daemon-driver-interface
%service_add_post virtinterfaced.service virtinterfaced.socket virtinterfaced-ro.socket virtinterfaced-admin.socket
%{fillup_only -n virtinterfaced}

%preun daemon-driver-interface
%service_del_preun virtinterfaced.service virtinterfaced.socket virtinterfaced-ro.socket virtinterfaced-admin.socket

%postun daemon-driver-interface
%service_del_postun virtinterfaced.service virtinterfaced.socket virtinterfaced-ro.socket virtinterfaced-admin.socket

%pre daemon-driver-nodedev
%service_add_pre virtnodedevd.service virtnodedevd.socket virtnodedevd-ro.socket virtnodedevd-admin.socket

%post daemon-driver-nodedev
%service_add_post virtnodedevd.service virtnodedevd.socket virtnodedevd-ro.socket virtnodedevd-admin.socket
%{fillup_only -n virtnodedevd}

%preun daemon-driver-nodedev
%service_del_preun virtnodedevd.service virtnodedevd.socket virtnodedevd-ro.socket virtnodedevd-admin.socket

%postun daemon-driver-nodedev
%service_del_postun virtnodedevd.service virtnodedevd.socket virtnodedevd-ro.socket virtnodedevd-admin.socket

%pre daemon-driver-secret
%service_add_pre virtsecretd.service virtsecretd.socket virtsecretd-ro.socket virtsecretd-admin.socket

%post daemon-driver-secret
%service_add_post virtsecretd.service virtsecretd.socket virtsecretd-ro.socket virtsecretd-admin.socket
%{fillup_only -n virtsecretd}

%preun daemon-driver-secret
%service_del_preun virtsecretd.service virtsecretd.socket virtsecretd-ro.socket virtsecretd-admin.socket

%postun daemon-driver-secret
%service_del_postun virtsecretd.service virtsecretd.socket virtsecretd-ro.socket virtsecretd-admin.socket

%pre daemon-driver-qemu
%service_add_pre virtqemud.service virtqemud.socket virtqemud-ro.socket virtqemud-admin.socket

%post daemon-driver-qemu
%service_add_post virtqemud.service virtqemud.socket virtqemud-ro.socket virtqemud-admin.socket
%{fillup_only -n virtqemud}

%preun daemon-driver-qemu
%service_del_preun virtqemud.service virtqemud.socket virtqemud-ro.socket virtqemud-admin.socket

%postun daemon-driver-qemu
%service_del_postun virtqemud.service virtqemud.socket virtqemud-ro.socket virtqemud-admin.socket

%pre daemon-driver-lxc
%service_add_pre virtlxcd.service virtlxcd.socket virtlxcd-ro.socket virtlxcd-admin.socket

%post daemon-driver-lxc
%service_add_post virtlxcd.service virtlxcd.socket virtlxcd-ro.socket virtlxcd-admin.socket
%{fillup_only -n virtlxcd}

%preun daemon-driver-lxc
%service_del_preun virtlxcd.service virtlxcd.socket virtlxcd-ro.socket virtlxcd-admin.socket

%postun daemon-driver-lxc
%service_del_postun virtlxcd.service virtlxcd.socket virtlxcd-ro.socket virtlxcd-admin.socket

%pre daemon-driver-libxl
%service_add_pre virtxend.service virtxend.socket virtxend-ro.socket virtxend-admin.socket

%post daemon-driver-libxl
%service_add_post virtxend.service virtxend.socket virtxend-ro.socket virtxend-admin.socket
%{fillup_only -n virtxend}

%preun daemon-driver-libxl
%service_del_preun virtxend.service virtxend.socket virtxend-ro.socket virtxend-admin.socket

%postun daemon-driver-libxl
%service_del_postun virtxend.service virtxend.socket virtxend-ro.socket virtxend-admin.socket

%pre client
%service_add_pre libvirt-guests.service

%post client
%service_add_post libvirt-guests.service
%{fillup_only -n libvirt-guests}

%preun client
%service_del_preun libvirt-guests.service
if [ $1 = 0 ]; then
    rm -f /var/lib/%{name}/libvirt-guests
fi

%postun client
%service_del_postun -n libvirt-guests.service

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%post nss -p /sbin/ldconfig

%postun nss -p /sbin/ldconfig

%files
%doc %{_docdir}/%{name}/libvirt.README

%files daemon
%{_sbindir}/libvirtd
%{_sbindir}/virtproxyd
%{_sbindir}/virtlogd
%{_sbindir}/virtlockd
%dir %{_libdir}/%{name}
%dir %attr(0700, root, root) %{_sysconfdir}/%{name}/
%dir %attr(0700, root, root) %{_sysconfdir}/%{name}/hooks
%{_fillupdir}/sysconfig.libvirtd
%{_fillupdir}/sysconfig.virtlogd
%{_fillupdir}/sysconfig.virtlockd
%{_unitdir}/libvirtd.service
%{_unitdir}/libvirtd.socket
%{_unitdir}/libvirtd-ro.socket
%{_unitdir}/libvirtd-admin.socket
%{_unitdir}/libvirtd-tcp.socket
%{_unitdir}/libvirtd-tls.socket
%{_unitdir}/virtproxyd.service
%{_unitdir}/virtproxyd.socket
%{_unitdir}/virtproxyd-ro.socket
%{_unitdir}/virtproxyd-admin.socket
%{_unitdir}/virtproxyd-tcp.socket
%{_unitdir}/virtproxyd-tls.socket
%{_unitdir}/virt-guest-shutdown.target
%{_unitdir}/virtlogd.service
%{_unitdir}/virtlogd.socket
%{_unitdir}/virtlogd-admin.socket
%{_unitdir}/virtlockd.service
%{_unitdir}/virtlockd.socket
%{_unitdir}/virtlockd-admin.socket
%{_sbindir}/rclibvirtd
%{_sbindir}/rcvirtlogd
%{_sbindir}/rcvirtlockd
%config(noreplace) %{_sysconfdir}/%{name}/libvirtd.conf
%config(noreplace) %{_sysconfdir}/%{name}/virtproxyd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd
%config(noreplace) %{_sysconfdir}/%{name}/virtlogd.conf
%config(noreplace) %{_sysconfdir}/%{name}/virtlockd.conf
%dir %{_sysconfdir}/sasl2/
%config(noreplace) %{_sysconfdir}/sasl2/libvirt.conf
%dir %{_datadir}/augeas/
%dir %{_datadir}/augeas/lenses
%dir %{_datadir}/augeas/lenses/tests
%{_datadir}/augeas/lenses/libvirtd.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd.aug
%{_datadir}/augeas/lenses/virtlogd.aug
%{_datadir}/augeas/lenses/tests/test_virtlogd.aug
%{_datadir}/augeas/lenses/virtlockd.aug
%{_datadir}/augeas/lenses/tests/test_virtlockd.aug
%{_datadir}/augeas/lenses/virtproxyd.aug
%{_datadir}/augeas/lenses/tests/test_virtproxyd.aug
%{_datadir}/augeas/lenses/libvirt_lockd.aug
%{_datadir}/augeas/lenses/tests/test_libvirt_lockd.aug
%{_datadir}/systemtap/tapset/libvirt_probes*.stp
%{_datadir}/systemtap/tapset/libvirt_functions.stp
%if %{with_qemu}
%{_datadir}/systemtap/tapset/libvirt_qemu_probes*.stp
%endif
%dir %{_localstatedir}/lib/%{name}/
%dir %attr(0711, root, root) %{_localstatedir}/lib/%{name}/images/
%dir %attr(0711, root, root) %{_localstatedir}/lib/%{name}/filesystems/
%dir %attr(0711, root, root) %{_localstatedir}/lib/%{name}/boot/
%dir %attr(0711, root, root) %{_localstatedir}/cache/%{name}/
%dir %attr(0700, root, root) %{_localstatedir}/log/%{name}/
%dir %attr(0755, root, root) %{_libdir}/%{name}/lock-driver
%attr(0755, root, root) %{_libdir}/%{name}/lock-driver/lockd.so
%if %{with_polkit_rules}
%{_datadir}/polkit-1/rules.d/50-libvirt.rules
%endif
%{_datadir}/polkit-1/actions/org.libvirt.unix.policy
%{_datadir}/polkit-1/actions/org.libvirt.api.policy
%attr(0755, root, root) %{_libdir}/%{name}/libvirt_iohelper
%doc %{_mandir}/man8/libvirtd.8*
%doc %{_mandir}/man8/virtlogd.8*
%doc %{_mandir}/man8/virtlockd.8*
%doc %{_mandir}/man7/virkey*.7*
%if %{with_apparmor}
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/abstractions
%dir %{_sysconfdir}/apparmor.d/%{name}
%dir %{_sysconfdir}/apparmor.d/local
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.sbin.libvirtd
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.lib.libvirt.virt-aa-helper
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/libvirt-qemu
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/libvirt-lxc
%config(noreplace) %{_sysconfdir}/apparmor.d/%{name}/TEMPLATE.lxc
%config(noreplace) %{_sysconfdir}/apparmor.d/%{name}/TEMPLATE.qemu
%config(noreplace) %{_sysconfdir}/apparmor.d/local/usr.lib.libvirt.virt-aa-helper
%{_libdir}/%{name}/virt-aa-helper
%endif
%if %{with_firewalld}
%dir %{_prefix}/lib/firewalld
%dir %{_fwdefdir}
%{_fwdefdir}/libvirtd-relocation-server.xml
%else
%config %{_fwdefdir}/libvirtd-relocation-server
%endif
%dir /usr/lib/supportconfig
%dir /usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/libvirt

%files daemon-hooks
%{_sysconfdir}/%{name}/hooks/qemu

%files daemon-config-network
%dir %{_datadir}/%{name}/networks/
%{_datadir}/%{name}/networks/default.xml

%files daemon-config-nwfilter
%dir %attr(0700, root, root) %{_sysconfdir}/%{name}/nwfilter/
%config %{_sysconfdir}/%{name}/nwfilter/*.xml

%files daemon-driver-interface
%config(noreplace) %{_sysconfdir}/%{name}/virtinterfaced.conf
%{_datadir}/augeas/lenses/virtinterfaced.aug
%{_datadir}/augeas/lenses/tests/test_virtinterfaced.aug
%{_unitdir}/virtinterfaced.service
%{_unitdir}/virtinterfaced.socket
%{_unitdir}/virtinterfaced-ro.socket
%{_unitdir}/virtinterfaced-admin.socket
%{_sbindir}/virtinterfaced
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_interface.so

%files daemon-driver-network
%config(noreplace) %{_sysconfdir}/%{name}/virtnetworkd.conf
%{_datadir}/augeas/lenses/virtnetworkd.aug
%{_datadir}/augeas/lenses/tests/test_virtnetworkd.aug
%{_unitdir}/virtnetworkd.service
%{_unitdir}/virtnetworkd.socket
%{_unitdir}/virtnetworkd-ro.socket
%{_unitdir}/virtnetworkd-admin.socket
%{_sbindir}/virtnetworkd
%dir %attr(0700, root, root) %{_sysconfdir}/%{name}/qemu/
%dir %attr(0700, root, root) %{_sysconfdir}/%{name}/qemu/networks/
%dir %attr(0700, root, root) %{_sysconfdir}/%{name}/qemu/networks/autostart
%dir %attr(0700, root, root) %{_localstatedir}/lib/%{name}/network/
%dir %attr(0755, root, root) %{_localstatedir}/lib/%{name}/dnsmasq/
%attr(0755, root, root) %{_libdir}/%{name}/libvirt_leaseshelper
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_network.so
%if %{with_firewalld_zone}
%dir %{_prefix}/lib/firewalld/zones/
%{_prefix}/lib/firewalld/zones/libvirt.xml
%endif

%files daemon-driver-nodedev
%config(noreplace) %{_sysconfdir}/%{name}/virtnodedevd.conf
%{_datadir}/augeas/lenses/virtnodedevd.aug
%{_datadir}/augeas/lenses/tests/test_virtnodedevd.aug
%{_unitdir}/virtnodedevd.service
%{_unitdir}/virtnodedevd.socket
%{_unitdir}/virtnodedevd-ro.socket
%{_unitdir}/virtnodedevd-admin.socket
%{_sbindir}/virtnodedevd
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_nodedev.so

%files daemon-driver-nwfilter
%config(noreplace) %{_sysconfdir}/%{name}/virtnwfilterd.conf
%{_datadir}/augeas/lenses/virtnwfilterd.aug
%{_datadir}/augeas/lenses/tests/test_virtnwfilterd.aug
%{_unitdir}/virtnwfilterd.service
%{_unitdir}/virtnwfilterd.socket
%{_unitdir}/virtnwfilterd-ro.socket
%{_unitdir}/virtnwfilterd-admin.socket
%{_sbindir}/virtnwfilterd
%dir %attr(0700, root, root) %{_sysconfdir}/%{name}/nwfilter/
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_nwfilter.so

%files daemon-driver-secret
%config(noreplace) %{_sysconfdir}/%{name}/virtsecretd.conf
%{_datadir}/augeas/lenses/virtsecretd.aug
%{_datadir}/augeas/lenses/tests/test_virtsecretd.aug
%{_unitdir}/virtsecretd.service
%{_unitdir}/virtsecretd.socket
%{_unitdir}/virtsecretd-ro.socket
%{_unitdir}/virtsecretd-admin.socket
%{_sbindir}/virtsecretd
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_secret.so

%files daemon-driver-storage

%files daemon-driver-storage-core
%config(noreplace) %{_sysconfdir}/%{name}/virtstoraged.conf
%{_datadir}/augeas/lenses/virtstoraged.aug
%{_datadir}/augeas/lenses/tests/test_virtstoraged.aug
%{_unitdir}/virtstoraged.service
%{_unitdir}/virtstoraged.socket
%{_unitdir}/virtstoraged-ro.socket
%{_unitdir}/virtstoraged-admin.socket
%{_sbindir}/virtstoraged
%attr(0755, root, root) %{_libdir}/%{name}/libvirt_parthelper
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_storage.so
%dir %{_libdir}/%{name}/storage-backend
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_fs.so
%dir %{_libdir}/%{name}/storage-file
%{_libdir}/%{name}/storage-file/libvirt_storage_file_fs.so

%files daemon-driver-storage-disk
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_disk.so

%files daemon-driver-storage-logical
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_logical.so

%files daemon-driver-storage-scsi
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_scsi.so

%files daemon-driver-storage-iscsi
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_iscsi.so

%files daemon-driver-storage-mpath
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_mpath.so

%if %{with_storage_gluster}
%files daemon-driver-storage-gluster
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_gluster.so
%{_libdir}/%{name}/storage-file/libvirt_storage_file_gluster.so
%endif

%if %{with_storage_rbd}
%files daemon-driver-storage-rbd
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_rbd.so
%endif

%if %{with_storage_sheepdog}
%files daemon-driver-storage-sheepdog
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_sheepdog.so
%endif

%if %{with_storage_iscsi_direct}
%files daemon-driver-storage-iscsi-direct
%{_libdir}/%{name}/storage-backend/libvirt_storage_backend_iscsi-direct.so
%endif

%if %{with_qemu}

%files daemon-driver-qemu
%config(noreplace) %{_sysconfdir}/%{name}/virtqemud.conf
%{_datadir}/augeas/lenses/virtqemud.aug
%{_datadir}/augeas/lenses/tests/test_virtqemud.aug
%{_unitdir}/virtqemud.service
%{_unitdir}/virtqemud.socket
%{_unitdir}/virtqemud-ro.socket
%{_unitdir}/virtqemud-admin.socket
%{_sbindir}/virtqemud
%config(noreplace) %{_sysconfdir}/%{name}/qemu.conf
%config(noreplace) %{_sysconfdir}/%{name}/qemu-lockd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.qemu
%dir %attr(0750, %{qemu_user}, %{qemu_group}) %{_localstatedir}/lib/%{name}/qemu/
%dir %attr(0750, %{qemu_user}, %{qemu_group}) %{_localstatedir}/cache/%{name}/qemu/
%dir %attr(0700, root, root) %{_localstatedir}/log/%{name}/qemu/
%{_datadir}/augeas/lenses/libvirtd_qemu.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd_qemu.aug
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_qemu.so
%dir %attr(0711, root, root) %{_localstatedir}/lib/%{name}/swtpm/
%dir %attr(0711, root, root) %{_localstatedir}/log/swtpm/
%dir %attr(0711, root, root) %{_localstatedir}/log/swtpm/%{name}/
%dir %attr(0711, root, root) %{_localstatedir}/log/swtpm/%{name}/qemu/
%endif

%if %{with_lxc}

%files daemon-driver-lxc
%config(noreplace) %{_sysconfdir}/%{name}/virtlxcd.conf
%{_datadir}/augeas/lenses/virtlxcd.aug
%{_datadir}/augeas/lenses/tests/test_virtlxcd.aug
%{_unitdir}/virtlxcd.service
%{_unitdir}/virtlxcd.socket
%{_unitdir}/virtlxcd-ro.socket
%{_unitdir}/virtlxcd-admin.socket
%{_sbindir}/virtlxcd
%config(noreplace) %{_sysconfdir}/%{name}/lxc.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.lxc
%dir %attr(0700, root, root) %{_localstatedir}/lib/%{name}/lxc/
%dir %attr(0700, root, root) %{_localstatedir}/log/%{name}/lxc/
%attr(0755, root, root) %{_libdir}/%{name}/libvirt_lxc
%{_datadir}/augeas/lenses/libvirtd_lxc.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd_lxc.aug
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_lxc.so
%attr(0755, root, root) %{_bindir}/virt-lxc-convert
    %if ! 0%{?is_opensuse}
%{_bindir}/virt-create-rootfs
%doc %{_mandir}/man1/virt-create-rootfs.1*
    %endif
%endif

%if %{with_libxl}

%files daemon-driver-libxl
%config(noreplace) %{_sysconfdir}/%{name}/virtxend.conf
%{_datadir}/augeas/lenses/virtxend.aug
%{_datadir}/augeas/lenses/tests/test_virtxend.aug
%{_unitdir}/virtxend.service
%{_unitdir}/virtxend.socket
%{_unitdir}/virtxend-ro.socket
%{_unitdir}/virtxend-admin.socket
%{_sbindir}/virtxend
%config(noreplace) %{_sysconfdir}/%{name}/libxl.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/libvirtd.libxl
%config(noreplace) %{_sysconfdir}/%{name}/libxl-lockd.conf
%{_datadir}/augeas/lenses/libvirtd_libxl.aug
%{_datadir}/augeas/lenses/tests/test_libvirtd_libxl.aug
%dir %attr(0700, root, root) %{_localstatedir}/lib/%{name}/libxl/
%dir %attr(0700, root, root) %{_localstatedir}/log/%{name}/libxl/
%dir %{_libdir}/%{name}/connection-driver
%{_libdir}/%{name}/connection-driver/libvirt_driver_libxl.so
%endif

%if %{with_vbox}

%files daemon-driver-vbox
%config(noreplace) %{_sysconfdir}/%{name}/virtvboxd.conf
%{_datadir}/augeas/lenses/virtvboxd.aug
%{_datadir}/augeas/lenses/tests/test_virtvboxd.aug
%{_unitdir}/virtvboxd.service
%{_unitdir}/virtvboxd.socket
%{_unitdir}/virtvboxd-ro.socket
%{_unitdir}/virtvboxd-admin.socket
%{_sbindir}/virtvboxd
%{_libdir}/%{name}/connection-driver/libvirt_driver_vbox.so
%endif

%if %{with_qemu}

%files daemon-qemu
%doc %{_docdir}/%{name}/libvirt-daemon-qemu.README
%endif

%if %{with_lxc}

%files daemon-lxc
%doc %{_docdir}/%{name}/libvirt-daemon-lxc.README
%endif

%if %{with_libxl}

%files daemon-xen
%doc %{_docdir}/%{name}/libvirt-daemon-xen.README
%endif

%if %{with_vbox}

%files daemon-vbox
%doc %{_docdir}/%{name}/libvirt-daemon-vbox.README
%endif

%files client
%doc %{_mandir}/man1/virsh.1*
%doc %{_mandir}/man1/virt-xml-validate.1*
%doc %{_mandir}/man1/virt-pki-validate.1*
%doc %{_mandir}/man1/virt-host-validate.1*
%{_bindir}/virsh
%{_bindir}/virt-xml-validate
%{_bindir}/virt-pki-validate
%{_bindir}/virt-host-validate
%if %{with_bash_completion}
%{_datadir}/bash-completion/completions/virsh
%endif
%dir %{_libdir}/%{name}
%attr(0755, root, root) %{_libdir}/%{name}/libvirt-guests.sh
%{_fillupdir}/sysconfig.libvirt-guests
%{_unitdir}/libvirt-guests.service
%{_sbindir}/rclibvirt-guests

%files libs -f %{_vpath_builddir}/%{name}.lang
%doc AUTHORS NEWS README README.md COPYING COPYING.LESSER 
%config(noreplace) %{_sysconfdir}/%{name}/libvirt.conf
%config(noreplace) %{_sysconfdir}/%{name}/libvirt-admin.conf
%{_libdir}/libvirt.so.*
%{_libdir}/libvirt-qemu.so.*
%{_libdir}/libvirt-lxc.so.*
%{_libdir}/libvirt-admin.so.*
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/schemas/
%dir %{_datadir}/%{name}/cpu_map/
%dir %attr(0755, root, root) %{_localstatedir}/lib/%{name}/

%{_datadir}/%{name}/schemas/basictypes.rng
%{_datadir}/%{name}/schemas/capability.rng
%{_datadir}/%{name}/schemas/domain.rng
%{_datadir}/%{name}/schemas/cputypes.rng
%{_datadir}/%{name}/schemas/domaincaps.rng
%{_datadir}/%{name}/schemas/domaincheckpoint.rng
%{_datadir}/%{name}/schemas/domaincommon.rng
%{_datadir}/%{name}/schemas/domainsnapshot.rng
%{_datadir}/%{name}/schemas/interface.rng
%{_datadir}/%{name}/schemas/network.rng
%{_datadir}/%{name}/schemas/networkcommon.rng
%{_datadir}/%{name}/schemas/networkport.rng
%{_datadir}/%{name}/schemas/nodedev.rng
%{_datadir}/%{name}/schemas/nwfilter.rng
%{_datadir}/%{name}/schemas/nwfilter_params.rng
%{_datadir}/%{name}/schemas/nwfilterbinding.rng
%{_datadir}/%{name}/schemas/secret.rng
%{_datadir}/%{name}/schemas/storagecommon.rng
%{_datadir}/%{name}/schemas/storagepool.rng
%{_datadir}/%{name}/schemas/storagepoolcaps.rng
%{_datadir}/%{name}/schemas/storagevol.rng
%{_datadir}/%{name}/cpu_map/*.xml
%{_datadir}/%{name}/test-screenshot.png

%files admin
%doc %{_mandir}/man1/virt-admin.1*
%{_bindir}/virt-admin
%if %{with_bash_completion}
%{_datadir}/bash-completion/completions/virt-admin
%endif

%if %{with_bash_completion}
%files bash-completion
%{_datadir}/bash-completion/completions/vsh
%endif

%files devel
%{_libdir}/libvirt.so
%{_libdir}/libvirt-admin.so
%{_libdir}/libvirt-qemu.so
%{_libdir}/libvirt-lxc.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/libvirt.pc
%{_libdir}/pkgconfig/libvirt-admin.pc
%{_libdir}/pkgconfig/libvirt-qemu.pc
%{_libdir}/pkgconfig/libvirt-lxc.pc
%dir %{_datadir}/%{name}/api/
%{_datadir}/%{name}/api/libvirt-api.xml
%{_datadir}/%{name}/api/libvirt-admin-api.xml
%{_datadir}/%{name}/api/libvirt-qemu-api.xml
%{_datadir}/%{name}/api/libvirt-lxc-api.xml

%files doc
# Website
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/*.png
%doc %{_docdir}/%{name}/*.html
%doc %{_docdir}/%{name}/*.gif
%doc %{_docdir}/%{name}/*.css
%doc %{_docdir}/%{name}/html
%doc %{_docdir}/%{name}/internals
%doc %{_docdir}/%{name}/kbase
%doc %{_docdir}/%{name}/logos
%doc %{_docdir}/%{name}/fonts
%doc %{_docdir}/%{name}/js
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/doc/%{name}/examples
%doc %{_datadir}/doc/%{name}/examples/*

%if %{with_sanlock}

%files lock-sanlock
%doc %{_mandir}/man8/virt-sanlock-cleanup.8*
    %if %{with_qemu}
%config(noreplace) %{_sysconfdir}/%{name}/qemu-sanlock.conf
    %endif
    %if %{with_libxl}
%config(noreplace) %{_sysconfdir}/%{name}/libxl-sanlock.conf
    %endif
%dir %{_libdir}/%{name}/lock-driver/
%attr(0755, root, root) %{_libdir}/%{name}/lock-driver/sanlock.so
%dir %{_datadir}/augeas/
%dir %{_datadir}/augeas/lenses
%dir %{_datadir}/augeas/lenses/tests
%{_datadir}/augeas/lenses/libvirt_sanlock.aug
%{_datadir}/augeas/lenses/tests/test_libvirt_sanlock.aug
%dir %attr(0700, root, sanlock) %{_localstatedir}/lib/%{name}/sanlock
%{_sbindir}/virt-sanlock-cleanup
%attr(0755, root, root) %{_libdir}/%{name}/libvirt_sanlock_helper
%endif

%if %{with_wireshark}

%files -n wireshark-plugin-libvirt
%dir %{wireshark_plugindir}/
%{wireshark_plugindir}/libvirt.so
%endif

%files nss
%{_libdir}/libnss_libvirt.so.2
%{_libdir}/libnss_libvirt_guest.so.2

%changelog
