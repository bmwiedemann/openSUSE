#
# spec file for package libm4ri
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libm4ri
%define date	20140914
%define lname	libm4ri-0_0_%date
Version:        0~%date
Release:        0
Summary:        Library for fast linear arithmetic over GF(2)
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Url:            https://bitbucket.org/malb/m4ri

#Git-Clone:	https://bitbucket.org/malb/m4ri.git
Source:         https://bitbucket.org/malb/m4ri/downloads/m4ri-%date.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libpng)

%description
M4RI is a library for fast arithmetic with dense matrices over the
Galois Field GF(2).

%package -n %lname
Summary:        Library for fast linear arithmetic over GF(2)
Group:          System/Libraries

%description -n %lname
M4RI is a library for fast arithmetic with dense matrices over the
Galois Field GF(2).

%package devel
Summary:        Development files for GF(2) arithmetic with libm4ri
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
M4RI is a library for fast arithmetic with dense matrices over the
Galois Field GF(2).

This subpackage contains libraries and header files for developing
applications that want to make use of libm4ri.

%prep
%setup -qn m4ri-%date

%build
#
# 1. Need to disable SSE for %%ix86. Since --disable-sse2 translates to the
# absence of -msse rather than the inclusion of -mno-sse, we do not need
# to guard it with %%if(n)arch.
#
# 2. Set cache size manually, because, otherwise, it will pick whatever the
# build host had, which is dumb. 32K:128K matches AMD T-Bred, and is also
# fitting within Core i7. Let's hope that's ok.
#
%configure --disable-static \
%ifnarch x86_64
	--disable-sse2 \
%endif
	--with-cachesize=32768:131072:131072
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%files -n %lname
%defattr(-,root,root)
%_libdir/libm4ri-0.0.%date.so

%files devel
%defattr(-,root,root)
%_libdir/libm4ri.so
%_libdir/pkgconfig/m4ri.pc
%_includedir/m4ri/

%changelog
