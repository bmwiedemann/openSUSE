#
# spec file for package openvswitch
#
# Copyright (c) 2024 SUSE LLC
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
# needssslcertforbuild


%define skip_python2 1
%define ovs_lname libopenvswitch-3_1-0
%define ovn_lname libovn-23_03-0
%define ovs_version 3.1.0
%define ovn_version 23.03.0
%define ovs_dir ovs-%{ovs_version}
%define ovn_dir ovn-%{ovn_version}
%define rpmstate %{_rundir}/openvswitch-rpm-state-
%define _dpdkv 22.11.1
%define name_tag ${nil}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%ifarch aarch64 x86_64 ppc64le
%if 0%{?suse_version}
# DPDK enabled only SUSE/openSUSE
%bcond_without dpdk
%else
# DPDK disabled elsewhere even if supported by the architecture.
%bcond_with dpdk
%endif
%else
# No DPDK support on these architectures
%bcond_with dpdk
%endif
# The testsuite is somewhat fragile for continuous testing in OBS
# but keep it here as an option
%bcond_with check
# Disable building the external kernel datapath by default
%bcond_with kmp
# Disable building with AF_XDP support, specify '--without afxdp' when building
%bcond_with afxdp
Name:           openvswitch
Version:        %{ovs_version}
Release:        0
Summary:        A multilayer virtual network switch
# All code is Apache-2.0 except
# - lib/sflow* which is SISSL
# - utilities/bugtool which is LGPL-2.1
License:        Apache-2.0 AND LGPL-2.1-only AND SISSL
Group:          Productivity/Networking/System
URL:            http://openvswitch.org/
Source0:        http://openvswitch.org/releases/openvswitch-%{version}.tar.gz
Source1:        https://github.com/ovn-org/ovn/archive/v%{ovn_version}.tar.gz#/ovn-%{ovn_version}.tar.gz
Source2:        preamble
Source10:       openvswitch-user.conf
Source89:       Module.supported.updates
Source99:       openvswitch-rpmlintrc
# OVS patches
# PATCH-FIX-OPENSUSE: Use-strongswan-for-openvswitch-ipsec-service.patch
Patch0:         0001-Use-strongswan-for-openvswitch-ipsec-service.patch
# PATCH-FIX-OPENSUSE: 0001-Run-openvswitch-as-openvswitch-openvswitch.patch
Patch1:         0001-Run-openvswitch-as-openvswitch-openvswitch.patch
# PATCH-FIX-OPENSUSE: 0001-Don-t-change-permissions-of-dev-hugepages.patch
Patch2:         0001-Don-t-change-permissions-of-dev-hugepages.patch
# PATCH-FIX-OPENSUSE: 0001-Use-double-hash-for-OVS_USER_ID-comment.patch
Patch3:         0001-Use-double-hash-for-OVS_USER_ID-comment.patch
# PATCH-FEATURE-UPSTREAM install-ovsdb-tools.patch -- Install some tools required for building OVN
Patch4:         install-ovsdb-tools.patch
# PATCH-FIX-UPSTREAM CVE-2023-1668.patch
Patch5:         CVE-2023-1668.patch
# PATCH-FIX-UPSTREAM CVE-2023-5366.patch
Patch6:         CVE-2023-5366.patch
# Fix CVE-2023-3966 [bsc#1219465] -- Invalid memory access in Geneve with HW offload
Patch7:         openvswitch-CVE-2023-3966.patch
# boo#1225906: Restore build with gcc14
Patch8:         openvswitch-2.17.8-gcc14-build-fix.patch
#OVN patches
# PATCH-FIX-OPENSUSE: 0001-Run-ovn-as-openvswitch-openvswitch.patch
Patch20:        0001-Run-ovn-as-openvswitch-openvswitch.patch
# PATCH-FIX-UPSTREAM CVE-2023-3152 [bsc#1212125] -- service monitor MAC flow is not rate limited
Patch21:        CVE-2023-3152.patch
# CVE-2021-36980 [bsc#1188524], use-after-free in decode_NXAST_RAW_ENCAP
BuildRequires:  autoconf
BuildRequires:  %{python_module setuptools}
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  unbound-devel
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(openssl)
Requires:       modutils
# ovs-ctl / ovs-pki use /usr/bin/uuidgen:
Requires:       util-linux
Provides:       openvswitch-common = %{version}
Obsoletes:      openvswitch-common < 2.7.0
Provides:       openvswitch-controller = %{version}
Obsoletes:      openvswitch-controller < 2.7.0
# openvswitch-switch has been merged to the main package
# so we need to provide a migration path
Provides:       %{name}-dpdk = %{version}
Provides:       %{name}-dpdk-switch = %{version}
Provides:       %{name}-switch = %{version}
Obsoletes:      %{name}-dpdk < 2.7.0
Obsoletes:      %{name}-dpdk-switch < 2.7.0
Obsoletes:      %{name}-switch < 2.7.0
%if 0%{?suse_version}
BuildRequires:  libopenssl-devel
BuildRequires:  python-rpm-macros
BuildRequires:  sysuser-tools
Requires(post): %fillup_prereq
Requires(pre):  shadow
Suggests:       logrotate
%{?systemd_ordering}
%sysusers_requires
%else
BuildRequires:  environment-modules
BuildRequires:  openssl-devel
BuildRequires:  python3-rpm-macros
BuildRequires:  systemd-units
Requires(post): systemd-units
Requires(postun): systemd-units
Requires(pre):  shadow-utils
Requires(preun): systemd-units
%endif
# Needed by the testsuite
%if %{with check}
BuildRequires:  procps
%endif
%if %{with kmp}
Suggests:       openvswitch-kmp
%endif
%if %{with dpdk}
# We need to be a bit strict with the dpdk version since
# it's very possible for DPDK to change it's API between
# releases.
BuildRequires:  dpdk-devel >= %{_dpdkv}
BuildRequires:  libmnl-devel
BuildRequires:  libnuma-devel
BuildRequires:  libpcap-devel
BuildRequires:  rdma-core-devel
%endif

