#
# spec file for package openvswitch
#
# Copyright (c) 2022 SUSE LLC
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
%define rpmstate %{_rundir}/openvswitch-rpm-state-
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%ifarch aarch64 x86_64 ppc64le
%bcond_without dpdk
%else
# No DPDK support on these architectures
%bcond_with dpdk
%endif
# The testsuite is somewhat fragile for continuous testing in OBS
%bcond_without check
# Disable building the external kernel datapath by default
%bcond_with kmp
%define lname libopenvswitch-2_17-0
Name:           openvswitch
Version:        2.17.2
Release:        0
Summary:        A multilayer virtual network switch
# All code is Apache-2.0 except
# - lib/sflow* which is SISSL
# - utilities/bugtool which is LGPL-2.1
License:        Apache-2.0 AND LGPL-2.1-only AND SISSL
Group:          Productivity/Networking/System
URL:            https://www.openvswitch.org/
Source0:        https://www.openvswitch.org/releases/openvswitch-%{version}.tar.gz
Source2:        preamble
Source89:       Module.supported.updates
Source99:       openvswitch-rpmlintrc
# PATCH-FIX-OPENSUSE: Use-strongswan-for-openvswitch-ipsec-service.patch
Patch0:         Use-strongswan-for-openvswitch-ipsec-service.patch
# PATCH-FIX-OPENSUSE: Run-openvswitch-as-openvswitch-openvswitch.patch
Patch1:         Run-openvswitch-as-openvswitch-openvswitch.patch
# PATCH-FIX-OPENSUSE: Don-t-change-permissions-of-dev-hugepages.patch
Patch2:         Don-t-change-permissions-of-dev-hugepages.patch
# PATCH-FIX-OPENSUSE: Use-double-hash-for-OVS_USER_ID-comment.patch
Patch3:         Use-double-hash-for-OVS_USER_ID-comment.patch
# PATCH-FEATURE-UPSTREAM install-ovsdb-tools.patch -- Install some tools required for building OVN
Patch4:         install-ovsdb-tools.patch
Patch5:         0001-openvswitch-merge-compiler.h-files-into-one-file.patch
Patch6:         0002-build-Seperated-common-used-headers.patch
Patch7:         openvswitch-2.17.2-Fix-tests-with-GNU-grep-3.8.patch
Patch8:         a77ad9693c8b49055389559187fe74eddb619746.patch
Patch9:         0001-m4-Test-avx512-for-x86-only.patch
# Python subpackage
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# Main package
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Sphinx
BuildRequires:  unbound-devel
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(openssl)
Requires:       modutils
# ovs-ctl / ovs-pki use /usr/bin/uuidgen:
Requires:       util-linux
Requires(post): %fillup_prereq
Requires(pre):  shadow
Suggests:       logrotate
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
%{?systemd_ordering}
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
BuildRequires:  dpdk-devel <= 21.12
BuildRequires:  dpdk-devel >= 20.11.0
BuildRequires:  libmnl-devel
BuildRequires:  libnuma-devel
BuildRequires:  libpcap-devel
BuildRequires:  rdma-core-devel
%endif
%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
%define python_sitelib %python3_sitelib
%define python_sitelib %{python3_sitelib}
%define python_files() -n python3-%{**}
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
Contains additional documentation for the Open vSwitch.

%package devel
Summary:        Development files for Open vSwitch
License:        Apache-2.0
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
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

%if 0%{?python_subpackage_only}
%package -n python-ovs
Summary:        Python bindings for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{lname} = %{version}
Requires:       python-sortedcontainers

%description -n python-ovs
This package contains the Python3 bindings for Open vSwitch database.
%else

%package -n python3-ovs
Summary:        Python bindings for Open vSwitch
License:        Apache-2.0
Group:          Productivity/Networking/System
Requires:       %{lname} = %{version}
Requires:       python-sortedcontainers

%description -n python3-ovs
This package contains the Python3 bindings for Open vSwitch database.
%endif

%prep
%autosetup -p1

%build
autoreconf -fi

# Build kernel modules if needed.
%if %{with kmp}
    mkdir kmp
    export EXTRA_CFLAGS='-DVERSION=\"%{version}\"'
    for flavor in %{flavors_to_build}; do
        rm -rf kmp/$flavor
        mkdir -p kmp/$flavor
        pushd kmp/$flavor
        tar -xf "%{SOURCE0}"
        cp -a %{SOURCE89} datapath/linux/Module.supported
        %configure \
            --with-logdir=%{_localstatedir}/log/openvswitch \
            --with-rundir=%{_rundir}/openvswitch \
            --with-linux=%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor \
            --with-linux-source=%{_prefix}/src/linux
        cd datapath/linux
        %make_build
        popd
    done
%endif

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
    --with-dbdir=%{_sharedstatedir}/openvswitch \
    --with-rundir=%{_rundir}/openvswitch \
    --with-logdir=%{_localstatedir}/log/openvswitch \
    --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
    PYTHON3=%{_bindir}/python3
%make_build

%check
%if %{with check}
touch resolv.conf
export OVS_RESOLV_CONF=$(pwd)/resolv.conf
mv python/build python/pb
ln -s _build.tmp python/build

# Recheck tests before we declare them broken. If that fails, dump
# the log and exit. >2.5.0 uses the RECHECK env variable so this
# needs to be taken into consideration for future releases.
if ! make check-am TESTSUITEFLAGS="%{?_smp_mflags}" &&
   ! make check-am TESTSUITEFLAGS='--recheck'; then
    cat tests/testsuite.log
    exit 1
