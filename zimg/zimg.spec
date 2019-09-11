#
# spec file for package zimg
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


%define         sover 2
Name:           zimg
Version:        2.9.2
Release:        0
Summary:        Scaling, colorspace conversion, and dithering library
License:        WTFPL
Group:          Development/Libraries/C and C++
URL:            https://github.com/sekrit-twc/zimg
Source0:        zimg-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
The "z" image library implements the commonly required image processing
basics of scaling, colorspace conversion, and depth conversion.

%package -n libzimg%{sover}
Summary:        Scaling, colorspace conversion, and dithering library
Group:          System/Libraries

%description -n libzimg%{sover}
The "z" image library implements the commonly required image processing
basics of scaling, colorspace conversion, and depth conversion.

%package devel
Summary:        Development files for libzimg%{sover}
Group:          Development/Libraries/C and C++
Requires:       libzimg%{sover} = %{version}

%description devel
The libzimg-devel package contains libraries and header files for
developing applications that use libzimg%{sover}.

%prep
%setup -q

%build
autoreconf -fiv
# do not enable tests here — they make zimg slower and the install
# rule is broken
%configure \
  %ifarch x86_64 %{ix86}
  --enable-x86simd \
  %endif
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
rm -rf %{buildroot}%{_datadir}/doc/zimg
find %{buildroot} -type f -name "*.la" -delete -print

# test suite is broken on other platforms, upstream informed
%ifarch x86_64
%check
make clean
%configure \
  %ifarch x86_64 %{ix86}
  --enable-x86simd \
  %endif
  --disable-static \
  --enable-unit-test
make %{?_smp_mflags} V=1
make %{?_smp_mflags} V=1 test/unit_test
test/unit_test
%endif

%post -n libzimg%{sover} -p /sbin/ldconfig
%postun -n libzimg%{sover} -p /sbin/ldconfig

%files -n libzimg%{sover}
%license COPYING
%doc ChangeLog README.md
%{_libdir}/libzimg.so.%{sover}*

%files devel
%doc doc/example
%{_includedir}/zimg.h
%{_includedir}/zimg++.hpp
%{_libdir}/libzimg.so
%{_libdir}/pkgconfig/zimg.pc

%changelog
