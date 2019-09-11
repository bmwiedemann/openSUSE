#
# spec file for package netcat-openbsd
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           netcat-openbsd
Version:        1.195
Release:        0
Summary:        TCP/IP swiss army knife
License:        BSD-3-Clause
Group:          Productivity/Networking/Other
URL:            http://www.openbsd.org/cgi-bin/cvsweb/src/usr.bin/nc/
Source0:        http://http.debian.net/debian/pool/main/n/netcat-openbsd/netcat-openbsd_%{version}.orig.tar.gz
#Patches from: http://http.debian.net/debian/pool/main/n/netcat-openbsd/netcat-openbsd_%{version}-1.debian.tar.xz
Patch0:         port-to-linux-with-libsd.patch
Patch1:         build-without-TLS-support.patch
Patch2:         connect-timeout.patch
Patch3:         get-sev-by-name.patch
Patch4:         send-crlf.patch
Patch5:         quit-timer.patch
Patch6:         udp-scan-timeout.patch
Patch7:         verbose-numeric-port.patch
Patch8:         dccp-support.patch
Patch9:         broadcast-support.patch
Patch10:        serialized-handling-multiple-clients.patch
Patch11:        set-TCP-MD5SIG-correctly-for-client-connections.patch
Patch12:        destination-port-list.patch
Patch13:        use-flags-to-specify-listen-address.patch
Patch14:        misc-failures-and-features.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbsd)
Provides:       nc6 = %{version}
Provides:       netcat = %{version}
Obsoletes:      nc6 <= 1.0
Obsoletes:      netcat <= 1.10

%description
A simple Unix utility which reads and writes data across network
connections using TCP or UDP protocol. It is designed to be a reliable
"back-end" tool that can be used directly or easily driven by other
programs and scripts. At the same time it is a feature-rich network
debugging and exploration tool, since it can create almost any kind of
connection you would need and has several interesting built-in
capabilities.

This package contains the OpenBSD rewrite of netcat, including support
for IPv6, proxies, and Unix sockets.

%prep
%setup -q
%autopatch -p1

%build
make %{?_smp_mflags} \
  CFLAGS="%{optflags}"

%install
install -D -m0755 nc %{buildroot}%{_bindir}/nc
install -D -m0644 nc.1 %{buildroot}/%{_mandir}/man1/nc.1
ln -s -f %{_bindir}/nc %{buildroot}/%{_bindir}/netcat
ln -s -f nc.1%{ext_man} %{buildroot}/%{_mandir}/man1/netcat.1%{ext_man}

%files
%{_bindir}/nc
%{_bindir}/netcat
%{_mandir}/man1/nc.1%{?ext_man}
%{_mandir}/man1/netcat.1%{?ext_man}

%changelog
