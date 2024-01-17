#
# spec file for package tlswrap
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           tlswrap
Version:        1.04
Release:        0
Summary:        TLS/SSL FTP wrapper/proxy
License:        BSD-3-Clause
Group:          Productivity/Networking/Ftp/Clients
Url:            http://www.tlswrap.com/
Source0:        %{name}-%{version}.tar.gz
Patch0:         openssl-1_1-compat.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel

%description
TLS/SSL FTP wrapper/proxy, allowing you to use your favorite FTP client with
any TLS/SSL-enabled FTP server.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags} "CFLAGS=%{optflags}"

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%license COPYING
%doc README
%{_bindir}/tlswrap

%changelog