%description
Open vSwitch is a multilayer virtual network Ethernet switch. It is
enables network automation through programmatic extension, and
supports standard management interfaces and protocols (e.g. NetFlow,
sFlow, RSPAN, ERSPAN, CLI, LACP, 802.1ag). In addition, it supports
distribution across multiple physical servers similar to VMware’s
vNetwork distributed vswitch or Cisco’s Nexus 1000V.

%if %{with kmp}
%package kmp
Summary:        Open vSwitch kernel modules
License:        GPL-2.0-or-later
Group:          System/Kernel
BuildRequires:  %{kernel_module_package_buildreqs}
%suse_kernel_module_package -p %{_sourcedir}/preamble ec2 xenpae vmi um

%description kmp
Kernel modules supporting the openvswitch datapath.
%endif

%package -n %{ovs_lname}
Summary:        Open vSwitch core libraries
License:        Apache-2.0
Group:          System/Libraries
%if %{with dpdk}
Requires:       dpdk >= %{_dpdkv}
Requires:       libdpdk-23 >= %{_dpdkv}
%endif

%description -n %{ovs_lname}
Contains the shared libraries used by Open vSwitch and any eventual extensions.

%package doc
Summary:        Open vSwitch Documentation
License:        Apache-2.0
Group:          System/Libraries
BuildArch:      noarch

%description doc
Contains additional documentation for the Open vSwitch.

%package devel
Summary:        Development files for Open vSwitch
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Requires:       %{ovs_lname} = %{version}
# Required for ovsdb-ildc
Requires:       python3-ovs = %{version}
Provides:       %{name}-dpdk-devel = %{version}
Obsoletes:      %{name}-dpdk-devel < 2.7.0

%description devel
Devel libraries and headers for Open vSwitch.

%package pki
Summary:        Open vSwitch public key infrastructure dependency package
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       openssl(cli)
Provides:       %{name}-dpdk-pki = %{version}
Obsoletes:      %{name}-dpdk-pki < 2.7.0

%description pki
openvswitch-pki provides PKI (public key infrastructure) support for
Open vSwitch switches and controllers, reducing the risk of
man-in-the-middle attacks on the Open vSwitch network infrastructure.

Open vSwitch is a full-featured software-based Ethernet switch.

%package vtep
Summary:        Open vSwitch VTEP emulator
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       %{name}-switch = %{version}
# Since openvswitch/scripts/ovs-vtep requires various ovs python modules.
Requires:       python3-ovs = %{version}
Provides:       %{name}-dpdk-vtep = %{version}
Obsoletes:      %{name}-dpdk-vtep < 2.7.0

%description vtep
A VTEP (VXLAN Tunnel EndPoint) emulator that uses Open vSwitch for
forwarding.

Open vSwitch is a full-featured software-based Ethernet switch.

%package ipsec
Summary:        Open vSwitch IPsec tunneling support
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       python3-ovs = %{version}
Requires:       strongswan

%description ipsec
This package provides IPsec tunneling support for OVS tunnels.

%package -n python3-ovs
Summary:        Python3 bindings for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{ovs_lname} = %{version}
Requires:       python3
Requires:       python3-sortedcontainers
Provides:       python3-%{name} = %{version}
Obsoletes:      python3-%{name} < 2.10.1

%description -n python3-ovs
This package contains the Python3 bindings for Open vSwitch database.

%package test
Summary:        Open vSwitch test package
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       python3
Requires:       python3-Twisted
Requires:       python3-ovs = %{version}
Provides:       python3-%{name}-test = %{version}
Obsoletes:      python3-%{name}-test < 2.13.0

%description test
Open vSwitch is a software-based Ethernet switch.

This package contains utilities that are useful to diagnose
performance and connectivity issues in Open vSwitch setup.

