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
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkg-config >= 0.21

%description
libmnl is a user-space library for parsing, validation, constructing
Netlink headers and TLVs.

%package -n %lname
Summary:        Minimalistic Netlink communication library
Group:          System/Libraries

%description -n %lname
libmnl is a user-space library for Netlink developers. There are a
lot of common tasks in parsing, validating, constructing of both the
Netlink header and TLVs that are repetitive and easy to get wrong.
This library provides helpers that allow for code reuse.

%package devel
Summary:        Headers for libmnl, a Netlink communications library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
libmnl is a user-space library for parsing, validation, constructing
Netlink headers and TLVs. This subpackage has the header files.

%package doc
Summary:        Documentation for libmnl, a Netlink communications library
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
libmnl is a user-space library for parsing, validation, constructing
Netlink headers and TLVs. This subpackage has the documentation.

%prep
%autosetup -p1

%build
# includedir intentional, cf. bugzilla.opensuse.org/795968
%configure --includedir="%_includedir/%name" --with-doxygen
%make_build

%check
%make_build check

%install
%make_install
find "%buildroot" -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %lname

%files -n %lname
%license COPYING
%_libdir/libmnl.so.*

%files devel
%license COPYING
%doc README
%_includedir/%name/
%_libdir/libmnl.so
%_libdir/pkgconfig/libmnl.pc

%files doc
%_mandir/man3/*.3*

%changelog
