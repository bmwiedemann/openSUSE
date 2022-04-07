#
# spec file for package libmnl
#
# Copyright (c) 2022 SUSE LLC
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


%define lname	%{name}0
Name:           libmnl
Version:        1.0.5
Release:        0
Summary:        Minimalistic Netlink communication library
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/libmnl/
#Git-Clone:	git://git.netfilter.org/libmnl
Source:         https://www.netfilter.org/projects/libmnl/files/libmnl-%version.tar.bz2
Source2:        https://www.netfilter.org/projects/libmnl/files/libmnl-%version.tar.bz2.sig
Source3:        %name.keyring
Source9:        baselibs.conf
BuildRequires:  libtool
BuildRequires:  pkgconfig >= 0.21

%description
libmnl is a minimalistic user-space library oriented to Netlink
developers. There are a lot of common tasks in parsing, validating,
constructing of both the Netlink header and TLVs that are repetitive
and easy to get wrong. This library aims to provide simple helpers
that allows you to re-use code and to avoid re-inventing the wheel.

%package -n %lname
Summary:        Minimalistic Netlink communication library
Group:          System/Libraries

%description -n %lname
libmnl is a minimalistic user-space library oriented to Netlink
developers. There are a lot of common tasks in parsing, validating,
constructing of both the Netlink header and TLVs that are repetitive
and easy to get wrong. This library aims to provide simple helpers
that allows you to re-use code and to avoid re-inventing the wheel.

%package devel
Summary:        Development files for libmnl
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libmnl is a minimalistic user-space library oriented to Netlink
developers. There are a lot of common tasks in parsing, validating,
constructing of both the Netlink header and TLVs that are repetitive
and easy to get wrong. This library aims to provide simple helpers
that allows you to re-use code and to avoid re-inventing the wheel.

%prep
%setup -q

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --includedir="%_includedir/%name"
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/libmnl.so.*

%files devel
%license COPYING
%doc README
%_includedir/%name/
%_libdir/libmnl.so
%_libdir/pkgconfig/libmnl.pc

%changelog
