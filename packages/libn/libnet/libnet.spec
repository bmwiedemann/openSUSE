#
# spec file for package libnet
#
# Copyright (c) 2020 SUSE LLC
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


%define libname libnet9
Name:           libnet
Version:        1.2
Release:        0
Summary:        A C Library for Portable Packet Creation
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://codedocs.xyz/libnet/libnet/
Source0:        https://github.com/libnet/libnet/releases/download/v%{version}/libnet-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  libtool

%description
Libnet is an API to help with the construction and handling of network
packets. It provides a portable framework for low-level network packet
writing and handling. Libnet includes packet creation at the IP layer
and at the link layer as well as a host of supplementary and
complementary functionality. Libnet is very useful for writing network
tools and network test code. See the man page and sample test code for
more detailed information.

%package -n %{libname}
Summary:        A C Library for Portable Packet Creation
Group:          Development/Libraries/C and C++

%description -n %{libname}
Libnet is an API to help with the construction and handling of network
packets. It provides a portable framework for low-level network packet
writing and handling. Libnet includes packet creation at the IP layer
and at the link layer as well as a host of supplementary and
complementary functionality. Libnet is very useful for writing network
tools and network test code. See the man page and sample test code for
more detailed information.

%package devel
Summary:        Devel files for libnet
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Libnet is an API to help with the construction and handling of network
packets. This package contains devel files.

%package doc
Summary:        Documentation for libnet
Group:          Development/Libraries/C and C++

%description doc
Libnet is an API to help with the construction and handling of network
packets. This package contains documentation.

%prep
%setup -q
###%patch1 -p1

rm -rf sample/win32
# HACK: to have samples/ dir untouched and ready for installation
cp -r sample sample_doc

%build
# no configure in a tarball
autoreconf -fiv
CFLAGS="%{optflags} -Wall -Wno-unused" \
%configure \
    --disable-static \
    --with-pic \
    --with-link-layer=linux
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install -d -m 755 %{buildroot}/%{_bindir}
install -m 755 libnet-config %{buildroot}/%{_bindir}

rm -rf sample/
# HACK: rename untouched dir back
mv sample_doc sample
find doc/  -name "Makefile*" -o -name ".libs" | xargs rm -rf
rm -rf %{buildroot}/usr/share/doc/%{name}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/libnet.so.*

%files devel
%{_bindir}/libnet-config
%{_includedir}/libnet*
%{_libdir}/libnet.so
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libnet.pc

%files doc
%doc doc/* sample

%changelog
