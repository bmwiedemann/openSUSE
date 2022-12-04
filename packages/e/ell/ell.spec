#
# spec file for package ell
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


%define lname   libell0
Name:           ell
Version:        0.54
Release:        0
Summary:        Wireless setup and cryptography library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://01.org/ell
#Git-Clone:     https://git.kernel.org/pub/scm/libs/ell/ell.git
Source:         https://mirrors.kernel.org/pub/linux/libs/ell/%name-%version.tar.xz
Source2:        https://mirrors.kernel.org/pub/linux/libs/ell/%name-%version.tar.sign
Source3:        %name.keyring
BuildRequires:  gcc-c++
BuildRequires:  libtool >= 2.2
BuildRequires:  pkg-config
BuildRequires:  xz

%description
The "Embedded Linux Library" implements an API for wireless
cryptography actions by using the kernel crypto API.

%package -n %lname
Summary:        Wireless setup and cryptography library
Group:          System/Libraries

%description -n %lname
The "Embedded Linux Library" implements an API for wireless
cryptography actions by using the kernel crypto API.

%package devel
Summary:        Development files for the ELL wireless setup/crypto library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The "Embedded Linux Library" implements an API for wireless
cryptography actions by using the kernel crypto API.

This subpackage contains libraries and header files for developing
applications that want to make use of ell.

%prep
%autosetup -p1

%build
# This project does not implement proper SONAMing, let alone symbol versioning.
# Force systems into lockstep updates to remedy this.
perl -i -lpe 's{^ELL_0.10}{ELL_%version}' ell/ell.sym

%configure
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%check
%make_build check || :

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%license COPYING
%_libdir/libell.so.*

%files devel
%_libdir/libell.so
%_libdir/pkgconfig/*.pc
%_includedir/ell/

%changelog
