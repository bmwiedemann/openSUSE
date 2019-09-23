#
# spec file for package openvswitch
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
# needssslcertforbuild


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%define lname libopenvswitch-2_11-0
%ifarch aarch64 x86_64
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
Name:           openvswitch
Version:        2.11.1
Release:        0
Summary:        A multilayer virtual network switch
# All code is Apache-2.0 except
# - lib/sflow* which is SISSL
# - utilities/bugtool which is LGPL-2.1
License:        Apache-2.0 AND LGPL-2.1-only AND SISSL
Group:          Productivity/Networking/System
Url:            http://openvswitch.org/
Source0:        http://openvswitch.org/releases/openvswitch-%{version}.tar.gz
Source1:        preamble
Source89:       Module.supported.updates
# PATCH-FIX-OPENSUSE: Use-strongswan-for-openvswitch-ipsec-service.patch
Patch0:         0001-Use-strongswan-for-openvswitch-ipsec-service.patch
# PATCH-FIX-UPSTREAM: 0001-rhel-secure-openvswitch-useropts.patch
Patch1:         0001-rhel-secure-openvswitch-useropts.patch
# PATCH-FIX-UPSTREAM: 0002-rhel-let-ctl-handle-runtime-directory.patch
Patch2:         0002-rhel-let-ctl-handle-runtime-directory.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  graphviz
BuildRequires:  libcap-ng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
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
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  python-rpm-macros
Requires(post): %fillup_prereq
Requires(pre):  shadow
Suggests:       logrotate
%{?systemd_ordering}
%else
BuildRequires:  findutils
BuildRequires:  openssl-devel
BuildRequires:  python-devel
BuildRequires:  python-six
BuildRequires:  python2-rpm-macros
BuildRequires:  python2-setuptools
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
# releases. This version currently requires 18.11.
BuildRequires:  dpdk-devel < 18.12
BuildRequires:  dpdk-devel >= 18.11
BuildRequires:  libmnl-devel
BuildRequires:  libnuma-devel
BuildRequires:  libpcap-devel
BuildRequires:  rdma-core-devel
%endif
BuildRequires:  unbound-devel

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

%package -n %{lname}
Summary:        Open vSwitch core libraries
License:        Apache-2.0
Group:          System/Libraries

%description -n %{lname}
Contains the shared libraries used by Open vSwitch and any eventual extensions.

%package doc
Summary:        Open vSwitch Documentation
License:        Apache-2.0
Group:          System/Libraries
BuildArch:      noarch

%description doc
Contains additional documentation for the Open vSwitch

%package devel
Summary:        Development files for Open vSwitch
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Provides:       %{name}-dpdk-devel = %{version}
Obsoletes:      %{name}-dpdk-devel < 2.7.0

%description devel
Devel libraries and headers for Open vSwitch.

%package ovn-central
Summary:        Open Virtual Network support for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       %{name}-ovn-common
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-northd
Provides:       %{name}-ovn:%{_bindir}/ovn-northd

%description ovn-central
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package ovn-host
Summary:        Open Virtual Network support for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       %{name}-ovn-common
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-controller
Provides:       %{name}-ovn:%{_bindir}/ovn-controller

%description ovn-host
This subpackage contains the OVN host controller.

%package ovn-vtep
Summary:        Open Virtual Network VTEP controller for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       %{name}-ovn-common
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-controller-vtep
Provides:       %{name}-ovn:%{_bindir}/ovn-controller-vtep

%description ovn-vtep
This subpackage contains the OVN VTEP (VXLAN Tunnel Endpoint) controller.

%package ovn-common
Summary:        Open Virtual Network diagnostic utilities
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn = %{version}
Provides:       %{name}-ovn = %{version}
Obsoletes:      %{name}-dpdk-ovn < 2.7.0
Obsoletes:      %{name}-ovn < 2.7.0

%description ovn-common
Utilities that are used to diagnose and manage the OVN components.

