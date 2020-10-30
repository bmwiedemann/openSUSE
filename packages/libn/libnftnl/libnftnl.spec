#
# spec file for package libnftnl
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


Name:           libnftnl
%define lname	libnftnl11
Version:        1.1.8
Release:        0
Summary:        Userspace library to access the nftables Netlink interface
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/libnftnl/

#Git-Clone:	git://git.netfilter.org/libnftnl
Source:         http://ftp.netfilter.org/pub/libnftnl/%name-%version.tar.bz2
Source2:        http://ftp.netfilter.org/pub/libnftnl/%name-%version.tar.bz2.sig
Source9:        %name.keyring
BuildRequires:  xz
BuildRequires:  pkgconfig(libmnl) >= 1.0.3

%description
libnftnl is a userspace library providing a low-level netlink
programming interface (API) to the in-kernel nf_tables subsystem.

%package -n %lname
Summary:        Userspace library to access the nftables Netlink interface
Group:          System/Libraries

%description -n %lname
libnftnl is a userspace library providing a low-level netlink
programming interface (API) to the in-kernel nf_tables subsystem.

%package devel
Summary:        Development files for libnftnl
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libnftnl is a userspace library providing a low-level netlink
programming interface (API) to the in-kernel nf_tables subsystem.

This subpackage contains libraries and header files for developing
applications that want to make use of libnftnl.

%prep
%autosetup -p1

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --with-xml-parsing --includedir="%_includedir/%name"
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libnftnl.so.11*

%files devel
%_includedir/%name/
%_libdir/libnftnl.so
%_libdir/pkgconfig/libnftnl.pc
%license COPYING

%changelog
