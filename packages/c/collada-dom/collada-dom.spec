#
# spec file for package collada-dom
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define libname libcollada-dom2_5-dp0
Name:           collada-dom
Version:        2.5.1+git20200104.c1e20b7
Release:        0
Summary:        COLLADA Document Object Model (DOM) C++ Library
License:        MIT
URL:            https://github.com/rdiankov/collada-dom
Source:         %{name}-%{version}.tar.gz
Patch0:         silence-warnings.patch
Patch1:         boost.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  libboost_filesystem-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(uriparser)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(zlib)

%description
The COLLADA Document Object Model (DOM) is an application programming
interface (API) that provides a C++ object representation of a COLLADA XML
instance document.

%package -n %{libname}
Summary:        The COLLADA Document Object Model (DOM) runtime C++ Library
Group:          System/Libraries

%description -n %{libname}
The COLLADA Document Object Model (DOM) runtime C++ Library

The COLLADA Document Object Model (DOM) is an application programming
interface (API) that provides a C++ object representation of a COLLADA XML
instance document.

%package devel
Summary:        The COLLADA Document Object Model (DOM) runtime C++ Library Development files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
The COLLADA Document Object Model (DOM) runtime C++ Library Development files

The COLLADA Document Object Model (DOM) is an application programming
interface (API) that provides a C++ object representation of a COLLADA XML
instance document.

%prep
%autosetup -p1
# fix compilation with boost 1.85 due to deprecated stuff that was removed
sed -i 's/convenience/operations/' dom/include/dae.h dom/src/dae/daeUtils.cpp
sed -i 's/branch_path/parent_path/' dom/src/dae/daeZAEUncompressHandler.cpp

%build
# silence warning spam
CXXFLAGS="-Wno-overloaded-virtual"
%cmake
%make_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%license licenses/license_e.txt licenses/dom_license_e.txt
%{_libdir}/*.so.*

%files -n %{name}-devel
%license licenses/license_e.txt licenses/dom_license_e.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}*.pc
%{_libdir}/cmake/*

%changelog
