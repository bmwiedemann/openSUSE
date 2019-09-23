#
# spec file for package argus-client
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define name2 argus-clients
Name:           argus-client
Version:        3.0.8.2
Release:        0
Summary:        Client for Network Monitoring Tool
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
Url:            http://www.qosient.com/argus/
Source:         http://qosient.com/argus/src/%{name2}-%{version}.tar.gz
Patch1:         %{name2}-3.0.6-overflow.patch
Patch2:         %{name2}-3.0.8-fclose.patch
Patch3:         argus-client-fix-build.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
BuildRequires:  tcpd-devel
BuildRequires:  pkgconfig(libtirpc)
Requires:       argus

%description
Client for Argus network monitoring tool.

%prep
%setup -q -n %{name2}-%{version}
%patch1
%patch2
%patch3 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

%install
install -d -m 755 %{buildroot}/{etc,usr/{bin,share/man}}
install -m 700 bin/arg* %{buildroot}%{_bindir}/
rm -f %{buildroot}%{_bindir}/argus_linux
install -m 755 bin/ra* %{buildroot}%{_bindir}/
( cd man
  cp -a man* %{buildroot}%{_mandir}
  chmod a-x %{buildroot}%{_mandir}/*/* )
rm -f %{buildroot}%{_mandir}/man1/tcpdump.1*
install -m 600 support/Config/rarc %{buildroot}%{_sysconfdir}/ra.conf
find support -type f -exec chmod 0644 {} \;
rm -f %{buildroot}%{_bindir}/argus*
rm -rf %{buildroot}%{_mandir}/man*/._*

%files
%license COPYING
%doc MANIFEST support
%{_mandir}/man*/*
%config %{_sysconfdir}/ra.conf
%{_bindir}/ra*

%changelog
