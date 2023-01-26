#
# spec file for package dlt-daemon
#
# Copyright (c) 2023 SUSE LLC
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


Name:           dlt-daemon
Version:        2.18.8
Release:        4%{?dist}
Summary:        DLT - Diagnostic Log and Trace
License:        MPL-2.0-no-copyleft-exception
Group:          Development/Tools/Other
URL:            https://github.com/COVESA/dlt-daemon
Source0:        https://github.com/COVESA/dlt-daemon/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Patch0:         dlt-daemon-config.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pandoc
BuildRequires:  systemd
BuildRequires:  systemd-devel
Requires(pre):  shadow
ExcludeArch:    %{ix86}


%description
This component provides a standardised log and trace interface, based on the
standardised protocol specified in the AUTOSAR standard 4.0 DLT.
This component can be used by GENIVI components and other applications as
logging facility providing
- the DLT shared library
- the DLT daemon, including startup scripts
- the DLT daemon adaptors
- the DLT client console utilities
- the DLT test applications

%package -n dlt-libs-devel
Summary:        DLT - Diagnostic Log and Trace: Development files
Requires:       dlt-libs = %{version}-%{release}

%description -n dlt-libs-devel
%{summary}.

%package -n dlt-libs
Summary:        DLT - Diagnostic Log and Trace: Libraries

%description -n dlt-libs
%{summary}.

%package -n dlt-tools
Summary:        DLT - Diagnostic Log and Trace: Tools
Recommends:     %{name} = %{version}-%{release}

%description -n dlt-tools
%{summary}.

%package -n dlt-examples
Summary:        DLT - Diagnostic Log and Trace: Examples
Requires:       %{name} = %{version}-%{release}

%description -n dlt-examples
%{summary}.

%prep
%setup -q
%patch0 -p1

%build
mkdir -p build
%cmake  -Wno-dev \
        -DDLT_USER=dlt-daemon \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DWITH_DLT_USE_IPv6=OFF \
        -DDLT_IPC=UNIX_SOCKET \
        -DWITH_MAN=ON \
        -DWITH_SYSTEMD=ON \
        -DWITH_SYSTEMD_WATCHDOG=ON \
        -DWITH_SYSTEMD_JOURNAL=ON \
        -DWITH_DLT_ADAPTOR=ON \
        -DWITH_DLT_SYSTEM=ON \
        -DDLT_USER_IPC_PATH=/run/dlt
%cmake_build

%install
mkdir -p %{buildroot}%{_bindir}
%cmake_install

# Home directory for the 'dlt-daemon' user
mkdir -p %{buildroot}%{_localstatedir}/lib/dlt-daemon

%pre
## This creates the users that are needed for /var/lib/dlt-daemon
getent group dlt-daemon >/dev/null || groupadd -r dlt-daemon
getent passwd dlt-daemon >/dev/null || \
    useradd -r -g dlt-daemon -d %{_localstatedir}/lib/dlt-daemon -s /sbin/nologin \
    -c "User for dlt-daemon" dlt-daemon
%service_add_pre dlt.service
exit 0

%post
%service_add_post dlt.service

%preun
%service_del_preun dlt.service

%postun
%service_del_postun dlt.service

%pre -n dlt-examples
%service_add_pre dlt-example-user.service

%post -n dlt-examples
%service_add_post dlt-example-user.service

%preun -n dlt-examples
%service_del_preun dlt-example-user.service

%postun -n dlt-examples
%service_del_postun dlt-example-user.service

%pre -n dlt-tools
%service_add_pre  dlt-adaptor-udp.service dlt-receive.service
%service_add_pre dlt-system.service

%post -n dlt-tools
%service_add_post dlt-adaptor-udp.service dlt-receive.service
%service_add_post dlt-system.service

%preun -n dlt-tools
%service_del_preun dlt-adaptor-udp.service dlt-receive.service
%service_del_preun dlt-system.service

%postun -n dlt-tools
%service_del_postun dlt-adaptor-udp.service dlt-receive.service
%service_del_postun dlt-system.service

%ldconfig_scriptlets -n dlt-libs

%files
%license LICENSE
%doc AUTHORS README.md ReleaseNotes.md
%attr(755,dlt-daemon,dlt-daemon) %dir %{_localstatedir}/lib/dlt-daemon
%config(noreplace) %{_sysconfdir}/dlt.conf
%config(noreplace) %{_sysconfdir}/dlt_gateway.conf
%{_unitdir}/dlt.service
%attr(0755,root,root)
%{_bindir}/dlt-daemon
%{_mandir}/man1/dlt-daemon.1%{?ext_man}
%{_mandir}/man5/dlt.conf.5%{?ext_man}
%{_mandir}/man5/dlt_gateway.conf.5%{?ext_man}

%files -n dlt-examples
# The binaries do not have man pages but do have markdown documents.
%doc doc/dlt-qnx-system.md doc/dlt_build_options.md doc/dlt_cdh.md doc/dlt_demo_setup.md doc/dlt_design_specification.md doc/dlt_example_user.md doc/dlt_extended_network_trace.md doc/dlt_filetransfer.md doc/dlt_for_developers.md doc/dlt_glossary.md doc/dlt_kpi.md doc/dlt_multinode.md doc/dlt_offline_logstorage.md
%{_bindir}/dlt-example-*
%{_bindir}/dlt-test-*
%{_datadir}/dlt-filetransfer
%{_unitdir}/dlt-example-user.service

%files -n dlt-tools
%{_bindir}/dlt-adaptor-stdin
%{_bindir}/dlt-adaptor-udp
%{_bindir}/dlt-control
%{_bindir}/dlt-convert
%{_bindir}/dlt-logstorage-ctrl
%{_bindir}/dlt-passive-node-ctrl
%{_bindir}/dlt-receive
%{_bindir}/dlt-sortbytimestamp
%{_bindir}/dlt-system
%config(noreplace) %{_sysconfdir}/dlt-system.conf
%{_unitdir}/dlt-adaptor-udp.service
%{_unitdir}/dlt-receive.service
%{_unitdir}/dlt-system.service
%{_mandir}/man1/dlt-adaptor-stdin.1%{?ext_man}
%{_mandir}/man1/dlt-adaptor-udp.1%{?ext_man}
%{_mandir}/man1/dlt-control.1%{?ext_man}
%{_mandir}/man1/dlt-convert.1%{?ext_man}
%{_mandir}/man1/dlt-logstorage-ctrl.1%{?ext_man}
%{_mandir}/man1/dlt-passive-node-ctrl.1%{?ext_man}
%{_mandir}/man1/dlt-receive.1%{?ext_man}
%{_mandir}/man1/dlt-sortbytimestamp.1%{?ext_man}
%{_mandir}/man1/dlt-system.1%{?ext_man}
%{_mandir}/man5/dlt-system.conf.5%{?ext_man}

%files -n dlt-libs
%{_libdir}/libdlt.so.*

%files -n dlt-libs-devel
%{_includedir}/dlt
%{_libdir}/pkgconfig/automotive-dlt.pc
%{_libdir}/libdlt.so
%{_libdir}/cmake/automotive-dlt

%changelog
