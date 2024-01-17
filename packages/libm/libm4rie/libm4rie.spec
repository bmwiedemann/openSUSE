#
# spec file for package libm4rie
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


Name:           libm4rie
Version:        20200125
# Note that libm4rie is not always updated in lockstep with libm4ri,
# and that is absolutely normal.
%define lname	libm4rie-0_0_%version
Release:        0
Summary:        Library for linear arithmetic over GF(2^e)
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://bitbucket.org/malb/m4rie

#Git-Clone:	https://bitbucket.org/malb/m4rie.git
Source:         https://bitbucket.org/malb/m4rie/downloads/m4rie-%version.tar.gz
BuildRequires:  libm4ri-devel
BuildRequires:  pkg-config

%description
M4RIE is a library for arithmetic with dense matrices over the
Galois Field GF(2^e).

%package -n %lname
Summary:        Library for linear arithmetic over GF(2^e)
Group:          System/Libraries

%description -n %lname
M4RIE is a library for arithmetic with dense matrices over the
Galois Field GF(2^e).

%package devel
Summary:        Development files for GF(2^e) arithmetic with libm4rie
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
M4RIE is a library for arithmetic with dense matrices over the
Galois Field GF(2^e).

This subpackage contains libraries and header files for developing
applications that want to make use of libm4rie.

%prep
%autosetup -n m4rie-%version

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files -n %lname
%_libdir/libm4rie-0.0.%version.so

%files devel
%_libdir/libm4rie.so
%_libdir/pkgconfig/*.pc
%_includedir/m4rie/

%changelog
