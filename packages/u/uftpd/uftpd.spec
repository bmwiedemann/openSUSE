#
# spec file for package uftpd
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
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


Name:           uftpd
Version:        2.12
Release:        0
Summary:        A combined TFTP/FTP server
License:        ISC
Group:          Productivity/Networking/Ftp/Servers
URL:            http://troglobit.com/uftpd.html
#Git-Clone:     https://github.com/troglobit/uftpd.git
Source:         https://github.com/troglobit/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libite)
BuildRequires:  pkgconfig(libuev) >= 2.2.0
Conflicts:      tftp
Conflicts:      atftp
Provides:       tftp(server)

%description
uftpd serves both TFTP and FTP without any configuration file, starts
automatically from the traditional UNIX inetd super server, and is
tcpwrapped.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
rm -rf %{buildroot}/%{_datadir}/doc

%files
%doc README.md
%license LICENSE
%{_sbindir}/in.ftpd
%{_sbindir}/in.tftpd
%{_sbindir}/uftpd
%{_mandir}/man8/in.ftpd.8%{?ext_man}
%{_mandir}/man8/in.tftpd.8%{?ext_man}
%{_mandir}/man8/uftpd.8%{?ext_man}

%changelog
