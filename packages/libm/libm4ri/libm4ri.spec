#
# spec file for package libm4ri
#
# Copyright (c) 2025 SUSE LLC
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


Name:           libm4ri
Version:        20250128
%define lname	libm4ri1
Release:        0
Summary:        Library for linear arithmetic over GF(2)
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://github.com/malb/m4ri
Source:         https://github.com/malb/m4ri/releases/download/%version/m4ri-%version.tar.gz
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpng)

%description
M4RI is a library for arithmetic with dense matrices over the
Galois Field GF(2).

%package -n %lname
Summary:        Library for linear arithmetic over GF(2)
Group:          System/Libraries

%description -n %lname
M4RI is a library for arithmetic with dense matrices over the
Galois Field GF(2).

%package devel
Summary:        Development files for GF(2) arithmetic with libm4ri
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
M4RI is a library for arithmetic with dense matrices over the
Galois Field GF(2).

This subpackage contains libraries and header files for developing
applications that want to make use of libm4ri.

%prep
%autosetup -n m4ri-%version

%build
#
# 1. Need to disable SSE for %%ix86. Since --disable-sse2 translates to the
# absence of -msse rather than the inclusion of -mno-sse, we do not need
# to guard it with %%if(n)arch.
#
# 2. Set cache size manually, because, otherwise, it will pick whatever the
# build host had, which is dumb. 32K:128K matches AMD T-Bred, and is also
# fitting within Core i7-2600. Let's hope that's ok.
#
%configure --disable-static \
%ifnarch x86_64
	--disable-sse2 \
%endif
	--with-cachesize=32768:131072:131072
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%ldconfig_scriptlets -n %lname

%files -n %lname
%_libdir/libm4ri.so.*

%files devel
%_libdir/libm4ri.so
%_libdir/pkgconfig/m4ri.pc
%_includedir/m4ri/

%changelog
