#
# spec file for package openhpi
#
# Copyright (c) 2021 SUSE LLC
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


Name:           openhpi
Version:        3.8.0.ge4631e8a
Release:        0
Summary:        Implementation of SA Forum's Hardware Platform Interface (HPI)
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            https://github.com/open-hpi/openhpi
Source:         openhpi-%{version}.tar.xz
Source2:        AUTHORS
Patch1:         fix_openipmi_typedef_selector_change.patch
Patch2:         fix_implicit_declarations.patch
Patch3:         Use-run-instead-of-var-run.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-toys
BuildRequires:  docbook-utils
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(openssl)

%description
OpenHPI implements the SA Forum's Hardware Platform Interface (HPI). HPI is an
abstracted interface for managing computer hardware, typically for chassis and
rack based servers. HPI includes a resource model; access to and control over
sensor, control, watchdog, and inventory data associated with resources;
abstracted System Event Log interfaces; hardware events and alerts; and a
managed hotswap interface.

OpenHPI provides a modular mechanism for adding new hardware and device
support. Plug-ins exist for providing access to various types of hardware,
including IPMI-based servers, Blade Center, and machines that export data via
sysfs.

%package -n libopenhpi4
Summary:        OpenHPI base libraries
Group:          System/Libraries

%description -n libopenhpi4
OpenHPI implements the SA Forum's Hardware Platform Interface (HPI).

This subpackage contains the OpenHPI base libraries.

%package devel
Summary:        Development Files for HPI
Group:          Development/Libraries/C and C++
Requires:       OpenIPMI-devel
Requires:       bzip2
Requires:       e2fsprogs-devel
Requires:       gdbm-devel
Requires:       glib2-devel
Requires:       glibc-devel
Requires:       libopenhpi4 = %{version}
Requires:       libstdc++-devel
Requires:       libtool
Requires:       ncurses-devel
Requires:       net-snmp-devel
Requires:       pkgconfig(openssl)
Requires:       popt-devel
Requires:       zlib-devel

%description devel
Contains additional files needed for a developer to create applications
and/or middleware that use the Service Availability Forum's HPI
specification.

%package clients
Summary:        HPI Command-line Applications
Group:          System/Monitoring
Requires:       openhpi = %{version}

%description clients
This package contains HPI command-line utilities

OpenHPI implements the SA Forum's Hardware Platform Interface (HPI). HPI is an
abstracted interface for managing computer hardware, typically for chassis and
rack based servers.

%package daemon
Summary:        Implementation of SA Forum's Hardware Platform Interface (HPI)
Group:          System/Monitoring
Requires:       openhpi = %{version}
%{?systemd_requires}

%description daemon
OpenHPI implements the SA Forum's Hardware Platform Interface (HPI). HPI is an
abstracted interface for managing computer hardware, typically for chassis and
rack based servers.

%prep
%setup -q
%autopatch -p1

%build
autoreconf -fiv

# fix permissions
chmod a-x plugins/simulator/*.[ch]
chmod a-x clients/*.[ch]

export CFLAGS="%{optflags} -fno-strict-aliasing -DGLIB_DISABLE_DEPRECATION_WARNINGS"
export CXXFLAGS="${CFLAGS}"
%configure \
    --disable-static \
    --disable-ipmi --disable-sysfs --enable-daemon \
    --enable-ipmidirect --enable-simulator --enable-clients \
    --enable-ilo2_ribcl --enable-oa_soap \
    --with-systemdsystemunitdir=%{_unitdir} \
    --with-varpath=%{_localstatedir}/lib/%{name}
make %{?_smp_mflags}
make %{?_smp_mflags} documentation
###################################################

%install
###################################################
%make_install
install -Dd -m 0755 \
    %{buildroot}%{_sysconfdir}/openhpi \
    %{buildroot}%{_localstatedir}/lib/openhpi
install -m 0644 openhpi.conf.example %{buildroot}%{_sysconfdir}/openhpi/openhpi.conf
ln -sf service %{buildroot}%{_sbindir}/rcopenhpid
rm -rv %{buildroot}%{_datadir}/doc/%{name}
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n libopenhpi4 -p /sbin/ldconfig
%postun -n libopenhpi4 -p /sbin/ldconfig

%pre daemon
%service_add_pre openhpid.service

%preun daemon
%service_del_preun openhpid.service

%post daemon
%service_add_post openhpid.service
echo "Check OPENHPI_UNCONFIGURED in %{_sysconfdir}/openhpi/openhpi.conf"

%postun daemon
%service_del_postun openhpid.service

%files
%defattr(-,root,root,0755)
%dir %attr(0750,root,root) %{_sysconfdir}/openhpi
%config(noreplace) %attr(0600,root,root) %{_sysconfdir}/openhpi/*
%license COPYING
%doc ChangeLog README *.example
%dir %{_localstatedir}/lib/openhpi
%dir %{_libdir}/openhpi
%{_libdir}/openhpi/lib*.so*
%{_mandir}/man7/openhpi.7%{?ext_man}

%files -n libopenhpi4
%{_libdir}/libopen*.so.*

%files devel
%{_includedir}/openhpi
%{_libdir}/pkgconfig/openhpi.pc
%{_libdir}/pkgconfig/openhpiutils.pc
%{_libdir}/libopen*.so

%files clients
%{_bindir}/hpi*
%{_mandir}/man1/hpi*.1%{?ext_man}
%{_bindir}/oh*
%{_mandir}/man1/oh*.1%{?ext_man}

%files daemon
%doc README.daemon
%{_unitdir}/openhpid.service
%{_sbindir}/openhpid
%{_sbindir}/rcopenhpid
%{_mandir}/man8/openhpid.8%{?ext_man}

%changelog
