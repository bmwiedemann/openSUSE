#
# spec file for package CCfits
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


%define sover   2_6
Name:           CCfits
Version:        2.7
Release:        0
Summary:        An object oriented interface to the cfitsio library
License:        MIT
Group:          System/Libraries
URL:            https://heasarc.gsfc.nasa.gov/docs/software/fitsio/ccfits/
Source0:        https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/ccfits/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM CCfits-cmake-install-pkgconfig.patch badshah400@gmail.com -- Configure and install pkgconfig file when building using cmake
Patch0:         CCfits-cmake-install-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cfitsio)

%description
It is designed to make the capabilities of cfitsio available to programmers
working in C++. It is written in ANSI C++ and implemented using the C++
Standard Library with namespaces, exception handling, and member template
functions.

%package -n     lib%{name}%{sover}
Summary:        An object oriented interface to the cfitsio library
Group:          System/Libraries

%description -n lib%{name}%{sover}
It is designed to make the capabilities of cfitsio available to programmers
working in C++. It is written in ANSI C++ and implemented using the C++
Standard Library with namespaces, exception handling, and member template
functions.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       pkgconfig(cfitsio)

%description    devel
An object oriented interface to the cfitsio library.

This package contains header files, and libraries needed to develop
application that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake -DTESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n lib%{name}%{sover}

%files -n lib%{name}%{sover}
%doc CHANGES
%license License*
%{_libdir}/lib%{name}.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
