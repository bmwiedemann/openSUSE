#
# spec file for package inih
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020 Matthias Bach <marix@marix.org>
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


Name:           inih
Version:        58
Release:        0
Summary:        Simple .INI file parser in C, good for embedded systems
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://github.com/benhoyt/inih
Source:         https://github.com/benhoyt/inih/archive/r%{version}.tar.gz#/inih-r%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig

%description
INI Not Invented Here is a simple parser for .INI files written in C and mostly
compatible with Python's ConfigParser.

%package -n libinih0
Summary:        INIH dynamic libary files
Group:          System/Libraries

%description -n libinih0
INI Not Invented Here is a simple parser for .INI files written in C and mostly
compatible with Python's ConfigParser.

This package provides the library for use at runtime by applications using INIH.

%package -n libinih-devel
Summary:        Development files for INIH
Group:          Development/Libraries/C and C++
Requires:       libinih0 = %{version}

%description -n libinih-devel
INI Not Invented Here is a simple parser for .INI files written in C and mostly
compatible with Python's ConfigParser.

This package provides the development headers for INIH including the C++ bindings.

%prep
%setup -q -n %{name}-r%{version}

%build
%meson -Ddefault_library=shared -Ddistro_install=true -Dwith_INIReader=true
%meson_build

%check
cd tests
bash -e ./unittest.sh
cd ../examples
bash -e cpptest.sh

%install
%meson_install

%post -n libinih0 -p /sbin/ldconfig
%postun -n libinih0 -p /sbin/ldconfig

%files -n libinih0
%{_libdir}/libinih.so.*
%{_libdir}/libINIReader.so.*
%license LICENSE.txt

%files -n libinih-devel
%{_includedir}/ini.h
%{_includedir}/INIReader.h
%{_libdir}/libinih.so
%{_libdir}/libINIReader.so
%{_libdir}/pkgconfig/inih.pc
%{_libdir}/pkgconfig/INIReader.pc
%doc README.md
%license LICENSE.txt

%changelog
