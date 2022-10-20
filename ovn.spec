#
# spec file for package ovn
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


%define lname libovn-21_09-0
%define ovs_version 2.17.0
# Test suite requires ovs to be installed and database server running
%bcond_with check
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           ovn
Version:        21.09.1
Release:        0
Summary:        Open Virtual Network diagnostic utilities
License:        Apache-2.0
Group:          Productivity/Networking/System
URL:            http://ovn.org/
Source0:        https://github.com/ovn-org/ovn/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE: 0001-Run-ovn-as-openvswitch-openvswitch.patch
Patch0:         0001-Run-ovn-as-openvswitch-openvswitch.patch
Patch1:         0001-build-allow-building-with-installed-ovs.patch
Patch2:         0002-build-Add-missing-troff-macros.patch
Patch3:         0003-build-Fix-ovs-include-paths.patch
Patch4:         0004-add-xml.patch
Patch5:         0005-build-fix-ovs-function-signature.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  openvswitch-devel >= %{ovs_version}
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-Sphinx
BuildRequires:  python3-ovs >= %{ovs_version}
%if %{with check}
BuildRequires:  openvswitch >= %{ovs_version}
BuildRequires:  openvswitch-test >= %{ovs_version}
%endif
Suggests:       logrotate

%description
OVN, the Open Virtual Network, is a system to support virtual network
abstraction.  OVN complements the existing capabilities of OVS to add
native support for virtual network abstractions, such as virtual L2 and L3
overlays and security groups.

%package central
Summary:        Open Virtual Network support for Open vSwitch
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       openvswitch-dpdk-ovn:%{_bindir}/ovn-northd
Provides:       openvswitch-ovn-central = %{version}
Provides:       openvswitch-ovn:%{_bindir}/ovn-northd
Obsoletes:      openvswitch-ovn-central < 2.13.0

%description central
This subpackage contains the OVN database and northbound daemon.

%package host
Summary:        Open Virtual Network support for Open vSwitch
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       openvswitch-dpdk-ovn:%{_bindir}/ovn-controller
Provides:       openvswitch-ovn-host = %{version}
Provides:       openvswitch-ovn:%{_bindir}/ovn-controller
Obsoletes:      openvswitch-ovn-host < 2.13.0

%description host
This subpackage contains the OVN host controller.

%package vtep
Summary:        Open Virtual Network VTEP controller for Open vSwitch
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       openvswitch-dpdk-ovn:%{_bindir}/ovn-controller-vtep
Provides:       openvswitch-ovn-vtep = %{version}
Provides:       openvswitch-ovn:%{_bindir}/ovn-controller-vtep
Obsoletes:      openvswitch-ovn-vtep < 2.13.0

%description vtep
This subpackage contains the OVN VTEP (VXLAN Tunnel Endpoint) controller.

%package docker
Summary:        Docker network plugins for OVN
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}
Requires:       python3-ovs >= %{ovs_version}
# openvswitch-ovn has been split into openvswitch-ovn-{central,common,docker,host,vtep}
Provides:       openvswitch-dpdk-ovn:%{_bindir}/ovn-docker-overlay-driver
Provides:       openvswitch-ovn-docker = %{version}
Provides:       openvswitch-ovn:%{_bindir}/ovn-docker-overlay-driver
Obsoletes:      openvswitch-ovn-docker < 2.13.0

%description docker
This subpackage contains the OVN Docker network plugins.

%package doc
Summary:        Open Virtual Network Documentation
Group:          System/Libraries
BuildArch:      noarch

%description doc
Contains additional documentation for OVN.

%package -n %{lname}
Summary:        Open Virtual Network core libraries
Group:          System/Libraries

%description -n %{lname}
iThis subpackage contains the OVN shared libraries.

%package devel
Summary:        Development files for Open Virtual Network
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
Devel libraries and headers for Open Virtual Network.

%prep
%autosetup -p1

%build
bash -x boot.sh
%configure \
        --disable-static \
        --enable-shared \
        --enable-libcapng \
        --enable-ssl \
        --with-dbdir=%{_sharedstatedir}/ovn \
        --with-rundir=%{_rundir}/ovn \
        --with-logdir=%{_localstatedir}/log/ovn \
        --with-pkidir=%{_sharedstatedir}/openvswitch/pki \
        PYTHON3=%{_bindir}/python3
%make_build

