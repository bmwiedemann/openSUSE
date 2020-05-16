#
# spec file for package tinyxml2
#
# Copyright (c) 2020 SUSE LLC
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


%define so_version 6
%define lib_package lib%{name}-%{so_version}
Name:           tinyxml2
Version:        6.0.0
Release:        0
Summary:        Basic XML parser in C++
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://github.com/leethomason/tinyxml2
Source:         https://github.com/leethomason/tinyxml2/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
TinyXML is a feature-bounded XML parser in C++ that can be integrated
into other programs.

TinyXML-2 does not parse or use DTDs (Document Type Definitions) or
XSLs (eXtensible Stylesheet Language). There are other parsers (with
different footprints) to do such.

%package -n     %{lib_package}
Summary:        Basic XML parser in C++
License:        Zlib
Group:          System/Libraries

%description -n %{lib_package}
TinyXML is a feature-bounded XML parser in C++ that can be integrated
into other programs.

TinyXML-2 does not parse or use DTDs (Document Type Definitions) or
XSLs (eXtensible Stylesheet Language). There are other parsers (with
different footprints) to do such.

%package        devel
Summary:        Development files for libtinyxml2
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lib_package} = %{version}

%description    devel
Contains libraries and header files for
developing applications that use libtinyxml2.

%prep
%setup -q

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
find %{buildroot} -type f -name "*.la" -delete -print
# /usr/lib/cmake is not owned by cmake; avoid any further conflicts
if [ ! -d "%{buildroot}/%{_libdir}/cmake/%{name}" ]; then
mkdir -p %{buildroot}/%{_libdir}/cmake/%{name}
mv %{buildroot}/usr/lib/cmake/tinyxml2 %{buildroot}/%{_libdir}/cmake/tinyxml2
fi

%check
make %{?_smp_mflags} test

%post -n %{lib_package} -p /sbin/ldconfig
%postun -n %{lib_package} -p /sbin/ldconfig

%files -n %{lib_package}
%defattr(-,root,root)
%doc readme.md
%{_libdir}/libtinyxml2.so.%{so_version}*

%files devel
%defattr(-,root,root)
%{_includedir}/tinyxml2.h
%{_libdir}/libtinyxml2.so
%{_libdir}/pkgconfig/tinyxml2.pc
%{_libdir}/cmake/tinyxml2

%changelog
