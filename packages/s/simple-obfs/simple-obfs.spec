#
# spec file for package simple-obfs
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


Name:           simple-obfs
Version:        0.0.5
Release:        0
Summary:        A simple obfusacting tool
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Proxy
URL:            https://github.com/shadowsocks/simple-obfs
Source0:        https://github.com/shadowsocks/simple-obfs/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/shadowsocks/libcork/archive/f02984545061c924808e4b9ea7cc6749a41f1979/libcork-f029845.tar.gz
Patch1:         simple-obfs-asciidoc-fix.patch
BuildRequires:  asciidoc
BuildRequires:  gcc8
BuildRequires:  gcc8-c++
BuildRequires:  libtool
BuildRequires:  mbedtls-devel
BuildRequires:  pkgconfig
BuildRequires:  udns-devel
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libev)
BuildRequires:  pkgconfig(libsodium) >= 1.0.4
BuildRequires:  pkgconfig(openssl)

%description
Simple-obfs is a simple obfusacting tool, designed as plugin server of shadowsocks.

%package doc
Summary:        Documents for simple-obfs
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
Simple-obfs is a simple obfusacting tool, designed as plugin server of shadowsocks.

This package provides Documents for it.

%prep
%setup -a1 -q
%patch1 -p1

%build
rmdir libcork
mv libcork-f02984545061c924808e4b9ea7cc6749a41f1979 libcork
export CC=gcc-8
export CXX=g++-8
autoreconf -fiv
%configure
make %{?_smp_mflags} V=1

%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.{a,la}

%files
%license COPYING
%doc Changes README.md AUTHORS
%{_mandir}/man1/obfs-*.1%{?ext_man}
%{_bindir}/obfs-local
%{_bindir}/obfs-server

%files doc
%dir %{_datadir}/doc/%{name}
%doc %{_datadir}/doc/%{name}/*.html

%changelog
