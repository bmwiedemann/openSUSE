#
# spec file for package argus
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


Name:           argus
Version:        3.0.8.3
Release:        0
Summary:        Network Monitoring Tool
License:        BSD-3-Clause AND GPL-2.0-only AND LGPL-2.1-only AND MIT
Group:          Productivity/Networking/Diagnostic
URL:            https://openargus.org/
Source:         https://qosient.com/argus/dev/%{name}-%{version}.tar.gz
Source3:        README.SUSE
Source4:        argus_linux.8.gz
Source5:        argus.service
Patch1:         %{name}-3.0.6.1-libpcap.patch
Patch2:         harden_argus.service.patch
Patch3:         fix-configure-libwrap-dependencies.diff
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libpcap-devel
BuildRequires:  libtirpc-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcpd-devel
BuildRequires:  tcsh

%package server
Summary:        Daemon for Network Monitoring Tool
Group:          Productivity/Networking/Diagnostic
Requires:       argus
Provides:       argus:%{_sbindir}/argus
%{?systemd_ordering}

%description
Argus is a network monitoring tool.

Documentation can be found in %{_docdir}/argus.

%description server
Daemon for Argus network monitoring tool.

%prep
%setup -q -n argus-%{version}
%patch1 -p1
cp %{SOURCE3} .
cp %{SOURCE4} man/man8/
%patch2 -p1
%patch3 -p1

%build
#autoreconf -fiv
export CFLAGS="%{optflags} -fno-strict-aliasing -fcommon"
%configure --with-pic
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/etc %{buildroot}/%{_sbindir} %{buildroot}/%{_bindir} %{buildroot}/%{_mandir} %{buildroot}/%{_docdir}
install -m 700 bin/argus %{buildroot}%{_sbindir}/argus
install -m 700 bin/arg* %{buildroot}%{_bindir}/
install -D -m 0644 %{SOURCE5} %{buildroot}/%{_unitdir}/argus.service
# alread in sbin
rm -f %{buildroot}%{_bindir}/argus
rm -f %{buildroot}%{_bindir}/argus_linux
( cd man
  cp -a man* %{buildroot}%{_mandir}
  chmod a-x %{buildroot}%{_mandir}/*/* )
rm -f %{buildroot}%{_mandir}/man1/tcpdump.1*
find -type f -name ._* -exec rm -Rf {} +
install -m 600 support/Config/argus.conf %{buildroot}%{_sysconfdir}/argus.conf
install -m 755 support/Archive/argusarchive %{buildroot}%{_bindir}/
find support -type f -exec chmod 0644 {} +
#chmod a+x support/{Archive/argusarchive,Startup/argus,System/magic}
chmod a+x support/{Archive/argusarchive,Startup/argus}

%pre server
%service_add_pre argus.service

%post server
%service_add_post argus.service

%preun server
%service_del_preun argus.service

%postun server
%service_del_postun argus.service

%files
%defattr(-,root,root)
%{_bindir}/argus*

%files server
%defattr(-,root,root)
%doc doc MANIFEST README.* support
%license COPYING
%{_mandir}/man*/*
%config %{_sysconfdir}/argus.conf
%{_unitdir}/argus.service
%{_sbindir}/*

%changelog
