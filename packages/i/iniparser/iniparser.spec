#
# spec file for package iniparser
#
# Copyright (c) 2024 SUSE LLC
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


# if bumping this, also update baselibs.conf
%define sonum 4
%define unity_version 2.6.1
Name:           iniparser
Version:        4.2.6
Release:        0
Summary:        Library to parse ini files
License:        MIT
Group:          System/Libraries
URL:            https://gitlab.com/iniparser/iniparser
Source:         https://gitlab.com/iniparser/iniparser/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        https://github.com/ThrowTheSwitch/Unity/archive/refs/tags/v%{unity_version}.tar.gz#/unity-%{unity_version}.tar.gz
Source3:        baselibs.conf
# PATCH-FIX-UPSTREAM - https://gitlab.com/iniparser/iniparser/-/merge_requests/171
Patch:          fix-tests.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# Test requires
BuildRequires:  ruby

%description
Libiniparser offers parsing of ini files from the C level.

%define libiniparser_name libiniparser%{sonum}

%package -n %{libiniparser_name}
Summary:        Library to parse ini files
Group:          System/Libraries

%description -n %{libiniparser_name}
Libiniparser offers parsing of ini files from the C level.

This package includes the libiniparser%{sonum} library.

%package -n libiniparser-devel
Summary:        Libraries and Header Files to Develop Programs with libiniparser Support
Group:          Development/Libraries/C and C++
Requires:       %{libiniparser_name} = %{version}

%description -n libiniparser-devel
This package contains the static libraries and header files needed to
develop programs which make use of the libiniparser programming
interface.

The libiniparser offers parsing of ini files from the C level.	See a
complete documentation in HTML format, from the
%{_docdir}/libiniparser-devel directory open the file
html/index.html with any HTML-capable browser.

Libraries and Header Files to Develop Programs with iniparser Support.

%prep
%autosetup -p1 -b2 -n %{name}-v%{version}

%build
%cmake \
	-DBUILD_STATIC_LIBS:BOOL=OFF \
	-DBUILD_DOCS:BOOL=ON \
	-DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/libiniparser-devel \
	-DBUILD_TESTING:BOOL=ON \
	-DFETCHCONTENT_SOURCE_DIR_UNITY:PATH=%{_builddir}/Unity-%{unity_version}
%cmake_build

%install
%cmake_install

%check
%ctest

%post -n %{libiniparser_name} -p /sbin/ldconfig
%postun -n %{libiniparser_name} -p /sbin/ldconfig

%files -n %{libiniparser_name}
%{_libdir}/*.so.*

%files -n libiniparser-devel
%doc html/
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%{_libdir}/cmake/unity
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_includedir}/unity
%exclude %{_libdir}/*.a

%changelog
