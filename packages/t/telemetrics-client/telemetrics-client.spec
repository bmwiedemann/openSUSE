#
# spec file for package telemetrics-client
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


Name:           telemetrics-client
Version:        2.2.3+git20191008.4119bde
Release:        0
Summary:        Telemetrics solution
License:        LGPL-2.1-or-later
Group:          System/Management
URL:            https://github.com/clearlinux/telemetrics-client
Source:         %{name}-%{version}.tar.xz
Source1:        telemetrics-users.conf
Patch:          telemetrics.conf.patch
Patch1:         telemctl-enable-disable.diff
Patch2:         install-paths.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libdw)
BuildRequires:  pkgconfig(libelf)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)

%description
This package provides the front end component of a complete telemetrics
solution for Linux-based operating systems. Specifically, the front end
component includes probes that collect specific types of data, a library,
which records the probes and send them to the daemon, a daemon that handles
the communication and daemon to collect and forward everything to a central
host.

%package devel
Summary:        Include files for Telemetrics
Group:          Development/Libraries/C and C++
Requires:       %name = %version

%description devel
This package contains the include files and libraries of the telemetrics-client for development.

%prep
%setup -q
%patch -p0
%patch1 -p1
%patch2 -p1

%build
./autogen.sh
%configure --libexecdir=/usr/lib/telemetrics-probes --with-backendserveraddr=https://telemetrics-server.local/v2/collector
make %{?_smp_mflags}
mv src/probes/README.md src/probes/README-Probes.md

%install
%make_install
rm %{buildroot}%{_prefix}/lib/systemd/system/telemprobd-update-trigger.service
rm %{buildroot}%{_libdir}/libtelemetry.la
mkdir -p %{buildroot}%{_sysconfdir}/telemetrics
mkdir -p %{buildroot}%{_sysusersdir}
install -m 644 %{SOURCE1} %{buildroot}%{_sysusersdir}/

%pre
%service_add_pre telempostd.path telemprobd.socket klogscanner.service journal-probe-tail.service bert-probe.service hprobe.service journal-probe.service pstore-clean.service pstore-probe.service python-probe.service

%post
/sbin/ldconfig
%service_add_post telempostd.path telemprobd.socket klogscanner.service journal-probe-tail.service bert-probe.service hprobe.service journal-probe.service pstore-clean.service pstore-probe.service python-probe.service
%sysusers_create telemetrics-users.conf
%tmpfiles_create telemetrics-dirs.conf

%preun
%service_del_preun telempostd.path telempostd.service telemprobd.service telemprobd.socket klogscanner.service journal-probe-tail.service bert-probe.service hprobe.service journal-probe.service pstore-clean.service pstore-probe.service python-probe.service

%postun
/sbin/ldconfig
%service_del_postun telempostd.path telemprobd.socket klogscanner.service journal-probe-tail.service bert-probe.service hprobe.service journal-probe.service pstore-clean.service pstore-probe.service python-probe.service

%files
%license LICENSE.LGPL-2.1
%doc README.md src/probes/README-Probes.md
%dir %{_sysconfdir}/telemetrics
%{_bindir}/telem-record-gen
%{_sbindir}/*
%{_prefix}/lib/sysctl.d/40-crash-probe.conf
%dir %{_prefix}/lib/systemd/system.conf.d
%{_prefix}/lib/systemd/system.conf.d/40-core-ulimit.conf
%{_prefix}/lib/systemd/system/
%{_prefix}/lib/telemetrics-probes
%{_sysusersdir}/telemetrics-users.conf
%{_tmpfilesdir}/telemetrics-dirs.conf
%{_libdir}/libtelemetry.so.3*
%dir %{_datadir}/defaults
%dir %{_datadir}/defaults/telemetrics
%{_datadir}/defaults/telemetrics/telemetrics.conf
%{_mandir}/man1/*
%{_mandir}/man5/*

%files devel
%{_includedir}/telemetry.h
%{_libdir}/libtelemetry.so
%{_libdir}/pkgconfig/libtelemetry.pc
%{_mandir}/man3/*

%changelog
