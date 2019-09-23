#
# spec file for package libsass
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


%define libname libsass-3_6_1-1
Name:           libsass
Version:        3.6.1
Release:        0
Summary:        Compiler library for A CSS preprocessor language
License:        MIT
Group:          Development/Libraries/C and C++
Url:            https://github.com/sass/libsass
Source:         https://github.com/sass/libsass/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         libsass-am.diff
Patch2:         libsass-vers.diff
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Sass is a CSS pre-processor language to add new features to CSS.
LibSass is a C/C++ port of the Sass CSS precompiler.

%package -n %{libname}
Summary:        Compiler library for A CSS preprocessor language
Group:          System/Libraries

%description -n %{libname}
This package provides the shared library object for libsass.

%package devel
Summary:        Development files for libsass, a library for a CSS preprocessor language
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
This package provides development header files for libsass.

%prep
%setup -q
%patch -P 1 -P 2 -p1

%build
if [ ! -f VERSION ]; then
	echo "%{version}" >VERSION
fi
autoreconf -fi
%configure --disable-static
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/libsass*.so.*

%files devel
%{_includedir}/sass*
%{_libdir}/pkgconfig/libsass.pc
%{_libdir}/libsass*.so

%changelog
