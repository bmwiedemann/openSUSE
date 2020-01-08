#
# spec file for package mingw32-gmp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mingw32-gmp
Version:        6.1.1
Release:        0
Summary:        The GNU MP Library
License:        GPL-2.0+ and LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://gmplib.org/
Source:         https://gmplib.org/download/gmp/gmp-%{version}.tar.xz

#!BuildIgnore: post-build-checks
BuildRequires:  m4
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw32-cross-gcc-c++
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw32_package_header_debug
BuildArch:      noarch

%description
GMP is a free library for arbitrary precision arithmetic, operating on signed integers,
rational numbers, and floating point numbers.

%package -n mingw32-libgmp10
Summary:        The GNU MP Library
Group:          System/Libraries
Obsoletes:      mingw32-libgmp
Provides:       mingw32-libgmp

%description -n mingw32-libgmp10
GMP is a free library for arbitrary precision arithmetic, operating on signed integers,
rational numbers, and floating point numbers.

%package -n mingw32-libgmpxx4
Summary:        C++ bindings for the GNU MP Library
Group:          System/Libraries
Obsoletes:      mingw32-libgmpxx
Provides:       mingw32-libgmpxx

%description -n mingw32-libgmpxx4
GMP is a free library for arbitrary precision arithmetic, operating on signed integers,
rational numbers, and floating point numbers.  C++ bindings for the GNU MP Library.

%package devel
Summary:        Include Files and Libraries for Development with the GNU MP Library
Group:          Development/Libraries/C and C++

%description devel
These libraries are needed to develop programs which calculate with huge numbers (integer and floating point).

%_mingw32_debug_package

%prep
%setup -q -n gmp-%{version}

%build
echo "lt_cv_deplibs_check_method='pass_all'" >>%{_mingw32_cache}
%{_mingw32_configure} \
	  --enable-shared \
      --disable-static \
	  --enable-cxx

%{_mingw32_make} %{?_smp_mflags} || %{_mingw32_make}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files -n mingw32-libgmp10
%defattr(755,root,root,755)
%{_mingw32_bindir}/libgmp-10.dll

%files -n mingw32-libgmpxx4
%defattr(755,root,root,755)
%{_mingw32_bindir}/libgmpxx-4.dll

%files devel
%defattr(644,root,root,755)
%{_mingw32_libdir}/libgmp.dll.a
%{_mingw32_libdir}/libgmpxx.dll.a
%{_mingw32_includedir}/gmp.h
%{_mingw32_includedir}/gmpxx.h
%{_mingw32_infodir}
%exclude %{_mingw32_infodir}/dir*

%changelog
