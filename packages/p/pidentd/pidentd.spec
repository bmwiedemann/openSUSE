#
# spec file for package pidentd
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


Name:           pidentd
Version:        3.0.19
Release:        0
Summary:        An Implementation of the RFC1413 Identification Server
License:        SUSE-Public-Domain
Group:          Productivity/Networking/System
URL:            https://github.com/ptrrkssn/pidentd
Source:         https://github.com/ptrrkssn/pidentd/archive/v%{version}.tar.gz
Source1:        pidentd.service
Patch0:         pidentd-destdir.patch
Patch1:         01-legacy.patch
Patch2:         pidentd-rpmlint-gcc-checks.patch
Patch3:         pidentd-no-date.patch
Patch4:         reproducible.patch
Patch5:         pidentd-ipv6.patch
BuildRequires:  autoconf
BuildRequires:  libtool

%description
This package contains identd, which implements a RFC1413 identification
server.  Identd looks up specific TCP/IP connections and returns the
user name and other information about the connection.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5

%build
autoconf
export CFLAGS="%{optflags} -DHAVE_IPV6"
%configure
%make_build

%install
%make_install
install -D -m 0644 etc/identd.conf %{buildroot}%{_sysconfdir}/identd.conf
ln -s identd %{buildroot}%{_sbindir}/in.identd
echo ".so man8/identd.8" > %{buildroot}%{_mandir}/man8/in.identd.8

ln -s service %{buildroot}%{_sbindir}/rcidentd
install -D -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/identd.service

mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/pidentd.conf <<EOF
d /run/identd 0755 root root - -
EOF

%pre
%service_add_pre identd.service

%post
%tmpfiles_create %{_tmpfilesdir}/pidentd.conf
%service_add_post identd.service

%preun
%service_del_preun identd.service

%postun
%service_del_postun identd.service

%files
%config %{_sysconfdir}/identd.conf
%doc ChangeLog* FAQ README
%{_tmpfilesdir}/pidentd.conf
%{_unitdir}/identd.service
%{_mandir}/man?/*
%{_sbindir}/*

%changelog