%package -n ovn
Version:        %{ovn_version}
Release:        0
Summary:        Open Virtual Network diagnostic utilities
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            http://ovn.org/
Requires:       %{name} = %{ovs_version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn = %{ovn_version}
Provides:       %{name}-ovn = %{ovn_version}
Provides:       %{name}-ovn-common = %{ovn_version}
Obsoletes:      %{name}-dpdk-ovn < 2.7.0
Obsoletes:      %{name}-ovn < 2.7.0
Obsoletes:      %{name}-ovn-common < 2.13.0
%if 0%{?suse_version}
Suggests:       logrotate
%endif

%description -n ovn
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package -n ovn-central
Version:        %{ovn_version}
Release:        0
Summary:        Open Virtual Network support for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            http://ovn.org/
Requires:       %{name} = %{ovs_version}
Requires:       ovn = %{ovn_version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-northd
Provides:       %{name}-ovn-central = %{ovn_version}
Provides:       %{name}-ovn:%{_bindir}/ovn-northd
Obsoletes:      %{name}-ovn-central < 2.13.0

%description -n ovn-central
This subpackage contains the OVN database and northbound daemon.

%package -n ovn-host
Version:        %{ovn_version}
Release:        0
Summary:        Open Virtual Network support for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            http://ovn.org/
Requires:       %{name} = %{ovs_version}
Requires:       ovn = %{ovn_version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-controller
Provides:       %{name}-ovn-host = %{ovn_version}
Provides:       %{name}-ovn:%{_bindir}/ovn-controller
Obsoletes:      %{name}-ovn-host < 2.13.0

%description -n ovn-host
This subpackage contains the OVN host controller.

%package -n ovn-vtep
Version:        %{ovn_version}
Release:        0
Summary:        Open Virtual Network VTEP controller for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            http://ovn.org/
Requires:       %{name} = %{ovs_version}
Requires:       ovn = %{ovn_version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-controller-vtep
Provides:       %{name}-ovn-vtep = %{ovn_version}
Provides:       %{name}-ovn:%{_bindir}/ovn-controller-vtep
Obsoletes:      %{name}-ovn-vtep < 2.13.0

%description -n ovn-vtep
This subpackage contains the OVN VTEP (VXLAN Tunnel Endpoint) controller.

%package -n ovn-docker
Version:        %{ovn_version}
Release:        0
Summary:        Docker network plugins for OVN
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            http://ovn.org/
Requires:       %{name} = %{ovs_version}
Requires:       ovn = %{ovn_version}
Requires:       python3-openvswitch = %{ovs_version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-docker-overlay-driver
Provides:       %{name}-ovn-docker = %{ovn_version}
Provides:       %{name}-ovn:%{_bindir}/ovn-docker-overlay-driver
Obsoletes:      %{name}-ovn-docker < 2.13.0

%description -n ovn-docker
This subpackage contains the OVN Docker network plugins.

%package -n ovn-doc
Version:        %{ovn_version}
Release:        0
Summary:        Open Virtual Network Documentation
License:        Apache-2.0
Group:          System/Libraries
BuildArch:      noarch

%description -n ovn-doc
Contains additional documentation for OVN.

%package -n %{ovn_lname}
Version:        %{ovn_version}
Release:        0
Summary:        Open Virtual Network core libraries
License:        Apache-2.0
Group:          System/Libraries

%description -n %{ovn_lname}
This subpackage contains the OVN shared libraries.

%package -n ovn-devel
Version:        %{ovn_version}
Release:        0
Summary:        Development files for Open Virtual Network
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Requires:       %{ovn_lname} = %{ovn_version}
# ovn-devel was split form openvswitch-devel
Provides:       %{name}-devel:%{_includedir}/ovn

%description -n ovn-devel
Devel libraries and headers for Open Virtual Network.

%prep
%setup -q -n %{name}-%{ovs_version} -a 1
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
# remove python/ovs/dirs.py - this is generated from template to have proper paths
rm python/ovs/dirs.py
cd %{ovn_dir}
%patch -P 20 -p1
%patch -P 21 -p1

%build
mkdir %ovs_dir
# We build both OVS and OVN. OVN is already on its own subdir ovn_dir.
# Move OVS sources to ovs_dir
find $PWD -maxdepth 1 ! -path $PWD ! -name %ovs_dir -a ! -name %ovn_dir -exec mv -t %ovs_dir {} +

# Init OVS config.
pushd %ovs_dir
# only call boot.sh for distros with autoconf >= 2.64
bash -x boot.sh
popd

# Build kernel modules if needed.
%if %{with kmp}
    mkdir kmp
    export EXTRA_CFLAGS='-DVERSION=\"%{ovs_version}\"'
    for flavor in %{flavors_to_build}; do
        rm -rf kmp/$flavor
        cp -r %ovs_dir kmp/$flavor
        cp -a %{SOURCE89} kmp/$flavor/datapath/linux/Module.supported
        pushd kmp/$flavor
        %configure \
            --with-logdir=%{_localstatedir}/log/openvswitch \
            --with-rundir=%{_rundir}/openvswitch \
            --with-linux=%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor \
            --with-linux-source=%{_prefix}/src/linux
        cd datapath/linux
        make %{?_smp_mflags}
        popd
    done
%endif

# Build OVS.
pushd %ovs_dir

# This currently has no effect as the @dpdk section has been patched out of the
# service file. Run it anyway, in case a new section that we need appears over
# time.
python3 build-aux/dpdkstrip.py \
%if %{with dpdk}
    --dpdk \
%else
    --nodpdk \
%endif
    < rhel/usr_lib_systemd_system_ovs-vswitchd.service.in \
    > rhel/usr_lib_systemd_system_ovs-vswitchd.service

%configure \
        --disable-static \
        --enable-shared \
        --enable-libcapng \
        --enable-ssl \
%if %{with dpdk}
        --with-dpdk=shared \
%endif
%if %{with afxdp}
        --enable-afxdp \
%else
        --disable-afxdp \
%endif
        --with-dbdir=%{_sharedstatedir}/openvswitch \
        --with-rundir=%{_rundir}/openvswitch \
        --with-logdir=%{_localstatedir}/log/openvswitch \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
        PYTHON3=%{_bindir}/python3
%make_build
popd

# Build OVN.
pushd %ovn_dir

bash -x boot.sh
%configure \
        --with-ovs-source=../%{ovs_dir} \
        --disable-static \
        --enable-shared \
        --enable-libcapng \
        --enable-ssl \
        --with-dbdir=%{_sharedstatedir}/ovn \
        --with-rundir=%{_rundir}/ovn \
        --with-logdir=%{_localstatedir}/log/ovn \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
        PYTHON3=%{_bindir}/python3 \
        LDFLAGS=-L../%{ovs_dir}/lib/.libs
%make_build
popd
%sysusers_generate_pre %{SOURCE10} openvswitch openvswitch.conf

%check
%if %{with check}
touch resolv.conf
export OVS_RESOLV_CONF=$(pwd)/resolv.conf
mv python/build python/pb
ln -s _build.tmp python/build

pushd %ovs_dir
# Recheck tests before we declare them broken. If that fails, dump
# the log and exit. >2.5.0 uses the RECHECK env variable so this
# needs to be taken into consideration for future releases.
if ! make check TESTSUITEFLAGS="%{?_smp_mflags}" &&
   ! make check RECHECK=yes; then
    cat tests/testsuite.log
    exit 1
fi
popd

pushd $ovn_dir
if ! make check TESTSUITEFLAGS="%{?_smp_mflags}" &&
   ! make check RECHECK=yes; then
    cat tests/testsuite.log
    exit 1
fi
popd
%endif

%install

# Intall kernel modules.
%if %{with kmp}
export NO_BRP_STALE_LINK_ERROR=yes
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
export BRP_PESIGN_FILES="*.ko /lib/firmware"
for flavor in %{flavors_to_build}; do
    pushd kmp/$flavor/datapath/linux
    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules_install M=$PWD
    popd
done
%endif

# Install OVS dist files on temp buildroot.
mkdir -p buildroot/ovs
pushd %ovs_dir
%make_install DESTDIR=$(pwd)/../buildroot/ovs
popd

# Clean up OVS files
rm -f buildroot/ovs%{_libdir}/*.a
rm -f buildroot/ovs%{_libdir}/*.la

# Install OVN dist files on temp build root.
mkdir -p buildroot/ovn
pushd %ovn_dir
%make_install DESTDIR=$(pwd)/../buildroot/ovn
popd

# Clean up OVN files
rm -f buildroot/ovn%{_datadir}/ovn/scripts/ovs*
rm -rf buildroot/ovn%{_datadir}/ovn/bugtool-plugins
rm -f buildroot/ovn%{_libdir}/*.a
rm -f buildroot/ovn%{_libdir}/*.la

# Remove known OVS dupes from OVN.
rm -f buildroot/ovn%{_mandir}/man5/ovs*
rm -f buildroot/ovn%{_mandir}/man7/ovs*

# Verify no duplicates and move dist files to real buildroot
dupes=$(find buildroot -mindepth 2 -type f -printf '%p\n' | cut -d'/' -f3- | sort | uniq -c | grep -Ev "^ *1 " || true)
[ -n "$dupes" ] && exit 1
cp -an buildroot/ovn/* %{buildroot}/
cp -an buildroot/ovs/* %{buildroot}/

# Install OVS additional files
pushd %ovs_dir

# Install extra headers not included with 'make install'
copy_headers() {
    src=$1
    dst=%{buildroot}/$2
    install -d -m 0755 $dst
    install -m 0644 $src/*.h $dst
}
copy_headers include/sparse %{_includedir}/openvswitch/sparse
copy_headers include/sparse/arpa %{_includedir}/openvswitch/sparse/arpa
copy_headers include/sparse/netinet %{_includedir}/openvswitch/sparse/netinet
copy_headers include/sparse/sys %{_includedir}/openvswitch/sparse/sys
copy_headers lib %{_includedir}/openvswitch/lib

for service in openvswitch \
               ovsdb-server \
               ovs-vswitchd \
               ovs-delete-transient-ports \
               openvswitch-ipsec; do
        install -D -m 644 rhel/usr_lib_systemd_system_${service}.service \
        %{buildroot}%{_unitdir}/${service}.service
        ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc${service}
done

# This changes group ownership of any vfio device to 'hugetlbfs' through udev.
# That's probably not the most appropriate name for such a group and also
# should probably be coordinated system wide.
#%%if %%{with dpdk}
#    install -p -D -m 0644 rhel/usr_lib_udev_rules.d_91-vfio.rules \
#    %%{buildroot}%%{_prefix}/lib/udev/rules.d/91-vfio.rules
#%%endif

%if 0%{?suse_version}
install -D -m 644 rhel/usr_share_openvswitch_scripts_systemd_sysconfig.template \
        %{buildroot}%{_fillupdir}/sysconfig.openvswitch

# Fix installation path
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions/
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/ovs-* %{buildroot}/%{_datadir}/bash-completion/completions/
chmod 0644 %{buildroot}/%{_datadir}/bash-completion/completions/*

# fixing W: # interpreter
find %{buildroot}/%{_datadir}/openvswitch/scripts/ -name "*.py" -exec sed -i 's|env python|python|' \{\} +

%else
install -D -m 644 rhel/usr_share_openvswitch_scripts_systemd_sysconfig.template \
        %{buildroot}%{_sysconfdir}/sysconfig/openvswitch
install -d -m 0755 %{buildroot}/%{_sysconfdir}/sysconfig/network-scripts/
install -p -m 0755 rhel/etc_sysconfig_network-scripts_ifdown-ovs \
        %{buildroot}%{_sysconfdir}/sysconfig/network-scripts/ifdown-ovs
install -p -m 0755 rhel/etc_sysconfig_network-scripts_ifup-ovs \
        %{buildroot}%{_sysconfdir}/sysconfig/network-scripts/ifup-ovs
%endif

install -d -m 0755 %{buildroot}/%{_rundir}/openvswitch
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 0755 %{buildroot}%{_localstatedir}/log/openvswitch

install -p -D -m 0644 rhel/etc_openvswitch_default.conf \
         %{buildroot}/%{_sysconfdir}/openvswitch/default.conf
install -m 644 rhel/etc_logrotate.d_openvswitch \
         %{buildroot}%{_sysconfdir}/logrotate.d/openvswitch

install -m 644 vswitchd/vswitch.ovsschema \
         %{buildroot}%{_datadir}/openvswitch/vswitch.ovsschema

# Copy documentation.
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r Documentation/* %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_docdir}/%{name}/_build
rm %{buildroot}%{_docdir}/%{name}/automake.mk
rm %{buildroot}%{_docdir}/%{name}/conf.py
popd

# Tests
mkdir -p %{buildroot}%{python3_sitelib}
cp -a %{buildroot}%{_datadir}/openvswitch/python/ovstest \
    %{buildroot}%{python3_sitelib}

# Python subpackage
# Build on a temporary directory.
mkdir python3-ovs && pushd $_
# Some build files are in sources while others are generated directly on
# buildroot as part of make_install (dirs.py). Copy them first.
cp -an ../%{ovs_dir}/python/* $(pwd)/
rm -rf %{buildroot}%{_datadir}/openvswitch/python
export LDFLAGS="${LDFLAGS} -L %{buildroot}%{_libdir}"
export CPPFLAGS="-I ../../include"

%if 0%{?suse_version}
# SLES
%{python3_build}
%{python3_install}
%else
# RHEL
%py3_build
%py3_install
%endif

# Done with OVS additional files.
popd

%python_expand %fdupes %{buildroot}%{$python_sitearch}
# Install OVN aditional files.
pushd %ovn_dir

for service in ovn-controller \
               ovn-controller-vtep \
               ovn-northd; do
        install -D -m 644 rhel/usr_lib_systemd_system_${service}.service \
        %{buildroot}%{_unitdir}/${service}.service
        ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc${service}
done

%if 0%{?suse_version}
install -D -m 644 rhel/usr_share_ovn_scripts_systemd_sysconfig.template \
        %{buildroot}%{_fillupdir}/sysconfig.ovn
%else
install -D -m 644 rhel/usr_share_ovn_scripts_systemd_sysconfig.template \
        %{buildroot}%{_sysconfdir}/sysconfig/ovn
%endif

# firewalld
install -d %{buildroot}%{_prefix}/lib/firewalld/services/
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-central-firewall-service.xml \
        %{buildroot}%{_prefix}/lib/firewalld/services/ovn-central-firewall-service.xml
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-host-firewall-service.xml \
        %{buildroot}%{_prefix}/lib/firewalld/services/ovn-host-firewall-service.xml

install -p -D -m 0644 rhel/etc_logrotate.d_ovn \
        %{buildroot}%{_sysconfdir}/logrotate.d/ovn
install -d -m 0755 %{buildroot}%{_localstatedir}/log/ovn

# Copy documentation.
mkdir -p %{buildroot}%{_docdir}/ovn
cp -r Documentation/* %{buildroot}%{_docdir}/ovn
rm -rf %{buildroot}%{_docdir}/ovn/_build
rm %{buildroot}%{_docdir}/ovn/automake.mk
rm %{buildroot}%{_docdir}/ovn/conf.py

# Done with OVN additional files.
popd

install -D -m 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}/openvswitch.conf

%pre -f openvswitch.pre
%if 0%{?suse_version}
    %service_add_pre ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service
%endif
if [ "$1" -ge 1 ]; then
    # Save the "enabled" state across the transition of
    # ownership of openvswitch.service from openvswitch-switch to
    # openvswitch.
    if [ x$(systemctl is-enabled openvswitch.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}openvswitch || :
    fi
fi

%pre ipsec
%if 0%{?suse_version}
    %service_add_pre openvswitch-ipsec.service
%endif

%preun
%if 0%{?suse_version}
    %service_del_preun ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service
%else
    %if 0%{?systemd_preun:1}
        %systemd_preun %{name}.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 0 ]; then
            /bin/systemctl --no-reload disable %{name}.service >/dev/null 2>&1 || :
            /bin/systemctl stop %{name}.service >/dev/null 2>&1 || :
        fi
    %endif
%endif

%preun ipsec
%if 0%{?suse_version}
	%service_del_preun openvswitch-ipsec.service
%endif

%preun test
%if 0%{?suse_version}
    %service_del_preun openvswitch-testcontroller
%else
    %if 0%{?systemd_post:1}
        %systemd_preun openvswitch-testcontroller.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 0 ]; then
            /bin/systemctl --no-reload disable openvswitch-testcontroller.service >/dev/null 2>&1 || :
            /bin/systemctl stop openvswitch-testcontroller.service >/dev/null 2>&1 || :
        fi
    %endif
%endif

%post
if [ $1 -eq 1 ]; then
    # Follow the upstream strategy that no running openvswitch
    # configuration is changed on upgrade so use fillup only for new installs.
    %{?suse_version: %fillup_only -n openvswitch}
fi

%if 0%{?suse_version}
	%service_add_post ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service
%else
    %if 0%{?systemd_post:1}
        %systemd_post openvswitch.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 1 ]; then
            /bin/systemctl daemon-reload >dev/null || :
        fi
    %endif
%endif

%post ipsec
%if 0%{?suse_version}
	%service_add_post openvswitch-ipsec.service
%endif

%post -n %{ovs_lname} -p /sbin/ldconfig

%postun
# Do not restart the openvswitch service on package updates.
# Restarting the service may break the existing network state.
# For example, openflow rules are not automatically re-installed
# after an OvS update if no SDN controller is used. Moreover, restaring
# the OvS can break remote administration during the update so let the
# admin decide when it's the best time for an OvS restart.
# 5771f476573445710834234a6a9f7bd999a027e7 ("fedora: do not restart the service on a pkg upgrade")
%if 0%{?suse_version}
    %service_del_postun_without_restart ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun openvswitch.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%postun ipsec
%if 0%{?suse_version}
	%service_del_postun_without_restart openvswitch-ipsec.service
%endif

%postun test
%if 0%{?suse_version}
    %service_del_postun_without_restart openvswitch-testcontroller
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun openvswitch-testcontroller.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%postun -n %{ovs_lname} -p /sbin/ldconfig

%posttrans
# Save the "enabled" state across the transition of ownership
# of openvswitch.service from openvswitch-switch to
# openvswitch.
if [ -e %{rpmstate}openvswitch ]; then
    rm -f %{rpmstate}openvswitch
    systemctl enable openvswitch.service
fi

ovsdbdir_regex="^[[:space:]]*OVS_DBDIR[[:space:]]*="
ovsuserid_regex="^[[:space:]]*OVS_USER_ID[[:space:]]*="
ovsvar_valueregex="[^=]*=[[:space:]]*["'"'"']{0,1}([^"'"'"']*)["'"'"']{0,1}[[:space:]]*$"
conf="%{_sysconfdir}/sysconfig/openvswitch"
ovsdbdir=$(grep -E "${ovsdbdir_regex}" "${conf}" | tail -1 | sed -E --posix 's|'"${ovsvar_valueregex}"'|\1|')
ovsuserid=$(grep -E "${ovsuserid_regex}" "${conf}" | tail -1 | sed -E --posix 's|'"${ovsvar_valueregex}"'|\1|')

# Default DB path changed from /etc/openvswitch to /var/lib/openvswitch.
# But try to keep the old path for upgraded users already making use of it.
if [ -z "$ovsdbdir" ]; then
    ovsdbpid=$(systemctl is-active --quiet ovsdb-server && systemctl show -p MainPID --value ovsdb-server || echo 0)
    if [ $ovsdbpid -gt 0 ] && [ -n "$(find /proc/$ovsdbpid/fd/ -type l -lname '%{_sysconfdir}/openvswitch/conf.db')" ]; then
        # We have ovsdb-server pid from the unit file with DB open at the old path.
        ovsdbdir="%{_sysconfdir}/openvswitch"
        sed -i -e '1{r /dev/stdin' -e 'N}' "%{_sysconfdir}/sysconfig/openvswitch" << EOF

# OVS_DBDIR was automatically inserted here on openvswitch package upgrade to
# preserve the currently used /etc/openvswitch as the database directory.
# Note that new installs use /var/lib/openvswitch as the default database
# directory by omission.
OVS_DBDIR="%{_sysconfdir}/openvswitch"

EOF
    fi
fi

# Default OVS user changed from root:root to openvswitch:openvswitch.
# But try to keep root:root for upgraded users already making use of it.
# Use .conf.db.~lock~ instead of conf.db as conf.db might have been moved
# to a backup on a previous run attempt.
if [ -z "$ovsuserid" -a -n "$ovsdbdir" -a -f "$ovsdbdir/.conf.db.~lock~" ]; then
    ovsuserid=$(stat -c "%{U}:%G" "$ovsdbdir/.conf.db.~lock~")
    if [ "$ovsuserid" = "root:root" ]; then
        sed -i -e '1{r /dev/stdin' -e 'N}' "%{_sysconfdir}/sysconfig/openvswitch" << EOF

# OVS_USER_ID was automatically inserted here on openvswitch package upgrade to
# preserve the currently used root:root as the openvswitch running credentials.
# Note that new installs use openvswitch:openvswitch as the default openvswitch
# running credentials by omission.
OVS_USER_ID="root:root"

EOF
    fi
fi

%pre -n ovn-central
%if 0%{?suse_version}
%service_add_pre ovn-northd.service
%endif
# Save the "enabled" state across the transition of
# ownership of ovn-northd.service from openvswitch-ovn-central to
# ovn-central.
if [ "$1" -ge 1 ]; then
    if [ x$(systemctl is-enabled ovn-northd.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}ovn-northd
    fi
fi

%pre -n ovn-host
%if 0%{?suse_version}
%service_add_pre ovn-controller.service
%endif
# Save the "enabled" state across the transition of
# ownership of ovn-controller.service from openvswitch-ovn-host to
# ovn-host.
if [ "$1" -ge 1 ]; then
    if [ x$(systemctl is-enabled ovn-controller.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}ovn-controller
    fi
fi

%pre -n ovn-vtep
%if 0%{?suse_version}
%service_add_pre ovn-controller-vtep.service
%endif
# Save the "enabled" state across the transition of
# ownership of ovn-controller-vtep.service from openvswitch-ovn-vtep to
# ovn-vtep.
if [ "$1" -ge 1 ]; then
    if [ x$(systemctl is-enabled ovn-controller-vtep.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}ovn-controller-vtep
    fi
fi

%preun -n ovn-central
%if 0%{?suse_version}
    %service_del_preun ovn-northd.service
%else
    %if 0%{?systemd_preun:1}
        %systemd_preun ovn-northd.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 0 ]; then
            /bin/systemctl --no-reload disable ovn-northd.service >/dev/null 2>&1 || :
            /bin/systemctl stop ovn-northd.service >/dev/null 2>&1 || :
        fi
    %endif
%endif

%preun -n ovn-host
%if 0%{?suse_version}
    %service_del_preun ovn-controller.service
%else
    %if 0%{?systemd_preun:1}
        %systemd_preun ovn-controller.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 0 ]; then
            /bin/systemctl --no-reload disable ovn-controller.service >/dev/null 2>&1 || :
            /bin/systemctl stop ovn-controller.service >/dev/null 2>&1 || :
        fi
    %endif
%endif

%preun -n ovn-vtep
%if 0%{?suse_version}
    %service_del_preun ovn-controller-vtep.service
%else
    %if 0%{?systemd_preun:1}
        %systemd_preun ovn-controller-vtep.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 0 ]; then
            /bin/systemctl --no-reload disable ovn-controller-vtep.service >/dev/null 2>&1 || :
            /bin/systemctl stop ovn-controller-vtep.service >/dev/null 2>&1 || :
        fi
    %endif
%endif

%post -n ovn
if [ $1 -eq 1 ]; then
    # Follow the upstream strategy that no running openvswitch
    # configuration is changed on upgrade so use fillup only for new installs.
    %{?suse_version: %fillup_only -n ovn}
fi

%post -n ovn-central
%if 0%{?suse_version}
    %service_add_post ovn-northd.service
%else
    %if 0%{?systemd_post:1}
        %systemd_post ovn-northd.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 1 ]; then
            /bin/systemctl daemon-reload >dev/null || :
        fi
    %endif
%endif

%post -n ovn-host
%if 0%{?suse_version}
    %service_add_post ovn-controller.service
%else
    %if 0%{?systemd_post:1}
        %systemd_post ovn-controller.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 1 ]; then
            /bin/systemctl daemon-reload >dev/null || :
        fi
    %endif
%endif

%post -n ovn-vtep
%if 0%{?suse_version}
    %service_add_post ovn-controller-vtep.service
%else
    %if 0%{?systemd_post:1}
        %systemd_post ovn-controller-vtep.service
    %else
        # Package install, not upgrade
        if [ $1 -eq 1 ]; then
            /bin/systemctl daemon-reload >dev/null || :
        fi
    %endif
%endif

%post -n %{ovn_lname} -p /sbin/ldconfig

%postun -n ovn-central
%if 0%{?suse_version}
    %service_del_postun_without_restart ovn-northd.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun ovn-northd.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%postun -n ovn-host
%if 0%{?suse_version}
    %service_del_postun_without_restart ovn-controller.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun ovn-controller.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%postun -n ovn-vtep
%if 0%{?suse_version}
    %service_del_postun_without_restart ovn-controller-vtep.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun ovn-controller-vtep.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%postun -n %{ovn_lname} -p /sbin/ldconfig

%posttrans -n ovn-central
# Save the "enabled" state across the transition of
# ownership of ovn-northd.service from openvswitch-ovn-central to
# ovn-central.
if [ -e %{rpmstate}ovn-northd ]; then
    rm %{rpmstate}ovn-northd
    systemctl enable ovn-northd.service
fi

%posttrans -n ovn-host
# Save the "enabled" state across the transition of
# ownership of ovn-northd.service from openvswitch-ovn-central to
# ovn-central.
if [ -e %{rpmstate}ovn-controller ]; then
    rm %{rpmstate}ovn-controller
    systemctl enable ovn-controller.service
fi

%posttrans -n ovn-vtep
# Save the "enabled" state across the transition of
# ownership of ovn-controller.service from openvswitch-ovn-host to
# ovn-host.
if [ -e %{rpmstate}ovn-controller-vtep ]; then
    rm %{rpmstate}ovn-controller-vtep
    systemctl enable ovn-controller-vtep.service
fi

%files
%defattr(-,root,openvswitch, 775)
%dir %{_sysconfdir}/openvswitch
%defattr(-,openvswitch,openvswitch)
%dir %{_localstatedir}/log/openvswitch
%config %ghost %{_sysconfdir}/openvswitch/system-id.conf
# This is no longer the DB path for new installs but we still need this for
# upgrades that preserve the old DB path.
%ghost %{_sysconfdir}/openvswitch/.conf.db.~lock~
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/openvswitch/default.conf
%{_bindir}/ovs-appctl
%{_bindir}/ovs-docker
%{_bindir}/ovs-dpctl
%{_bindir}/ovs-dpctl-top
%{_bindir}/ovs-ofctl
%{_bindir}/ovs-parse-backtrace
%{_bindir}/ovs-vsctl
%{_bindir}/ovsdb-client
%{_bindir}/ovsdb-tool
%{_sbindir}/ovs-bugtool
%{_sbindir}/ovs-vswitchd
%{_sbindir}/ovsdb-server
%dir %{_datadir}/openvswitch
%dir %{_datadir}/openvswitch/scripts
%dir %{_datadir}/openvswitch/scripts/usdt
%{_datadir}/openvswitch/bugtool-plugins
%{_datadir}/openvswitch/scripts/ovs-bugtool-*
%{_datadir}/openvswitch/scripts/ovs-check-dead-ifs
%{_datadir}/openvswitch/scripts/ovs-ctl
%{_datadir}/openvswitch/scripts/ovs-kmod-ctl
%{_datadir}/openvswitch/scripts/ovs-lib
%{_datadir}/openvswitch/scripts/ovs-save
%{_datadir}/openvswitch/scripts/usdt/*
%{_datadir}/openvswitch/vswitch.ovsschema
%{_datadir}/openvswitch/local-config.ovsschema
%{_mandir}/man1/ovsdb-client.1%{?ext_man}
%{_mandir}/man1/ovsdb-server.1%{?ext_man}
%{_mandir}/man1/ovsdb-tool.1%{?ext_man}
%{_mandir}/man5/ovs-vswitchd.conf.db.5%{?ext_man}
%{_mandir}/man5/ovsdb-server.5%{?ext_man}
%{_mandir}/man5/ovsdb.5%{?ext_man}
%{_mandir}/man7/ovs-actions.7%{?ext_man}
%{_mandir}/man7/ovs-fields.7%{?ext_man}
%{_mandir}/man7/ovsdb.7%{?ext_man}
%{_mandir}/man7/ovsdb-server.7%{?ext_man}
%{_mandir}/man8/ovs-appctl.8%{?ext_man}
%{_mandir}/man8/ovs-bugtool.8%{?ext_man}
%{_mandir}/man8/ovs-ctl.8%{?ext_man}
%{_mandir}/man8/ovs-dpctl-top.8%{?ext_man}
%{_mandir}/man8/ovs-dpctl.8%{?ext_man}
%{_mandir}/man8/ovs-kmod-ctl.8%{?ext_man}
%{_mandir}/man8/ovs-ofctl.8%{?ext_man}
%{_mandir}/man8/ovs-parse-backtrace.8%{?ext_man}
%{_mandir}/man8/ovs-vsctl.8%{?ext_man}
%{_mandir}/man8/ovs-vswitchd.8%{?ext_man}
%{_mandir}/man5/ovsdb.local-config.5.gz
%config(noreplace) %{_sysconfdir}/logrotate.d/openvswitch
%{_sbindir}/rcovsdb-server
%{_sbindir}/rcovs-vswitchd
%{_sbindir}/rcopenvswitch
%{_sbindir}/rcovs-delete-transient-ports
%{_unitdir}/openvswitch.service
%{_unitdir}/ovs-vswitchd.service
%{_unitdir}/ovsdb-server.service
%{_unitdir}/ovs-delete-transient-ports.service
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.openvswitch
%{_datadir}/bash-completion/completions/ovs-appctl-bashcomp.bash
%{_datadir}/bash-completion/completions/ovs-vsctl-bashcomp.bash
%{_sysusersdir}/openvswitch.conf
%else
%config(noreplace) %{_sysconfdir}/sysconfig/openvswitch
%{_sysconfdir}/bash_completion.d/ovs-appctl-bashcomp.bash
%{_sysconfdir}/bash_completion.d/ovs-vsctl-bashcomp.bash
%{_sysconfdir}/sysconfig/network-scripts/ifup-ovs
%{_sysconfdir}/sysconfig/network-scripts/ifdown-ovs
%endif
%ghost %attr(755,root,root) %{_rundir}/openvswitch
%ghost %attr(644,root,root) %{_rundir}/openvswitch.useropts
%exclude %{_docdir}/%{name}
%doc %ovs_dir/AUTHORS.rst %ovs_dir/CONTRIBUTING.rst %ovs_dir/NEWS %ovs_dir/README.rst
%license %ovs_dir/LICENSE %ovs_dir/NOTICE

%files doc
%exclude %{_docdir}/%{name}/AUTHORS.rst
%exclude %{_docdir}/%{name}/CONTRIBUTING.rst
%exclude %{_docdir}/%{name}/NEWS
%exclude %{_docdir}/%{name}/README.rst
%{_docdir}/%{name}/

%files -n %{ovs_lname}
%{_libdir}/libofproto-3*.so.*
%{_libdir}/libopenvswitch-3*.so.*
%{_libdir}/libovsdb-3*.so.*
%{_libdir}/libsflow-3*.so.*
%{_libdir}/libvtep-3*.so.*

%files pki
%{_mandir}/man8/ovs-pki.8%{?ext_man}
%{_bindir}/ovs-pki

%files vtep
%{_bindir}/vtep-ctl
%{_mandir}/man5/vtep.5%{?ext_man}
%{_mandir}/man8/vtep-ctl.8%{?ext_man}
%{_datadir}/openvswitch/scripts/ovs-vtep
%{_datadir}/openvswitch/vtep.ovsschema

%files ipsec
%{_datadir}/openvswitch/scripts/ovs-monitor-ipsec
%{_sbindir}/rcopenvswitch-ipsec
%{_unitdir}/openvswitch-ipsec.service

%files -n python3-ovs
%{python3_sitearch}/ovs/
%{python3_sitearch}/ovs-*.egg-info

%files test
%{_bindir}/ovs-l3ping
%{_bindir}/ovs-pcap
%{_bindir}/ovs-test
%{_bindir}/ovs-testcontroller
%{_bindir}/ovs-tcpdump
%{_bindir}/ovs-tcpundump
%{_bindir}/ovs-vlan-test
%{_mandir}/man1/ovs-pcap.1%{?ext_man}
%{_mandir}/man1/ovs-tcpundump.1%{?ext_man}
%{_mandir}/man8/ovs-l3ping.8%{?ext_man}
%{_mandir}/man8/ovs-tcpdump.8%{?ext_man}
%{_mandir}/man8/ovs-testcontroller.8%{?ext_man}
%{_mandir}/man8/ovs-test.8%{?ext_man}
%{_mandir}/man8/ovs-vlan-test.8%{?ext_man}
%{python3_sitelib}/ovstest/

%files devel
%{_libdir}/libofproto.so
%{_libdir}/libopenvswitch.so
%{_libdir}/libovsdb.so
%{_libdir}/libsflow.so
%{_libdir}/libvtep.so
%{_includedir}/openflow/
%{_includedir}/openvswitch/
%{_libdir}/pkgconfig/*.pc
# Devel tools required for OVN
%{_bindir}/ovsdb-idlc
%{_mandir}/man1/ovsdb-idlc.1%{?ext_man}
%dir %{_datadir}/openvswitch/ovsdb
%{_datadir}/openvswitch/ovsdb/ovsdb-doc
%{_datadir}/openvswitch/ovsdb/ovsdb-dot

%files -n ovn
%defattr(-,openvswitch,openvswitch)
%dir %{_localstatedir}/log/ovn
%defattr(-,root,root)
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.ovn
%else
%config(noreplace) %{_sysconfdir}/sysconfig/ovn
%endif
%{_bindir}/ovn-nbctl
%{_bindir}/ovn-sbctl
%{_bindir}/ovn-trace
%{_bindir}/ovn-detrace
%{_bindir}/ovn_detrace.py
%{_bindir}/ovn-appctl
%{_bindir}/ovn-ic-nbctl
%{_bindir}/ovn-ic-sbctl
%dir %{_datadir}/ovn
%dir %{_datadir}/ovn/scripts
%{_datadir}/ovn/scripts/ovn-ctl
%{_datadir}/ovn/scripts/ovn-lib
%{_datadir}/ovn/scripts/ovndb-servers.ocf
%{_datadir}/ovn/scripts/ovn-bugtool-nbctl-show
%{_datadir}/ovn/scripts/ovn-bugtool-sbctl-lflow-list
%{_datadir}/ovn/scripts/ovn-bugtool-sbctl-show
%{_mandir}/man5/ovn-nb.5%{?ext_man}
%{_mandir}/man5/ovn-sb.5%{?ext_man}
%{_mandir}/man8/ovn-ic-nbctl.8%{?ext_man}
%{_mandir}/man8/ovn-ic-sbctl.8%{?ext_man}
%{_mandir}/man8/ovn-ic.8%{?ext_man}
%{_mandir}/man5/ovn-ic-nb.5%{?ext_man}
%{_mandir}/man5/ovn-ic-sb.5%{?ext_man}
%{_mandir}/man1/ovn-detrace.1%{?ext_man}
%{_mandir}/man8/ovn-appctl.8%{?ext_man}
%{_mandir}/man7/ovn-architecture.7%{?ext_man}
%{_mandir}/man8/ovn-ctl.8%{?ext_man}
%{_mandir}/man8/ovn-nbctl.8%{?ext_man}
%{_mandir}/man8/ovn-trace.8%{?ext_man}
%{_mandir}/man8/ovn-sbctl.8%{?ext_man}
%config(noreplace) %{_sysconfdir}/logrotate.d/ovn
%doc %ovn_dir/AUTHORS.rst %ovn_dir/CONTRIBUTING.rst %ovn_dir/NEWS %ovn_dir/README.rst
%license %ovn_dir/LICENSE %ovn_dir/NOTICE

%files -n ovn-docker
%{_bindir}/ovn-docker-overlay-driver
%{_bindir}/ovn-docker-underlay-driver

%files -n ovn-central
# Can't use libexecdir because it differs between
# RedHat and SUSE and firewalld expects things in /usr/lib
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_bindir}/ovn-northd
%{_bindir}/ovn-ic
%{_mandir}/man8/ovn-northd.8%{?ext_man}
%{_datadir}/ovn/ovn-nb.ovsschema
%{_datadir}/ovn/ovn-sb.ovsschema
%{_datadir}/ovn/ovn-ic-nb.ovsschema
%{_datadir}/ovn/ovn-ic-sb.ovsschema
%{_unitdir}/ovn-northd.service
%{_sbindir}/rcovn-northd
%{_prefix}/lib/firewalld/services/ovn-central-firewall-service.xml

%files -n ovn-host
# Can't use libexecdir because it differs between
# RedHat and SUSE and firewalld expects things in /usr/lib
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_bindir}/ovn-controller
%{_mandir}/man8/ovn-controller.8%{?ext_man}
%{_unitdir}/ovn-controller.service
%{_sbindir}/rcovn-controller
%{_prefix}/lib/firewalld/services/ovn-host-firewall-service.xml

%files -n ovn-vtep
%{_bindir}/ovn-controller-vtep
%{_mandir}/man8/ovn-controller-vtep.8%{?ext_man}
%{_unitdir}/ovn-controller-vtep.service
%{_sbindir}/rcovn-controller-vtep

%files -n ovn-doc
%exclude %{_docdir}/ovn/AUTHORS.rst
%exclude %{_docdir}/ovn/CONTRIBUTING.rst
%exclude %{_docdir}/ovn/NEWS
%exclude %{_docdir}/ovn/README.rst
%{_docdir}/ovn/

%files -n %{ovn_lname}
%{_libdir}/libovn-*.so.*

%files -n ovn-devel
%{_libdir}/libovn.so
%{_includedir}/ovn/

%changelog
