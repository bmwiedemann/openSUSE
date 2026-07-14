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


%define sonum 4
%define unity_version 2.6.1
%define libname  lib%{name}%{sonum}
%define libdevel lib%{name}-devel

Name:           iniparser
Version:        4.2.6
Release:        0
Summary:        Library to parse ini files
License:        MIT
Group:          System/Libraries
URL:            https://gitlab.com/iniparser/iniparser
Source0:        https://gitlab.com/iniparser/iniparser/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/ThrowTheSwitch/Unity/archive/refs/tags/v%{unity_version}.tar.gz#/unity-%{unity_version}.tar.gz
# PATCH-FIX-UPSTREAM - https://gitlab.com/iniparser/iniparser/-/merge_requests/171
Patch0:         fix-tests.patch

BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  fdupes
# Test requires
BuildRequires:  ruby

BuildSystem:    cmake
BuildOption(prep): -b1 -n %{name}-%{version}
BuildOption(conf): -DBUILD_DOCS:BOOL=ON
BuildOption(conf): -DBUILD_TESTING:BOOL=ON
BuildOption(conf): -DBUILD_STATIC_LIBS:BOOL=OFF
BuildOption(conf): -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{libdevel}
BuildOption(conf): -DFETCHCONTENT_SOURCE_DIR_UNITY:PATH=%{_builddir}/Unity-%{unity_version}

%description
Libiniparser offers parsing of ini files from the C level.

%package -n %{libname}
Summary:        Library to parse ini files
Group:          System/Libraries

%description -n %{libname}
Libiniparser offers parsing of ini files from the C level.

%package -n %{libdevel}
Summary:        Libraries and header files to develop programs with libiniparser support
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{libdevel}
This package contains the static libraries and header files needed to develop
programs which make use of the libiniparser programming interface.

The libiniparser offers parsing of ini files from the C level. See a complete
documentation in HTML format, from the %{_docdir}/%{libdevel} directory
open the file html/index.html with any HTML-capable browser.

%install -a
%fdupes %{buildroot}%{_docdir}

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libdevel}
%doc %{_docdir}/%{libdevel}
%{_libdir}/*.so
%{_libdir}/cmake/%{name}
%{_libdir}/cmake/unity
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}
%{_includedir}/unity
%exclude %{_libdir}/*.a

%changelog