%package ovn-docker
Summary:        Docker network plugins for OVN
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       %{name}-ovn-common = %{version}
Requires:       python-openvswitch = %{version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       %{name}-dpdk-ovn:%{_bindir}/ovn-docker-overlay-driver
Provides:       %{name}-ovn:%{_bindir}/ovn-docker-overlay-driver

%description ovn-docker
Docker network plugins for OVN.

%package pki
Summary:        Open vSwitch public key infrastructure dependency package
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
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
Requires:       python-openvswitch = %{version}
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
Requires:       python-openvswitch = %{version}
Requires:       strongswan

%description ipsec
This package provides IPsec tunneling support for OVS tunnels.

%package -n python2-ovs
Summary:        Python2 bindings for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{lname} = %{version}
Requires:       python2
Requires:       python2-six
Provides:       python-%{name} = %{version}
Provides:       python-ovs = %{version}
Provides:       python2-%{name} = %{version}
Obsoletes:      python-%{name} < 2.8.1
Obsoletes:      python-ovs < 2.8.1
Obsoletes:      python2-%{name} < 2.10.1

%description -n python2-ovs
This package contains the Python2 bindings for Open vSwitch database.

%package -n python3-ovs
Summary:        Python3 bindings for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{lname} = %{version}
Requires:       python3
Requires:       python3-six
Provides:       python3-%{name} = %{version}
Obsoletes:      python3-%{name} < 2.10.1

%description -n python3-ovs
This package contains the Python3 bindings for Open vSwitch database.

%package test
Summary:        Open vSwitch test package
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       python2
Requires:       python2-Twisted
Requires:       python2-ovs = %{version}
Provides:       %{name}-dpdk-test = %{version}
Provides:       python-%{name}-test = %{version}
Provides:       python2-%{name}-test = %{version}
Obsoletes:      %{name}-dpdk-test < 2.7.0
Obsoletes:      python-%{name}-test < 2.8.1
Obsoletes:      python2-%{name}-test < 2.10.1

%description test
Open vSwitch is a software-based Ethernet switch.

This package contains utilities that are useful to diagnose
performance and connectivity issues in Open vSwitch setup.

%prep
%setup -q -n openvswitch-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
set -- * .travis* .mailmap .cirrus.yml
mkdir source
mv "$@" source/
mkdir obj

pushd source
# only call boot.sh for distros with autoconf >= 2.64
bash -x boot.sh
popd
%if %{with kmp}
    export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
    for flavor in %{flavors_to_build}; do
        rm -rf obj/$flavor
        cp -r source obj/$flavor
        cp -a %{SOURCE89} obj/$flavor/datapath/linux/Module.supported
        pushd obj/$flavor
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

pushd source

%if %{with dpdk}
    dpdk_opt="--with-dpdk"
%endif

%{_bindir}/python build-aux/dpdkstrip.py \
%if %{with dpdk}
    --dpdk \
%else
    --nodpdk \
%endif
    < rhel/usr_lib_systemd_system_ovs-vswitchd.service.in \
    > rhel/usr_lib_systemd_system_ovs-vswitchd.service

# This is only used for building the ovstest module
export PYTHON='%{_bindir}/python2'

%configure \
        --disable-static \
        --enable-libcapng \
        --enable-shared \
        --enable-ssl \
        ${dpdk_opt} \
        --with-rundir=%{_rundir}/openvswitch \
        --with-logdir=%{_localstatedir}/log/openvswitch
make %{?_smp_mflags}
popd

%check
%if %{with check}
pushd source
touch resolv.conf
export OVS_RESOLV_CONF=$(pwd)/resolv.conf

# Recheck tests before we declare them broken. If that fails, dump
# the log and exit. >2.5.0 uses the RECHECK env variable so this
# needs to be taken into consideration for future releases.
if ! make check TESTSUITEFLAGS="%{?_smp_mflags}" &&
   ! make check TESTSUITEFLAGS='--recheck'; then
    cat tests/testsuite.log
    exit 1
fi
popd
%endif

%install
%if %{with kmp}
export NO_BRP_STALE_LINK_ERROR=yes
export INSTALL_MOD_PATH=%{buildroot}
export INSTALL_MOD_DIR=updates
export BRP_PESIGN_FILES="*.ko /lib/firmware"
for flavor in %{flavors_to_build}; do
    pushd obj/$flavor/datapath/linux
    make -C %{_prefix}/src/linux-obj/%{_target_cpu}/$flavor modules_install M=$PWD
    popd
done
%endif

pushd source

%make_install

# Install extra headers not included with 'make install'
copy_headers() {
    src=$1
    dst=$RPM_BUILD_ROOT/$2
    install -d -m 0755 $dst
    install -m 0644 $src/*.h $dst
}
copy_headers include/sparse %{_includedir}/openvswitch/sparse
copy_headers include/sparse/arpa %{_includedir}/openvswitch/sparse/arpa
copy_headers include/sparse/netinet %{_includedir}/openvswitch/sparse/netinet
copy_headers include/sparse/sys %{_includedir}/openvswitch/sparse/sys
copy_headers lib %{_includedir}/openvswitch/lib

for service in openvswitch ovn-controller ovn-controller-vtep \
    ovn-northd ovsdb-server ovs-vswitchd ovs-delete-transient-ports \
    openvswitch-ipsec; do
        install -D -m 644 rhel/usr_lib_systemd_system_${service}.service \
        %{buildroot}%{_unitdir}/${service}.service
        ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc${service}
done

%if %{with dpdk}
    install -p -D -m 0644 rhel/usr_lib_udev_rules.d_91-vfio.rules \
    %{buildroot}%{_prefix}/lib/udev/rules.d/91-vfio.rules
%endif

%if 0%{?suse_version}
install -D -m 644 rhel/usr_share_openvswitch_scripts_systemd_sysconfig.template \
        %{buildroot}%{_fillupdir}/sysconfig.openvswitch

# fixing W: suse-filelist-forbidden-bashcomp-userdirs /etc/bash_completion.d/ovs-appctl-bashcomp.bash is not allowed in SUSE
mkdir -p %{buildroot}/%{_prefix}/share/bash-completion/completions/
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/ovs-* %{buildroot}/%{_prefix}/share/bash-completion/completions/

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
install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d

install -m 644 vswitchd/vswitch.ovsschema \
         %{buildroot}%{_datadir}/openvswitch/vswitch.ovsschema

# firewalld
install -d %{buildroot}%{_prefix}/lib/firewalld/services/
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-central-firewall-service.xml \
        %{buildroot}%{_prefix}/lib/firewalld/services/ovn-central-firewall-service.xml
install -p -m 0644 rhel/usr_lib_firewalld_services_ovn-host-firewall-service.xml \
        %{buildroot}%{_prefix}/lib/firewalld/services/ovn-host-firewall-service.xml

# Copy documentation.
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r Documentation/* %{buildroot}%{_docdir}/%{name}
find %{buildroot}%{_docdir}/%{name}/ -type f ! -name '*.rst' -delete

popd

# Tests
mkdir -p %{buildroot}%{python2_sitelib}
cp -a %{buildroot}%{_datadir}/openvswitch/python/ovstest \
    %{buildroot}%{python2_sitelib}

# Python subpackages
# Build on a temporary directory.
pushd $(mktemp -d -p source/build-aux)
cp -a ../../python/* $(pwd)/

# Some build files are in sources while others are generated directly on
# buildroot as part of make_install (dirs.py), so update the former with the
# latter.
cp -a %{buildroot}%{_datadir}/openvswitch/python/* $(pwd)/

export LDFLAGS="${LDFLAGS} -L %{buildroot}%{_libdir}"
export CPPFLAGS="-I ../../include"

%if 0%{?suse_version}
# SLES
%{python_build}
%{python_install}
%fdupes %{buildroot}%{python2_sitearch}
%fdupes %{buildroot}%{python3_sitearch}

%else
# RHEL
%py2_build
%py2_install
# No python3 for RHEL. We are missing python3-* packages from EPEL
%endif

popd

rm -rf %{buildroot}%{_datadir}/openvswitch/python

find %{buildroot} -type f -name "*.la" -delete -print

%define eflag /run/openvswitch-was-enabled

%post
/sbin/ldconfig

if [ $1 -eq 1 ]; then
    # Follow the upstream strategy that no running openvswitch
    # configuration is changed on upgrade so use fillup only for new installs.
    %{?suse_version: %fillup_only -n openvswitch}

%if %{with dpdk}
    %define rgroup hugetlbfs
%else
    %define rgroup openvswitch
%endif

    sed -i \
        's@^#OVS_USER_ID="openvswitch:openvswitch"@OVS_USER_ID="openvswitch:%{rgroup}"@'\
        %{_sysconfdir}/sysconfig/openvswitch
    sed -i 's:\(.*su\).*:\1 openvswitch %{rgroup}:' %{_sysconfdir}/logrotate.d/openvswitch

    # In the case of upgrade, this is not needed
    chown -R openvswitch:openvswitch %{_sysconfdir}/openvswitch
    chown -R openvswitch:%{rgroup} %{_localstatedir}/log/openvswitch
fi
%if 0%{?suse_version}
	%service_add_post ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service
%else
    %if 0%{?systemd_post:1}
        %systemd_post %{name}.service
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

%posttrans
# Save the "enabled" state across the transition of ownership
# of openvswitch.service from openvswitch-switch to
# openvswitch.
if test -f %{eflag}; then
    rm -f %{eflag}
    systemctl enable openvswitch.service
fi

%postun
/sbin/ldconfig
# Do not restart the openvswitch service on package updates.
# Restarting the service may break the existing network state.
# For example, openflow rules are not automatically re-installed
# after an OvS update if no SDN controller is used. Moreover, restaring
# the OvS can break remote administration during the update so let the
# admin decide when it's the best time for an OvS restart.
# 5771f476573445710834234a6a9f7bd999a027e7 ("fedora: do not restart the service on a pkg upgrade")
%if 0%{?suse_version}
    %service_del_postun -n ovsdb-server.service -n ovs-vswitchd.service -n openvswitch.service -n ovs-delete-transient-ports.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun %{name}.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%postun ipsec
%if 0%{?suse_version}
	%service_del_postun -n openvswitch-ipsec.service
%endif

%pre
%if 0%{?suse_version}
%service_add_pre ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service
%endif
# Save the "enabled" state across the transition of
# ownership of openvswitch.service from openvswitch-switch to
# openvswitch.
if [ "$1" -ge 1 ]; then \
    if [ x$(systemctl is-enabled openvswitch.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{eflag}
    fi
fi

getent group openvswitch >/dev/null || groupadd -r openvswitch
getent passwd openvswitch >/dev/null || \
    useradd -r -g openvswitch -d / -s /sbin/nologin \
    -c "Open vSwitch Daemons" openvswitch

%if %{with dpdk}
    getent group hugetlbfs >/dev/null || \
    groupadd -r hugetlbfs
    usermod -a -G hugetlbfs openvswitch
%endif
exit 0

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

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%pre ovn-central
%if 0%{?suse_version}
%service_add_pre ovn-northd.service
%endif

%pre ovn-host
%if 0%{?suse_version}
%service_add_pre ovn-controller.service
%endif

%pre ovn-vtep
%if 0%{?suse_version}
%service_add_pre ovn-controller-vtep.service
%endif

%post ovn-central
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

%post ovn-host
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

%post ovn-vtep
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

%preun ovn-central
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

%preun ovn-host
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

%preun ovn-vtep
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

%postun ovn-central
%if 0%{?suse_version}
    %service_del_postun -n ovn-northd.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun ovn-northd.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%post ovn-common -p /sbin/ldconfig
%postun ovn-common -p /sbin/ldconfig
%postun ovn-host
%if 0%{?suse_version}
    %service_del_postun -n ovn-controller.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun ovn-controller.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%postun ovn-vtep
%if 0%{?suse_version}
    %service_del_postun -n ovn-controller-vtep.service
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun ovn-controller-vtep.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
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

%postun test
%if 0%{?suse_version}
    %service_del_postun -n openvswitch-testcontroller
%else
    %if 0%{?systemd_postun:1}
        %systemd_postun openvswitch-testcontroller.service
    %else
        /bin/systemctl daemon-reload >/dev/null 2>&1 || :
    %endif
%endif

%post vtep -p /sbin/ldconfig
%postun vtep -p /sbin/ldconfig

%files
%defattr(-,openvswitch,openvswitch)
%dir %{_sysconfdir}/openvswitch
%config(noreplace) %{_sysconfdir}/openvswitch/default.conf
%config %ghost %{_sysconfdir}/openvswitch/conf.db
%ghost %{_sysconfdir}/openvswitch/.conf.db.~lock~
%config %ghost %{_sysconfdir}/openvswitch/system-id.conf
%defattr(-,root,root)
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
%{_sbindir}/ovs-vlan-bug-workaround
%{_sbindir}/ovs-vswitchd
%{_sbindir}/ovsdb-server
%dir %{_datadir}/openvswitch
%dir %{_datadir}/openvswitch/scripts
%{_datadir}/openvswitch/bugtool-plugins
%{_datadir}/openvswitch/scripts/ovs-bugtool-*
%{_datadir}/openvswitch/scripts/ovs-check-dead-ifs
%{_datadir}/openvswitch/scripts/ovs-ctl
%{_datadir}/openvswitch/scripts/ovs-kmod-ctl
%{_datadir}/openvswitch/scripts/ovs-lib
%{_datadir}/openvswitch/scripts/ovs-save
%{_datadir}/openvswitch/vswitch.ovsschema
%{_mandir}/man1/ovsdb-client.1%{?ext_man}
%{_mandir}/man1/ovsdb-server.1%{?ext_man}
%{_mandir}/man1/ovsdb-tool.1%{?ext_man}
%{_mandir}/man5/ovs-vswitchd.conf.db.5%{?ext_man}
%{_mandir}/man5/ovsdb-server.5%{?ext_man}
%{_mandir}/man7/ovs-actions.7%{?ext_man}
%{_mandir}/man7/ovs-fields.7%{?ext_man}
%{_mandir}/man8/ovs-appctl.8%{?ext_man}
%{_mandir}/man8/ovs-bugtool.8%{?ext_man}
%{_mandir}/man8/ovs-ctl.8%{?ext_man}
%{_mandir}/man8/ovs-dpctl-top.8%{?ext_man}
%{_mandir}/man8/ovs-dpctl.8%{?ext_man}
%{_mandir}/man8/ovs-kmod-ctl.8%{?ext_man}
%{_mandir}/man8/ovs-ofctl.8%{?ext_man}
%{_mandir}/man8/ovs-vlan-bug-workaround.8%{?ext_man}
%{_mandir}/man8/ovs-parse-backtrace.8%{?ext_man}
%{_mandir}/man8/ovs-vsctl.8%{?ext_man}
%{_mandir}/man8/ovs-vswitchd.8%{?ext_man}
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
%else
%config(noreplace) %{_sysconfdir}/sysconfig/openvswitch
%{_sysconfdir}/bash_completion.d/ovs-appctl-bashcomp.bash
%{_sysconfdir}/bash_completion.d/ovs-vsctl-bashcomp.bash
%{_sysconfdir}/sysconfig/network-scripts/ifup-ovs
%{_sysconfdir}/sysconfig/network-scripts/ifdown-ovs
%endif
%attr(750,root,root) %dir %{_localstatedir}/log/openvswitch
%ghost %attr(755,root,root) %{_rundir}/openvswitch
%ghost %attr(644,root,root) %{_rundir}/openvswitch.useropts
%if %{with dpdk}
%{_prefix}/lib/udev/rules.d/91-vfio.rules
%endif
%exclude %{_docdir}/%{name}
%doc source/AUTHORS.rst source/CONTRIBUTING.rst source/NEWS source/README.rst
%license source/LICENSE source/NOTICE

%files doc
%exclude %{_docdir}/%{name}/AUTHORS.rst
%exclude %{_docdir}/%{name}/CONTRIBUTING.rst
%exclude %{_docdir}/%{name}/NEWS
%exclude %{_docdir}/%{name}/README.rst
%{_docdir}/%{name}/

%files -n %{lname}
%{_libdir}/libofproto-2*.so.*
%{_libdir}/libopenvswitch-2*.so.*
%{_libdir}/libovsdb-2*.so.*
%{_libdir}/libsflow-2*.so.*
%{_libdir}/libovn-2*.so.*
%{_libdir}/libvtep-2*.so.*

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

%files -n python2-ovs
%{python2_sitearch}/ovs/
%{python2_sitearch}/ovs-*.egg-info

%if 0%{?suse_version}
%files -n python3-ovs
%{python3_sitearch}/ovs/
%{python3_sitearch}/ovs-*.egg-info
%endif

%files ovn-docker
%{_bindir}/ovn-docker-overlay-driver
%{_bindir}/ovn-docker-underlay-driver

%files ovn-common
%{_bindir}/ovn-nbctl
%{_bindir}/ovn-sbctl
%{_bindir}/ovn-trace
%{_bindir}/ovn-detrace
%{_datadir}/openvswitch/scripts/ovn-ctl
%{_datadir}/openvswitch/scripts/ovndb-servers.ocf
%{_datadir}/openvswitch/scripts/ovn-bugtool-nbctl-show
%{_datadir}/openvswitch/scripts/ovn-bugtool-sbctl-lflow-list
%{_datadir}/openvswitch/scripts/ovn-bugtool-sbctl-show
%{_mandir}/man5/ovn-nb.5%{?ext_man}
%{_mandir}/man5/ovn-sb.5%{?ext_man}
%{_mandir}/man1/ovn-detrace.1%{?ext_man}
%{_mandir}/man7/ovn-architecture.7%{?ext_man}
%{_mandir}/man8/ovn-ctl.8%{?ext_man}
%{_mandir}/man8/ovn-nbctl.8%{?ext_man}
%{_mandir}/man8/ovn-trace.8%{?ext_man}
%{_mandir}/man8/ovn-sbctl.8%{?ext_man}

%files ovn-central
# Can't use libexecdir because it differs between
# RedHat and SUSE and firewalld expects things in /usr/lib
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_bindir}/ovn-northd
%{_mandir}/man8/ovn-northd.8%{?ext_man}
%{_datadir}/openvswitch/ovn-nb.ovsschema
%{_datadir}/openvswitch/ovn-sb.ovsschema
%{_unitdir}/ovn-northd.service
%{_sbindir}/rcovn-northd
%{_prefix}/lib/firewalld/services/ovn-central-firewall-service.xml

%files ovn-host
# Can't use libexecdir because it differs between
# RedHat and SUSE and firewalld expects things in /usr/lib
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_bindir}/ovn-controller
%{_mandir}/man8/ovn-controller.8%{?ext_man}
%{_unitdir}/ovn-controller.service
%{_sbindir}/rcovn-controller
%{_prefix}/lib/firewalld/services/ovn-host-firewall-service.xml

%files ovn-vtep
%{_bindir}/ovn-controller-vtep
%{_mandir}/man8/ovn-controller-vtep.8%{?ext_man}
%{_unitdir}/ovn-controller-vtep.service
%{_sbindir}/rcovn-controller-vtep

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
%{python2_sitelib}/ovstest/

%files devel
%{_libdir}/libofproto.so
%{_libdir}/libopenvswitch.so
%{_libdir}/libovn.so
%{_libdir}/libovsdb.so
%{_libdir}/libsflow.so
%{_libdir}/libvtep.so
%{_includedir}/openflow/
%{_includedir}/ovn/
%{_includedir}/openvswitch/
%{_libdir}/pkgconfig/*.pc

%changelog