fi
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

%make_install
# Remove static libraries and libtool files
rm -f %{buildroot}%{_libdir}/*.{l,}a

# Fix installation path
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions/
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/ovs-* %{buildroot}/%{_datadir}/bash-completion/completions/
chmod 0644 %{buildroot}/%{_datadir}/bash-completion/completions/*

# Install systemd files
for service in openvswitch \
               ovsdb-server \
               ovs-vswitchd \
               ovs-delete-transient-ports \
               openvswitch-ipsec; do
        install -D -m 644 rhel/usr_lib_systemd_system_${service}.service \
        %{buildroot}%{_unitdir}/${service}.service
        ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc${service}
done

install -D -m 644 rhel/usr_share_openvswitch_scripts_systemd_sysconfig.template \
        %{buildroot}%{_fillupdir}/sysconfig.openvswitch

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

# Python subpackage
# Install python tests package
mkdir -p %{buildroot}%{python3_sitelib}
cp -a %{buildroot}%{_datadir}/openvswitch/python/ovstest \
      %{buildroot}%{python3_sitelib}
# Remove non standard location python package
rm -rf %{buildroot}%{_datadir}/openvswitch/python
# Install python package, some files are generated by make install
# make sure dirs.py is freshly generated
rm -f python/ovs/dirs.py
make python/ovs/dirs.py
pushd python
export LDFLAGS="${LDFLAGS} -L %{buildroot}%{_libdir}"
export CPPFLAGS="-I %{buildroot}%{_includedir} -I %{buildroot}%{_includedir}/openvswitch"
%python_build
%python_install
popd
# Currently (version 2.17) the c parser for json is broken on 32bit (int overflow for number parsing)
%ifarch i386 i586 i686
%python_expand rm -v %{buildroot}%{$python_sitearch}/ovs/_json*.so
%endif

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%pre
%service_add_pre ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service
if [ "$1" -ge 1 ]; then
    # Save the "enabled" state across the transition of
    # ownership of openvswitch.service from openvswitch-switch to
    # openvswitch.
    if [ x$(systemctl is-enabled openvswitch.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}openvswitch
    fi
fi

getent group openvswitch >/dev/null || groupadd -r openvswitch
getent passwd openvswitch >/dev/null || \
    useradd -r -g openvswitch -d / -s /sbin/nologin \
    -c "Open vSwitch Daemons" openvswitch

exit 0

%pre ipsec
%service_add_pre openvswitch-ipsec.service

%preun
%service_del_preun ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service

%preun ipsec
%service_del_preun openvswitch-ipsec.service

%preun test
%service_del_preun openvswitch-testcontroller

%post
if [ $1 -eq 1 ]; then
    # Follow the upstream strategy that no running openvswitch
    # configuration is changed on upgrade so use fillup only for new installs.
    %{?suse_version: %fillup_only -n openvswitch}
fi
%service_add_post ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service

%post ipsec
%service_add_post openvswitch-ipsec.service

%post -n %{lname} -p /sbin/ldconfig

%postun
# Do not restart the openvswitch service on package updates.
# Restarting the service may break the existing network state.
# For example, openflow rules are not automatically re-installed
# after an OvS update if no SDN controller is used. Moreover, restaring
# the OvS can break remote administration during the update so let the
# admin decide when it's the best time for an OvS restart.
%service_del_postun_without_restart ovsdb-server.service ovs-vswitchd.service openvswitch.service ovs-delete-transient-ports.service

%postun ipsec
%service_del_postun_without_restart openvswitch-ipsec.service

%postun test
%service_del_postun_without_restart openvswitch-testcontroller

%postun -n %{lname} -p /sbin/ldconfig

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

%files
%defattr(-,root,openvswitch, 775)
%dir %{_sysconfdir}/openvswitch
%defattr(-,openvswitch,openvswitch)
%dir %{_localstatedir}/log/openvswitch
%config %ghost %{_sysconfdir}/openvswitch/system-id.conf
# This is no longer the DB path for new installs but we still need this for
# upgrades that preserve the old DB path.
%ghost %{_sysconfdir}/openvswitch/.conf.db.~lock~
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
%config(noreplace) %{_sysconfdir}/logrotate.d/openvswitch
%{_sbindir}/rcovsdb-server
%{_sbindir}/rcovs-vswitchd
%{_sbindir}/rcopenvswitch
%{_sbindir}/rcovs-delete-transient-ports
%{_unitdir}/openvswitch.service
%{_unitdir}/ovs-vswitchd.service
%{_unitdir}/ovsdb-server.service
%{_unitdir}/ovs-delete-transient-ports.service
%{_fillupdir}/sysconfig.openvswitch
%{_datadir}/bash-completion/completions/ovs-appctl-bashcomp.bash
%{_datadir}/bash-completion/completions/ovs-vsctl-bashcomp.bash
%ghost %attr(755,root,root) %{_rundir}/openvswitch
%ghost %attr(644,root,root) %{_rundir}/openvswitch.useropts
%exclude %{_docdir}/%{name}
%doc AUTHORS.rst CONTRIBUTING.rst NEWS README.rst
%license LICENSE NOTICE

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

%files %{python_files ovs}
%license LICENSE NOTICE
%{python_sitearch}/ovs
%{python_sitearch}/ovs-%{version}*

%changelog