%install
%make_install
# Clean up OVN files
rm -f %{buildroot}%{_datadir}/ovn/scripts/ovs*
rm -rf %{buildroot}%{_datadir}/ovn/bugtool-plugins
rm -f %{buildroot}%{_libdir}/*.a
find %{buildroot} -type f -name "*.la" -delete -print

# Remove known OVS dupes from OVN.
rm -f %{buildroot}%{_mandir}/man5/ovs*
rm -f %{buildroot}%{_mandir}/man7/ovs*

# Install OVN aditional files.
for service in ovn-controller \
               ovn-controller-vtep \
               ovn-northd; do
        install -D -m 644 rhel/usr_lib_systemd_system_${service}.service \
        %{buildroot}%{_unitdir}/${service}.service
        mkdir -p %{buildroot}%{_sbindir}
        ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc${service}
done
install -D -m 644 rhel/usr_share_ovn_scripts_systemd_sysconfig.template \
        %{buildroot}%{_fillupdir}/sysconfig.ovn

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

%if %{with check}
%check
export PATH="%{_sbindir}:$PATH"
echo "OVS database server needs to be running for the test suite"
if ! make check-local; then
	cat test-suite.log
	exit 1
fi
%endif

%pre central
%service_add_pre ovn-northd.service
# Save the "enabled" state across the transition of
# ownership of ovn-northd.service from openvswitch-ovn-central to
# ovn-central.
if [ "$1" -ge 1 ]; then
    if [ x$(systemctl is-enabled ovn-northd.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}ovn-northd
    fi
fi

%pre host
%service_add_pre ovn-controller.service
# Save the "enabled" state across the transition of
# ownership of ovn-controller.service from openvswitch-ovn-host to
# ovn-host.
if [ "$1" -ge 1 ]; then
    if [ x$(systemctl is-enabled ovn-controller.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}ovn-controller
    fi
fi

%pre vtep
%service_add_pre ovn-controller-vtep.service
# Save the "enabled" state across the transition of
# ownership of ovn-controller-vtep.service from openvswitch-ovn-vtep to
# ovn-vtep.
if [ "$1" -ge 1 ]; then
    if [ x$(systemctl is-enabled ovn-controller-vtep.service 2>/dev/null ||:) = "xenabled" ]; then
        touch %{rpmstate}ovn-controller-vtep
    fi
fi

%preun central
%service_del_preun ovn-northd.service

%preun host
%service_del_preun ovn-controller.service

%preun vtep
%service_del_preun ovn-controller-vtep.service

%post
if [ $1 -eq 1 ]; then
    # Follow the upstream strategy that no running openvswitch
    # configuration is changed on upgrade so use fillup only for new installs.
    %{?suse_version: %fillup_only}
fi

%post central
%service_add_post ovn-northd.service

%post host
%service_add_post ovn-controller.service

%post vtep
%service_add_post ovn-controller-vtep.service

%post -n %{lname} -p /sbin/ldconfig

%postun central
%service_del_postun_without_restart ovn-northd.service

%postun host
%service_del_postun_without_restart ovn-controller.service

%postun vtep
%service_del_postun_without_restart ovn-controller-vtep.service

%postun -n %{lname} -p /sbin/ldconfig

%posttrans central
# Save the "enabled" state across the transition of
# ownership of ovn-northd.service from openvswitch-ovn-central to
# ovn-central.
if [ -e %{rpmstate}ovn-northd ]; then
    rm %{rpmstate}ovn-northd
    systemctl enable ovn-northd.service
fi

%posttrans host
# Save the "enabled" state across the transition of
# ownership of ovn-northd.service from openvswitch-ovn-central to
# ovn-central.
if [ -e %{rpmstate}ovn-controller ]; then
    rm %{rpmstate}ovn-controller
    systemctl enable ovn-controller.service
fi

%posttrans vtep
# Save the "enabled" state across the transition of
# ownership of ovn-controller.service from openvswitch-ovn-host to
# ovn-host.
if [ -e %{rpmstate}ovn-controller-vtep ]; then
    rm %{rpmstate}ovn-controller-vtep
    systemctl enable ovn-controller-vtep.service
fi

%files
%defattr(-,openvswitch,openvswitch)
%dir %{_localstatedir}/log/ovn
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.ovn
%else
%config(noreplace) %{_sysconfdir}/sysconfig/ovn
%endif
%{_bindir}/ovn-nbctl
%{_bindir}/ovn-sbctl
%{_bindir}/ovn-trace
%{_bindir}/ovn-detrace
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
%attr(-,root,root) %doc AUTHORS.rst CONTRIBUTING.rst NEWS README.rst
%attr(-,root,root) %license LICENSE NOTICE

%files docker
%{_bindir}/ovn-docker-overlay-driver
%{_bindir}/ovn-docker-underlay-driver

%files central
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

%files host
# Can't use libexecdir because it differs between
# RedHat and SUSE and firewalld expects things in /usr/lib
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/services
%{_sbindir}/rcovn-controller
%{_bindir}/ovn-controller
%{_mandir}/man8/ovn-controller.8%{?ext_man}
%{_unitdir}/ovn-controller.service
%{_prefix}/lib/firewalld/services/ovn-host-firewall-service.xml

%files vtep
%{_sbindir}/rcovn-controller-vtep
%{_bindir}/ovn-controller-vtep
%{_mandir}/man8/ovn-controller-vtep.8%{?ext_man}
%{_unitdir}/ovn-controller-vtep.service

%files doc
%exclude %{_docdir}/ovn/AUTHORS.rst
%exclude %{_docdir}/ovn/CONTRIBUTING.rst
%exclude %{_docdir}/ovn/NEWS
%exclude %{_docdir}/ovn/README.rst
%attr(-,root,root) %{_docdir}/ovn/

%files -n %{lname}
%{_libdir}/libovn-*.so.*

%files devel
%{_libdir}/libovn.so
%{_includedir}/ovn/

%changelog
