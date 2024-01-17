#
# spec file for package muparserx
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 Angelos Tzotsos <tzotsos@opensuse.org>.
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


%global flavor @BUILD_FLAVOR@%nil
%if "%flavor" == "doc"
%define psuffix -doc-src
%endif

%define libbase 4_0_12
Name:           muparserx
Version:        4.0.12
Release:        0
Summary:        A C++ Library for Parsing Expressions
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://beltoforion.de/en/muparserx/
Source:         https://github.com/beltoforion/muparserx/archive/v%version.tar.gz
BuildRequires:  fdupes
%if "%flavor" != "doc"
BuildRequires:  cmake >= 2.8.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
%else
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildArch:      noarch
%endif

%description
A C++ Library for Parsing Expressions with Strings, Complex Numbers,
Vectors, Matrices and more.

%package devel
Summary:        Development files for muParserX
Group:          Development/Languages/C and C++
Requires:       lib%name%libbase = %version

%description devel
The muparserx development files. A C++ Library for Parsing Expressions with
Strings, Complex Numbers, Vectors, Matrices and more.

%package devel-doc
Summary:        Development files for muparserx
Group:          Documentation/HTML

%description devel-doc
The API documentation for muParserX.

%package -n lib%name%libbase
Summary:        A C++ Library for Parsing Expressions
Group:          System/Libraries

%description -n lib%name%libbase
The muparserx shared library. A C++ Library for Parsing Expressions with
Strings, Complex Numbers, Vectors, Matrices and more.

%prep
%autosetup -p0
# Use SVG images:
# 1. significantly smaller than png
# 2. graphviz-core suffices
# 3. output is reproducible, instead of arch/CPU dependent via gnome/pango rasterizer
echo -e "DOT_FONTNAME = sans\nDOT_IMAGEFORMAT = svg\nSVG_INTERACTIVE = yes" >> doc/doxyfile.dox

%build
%if "%flavor" == "doc"
dos2unix sample/*
pushd doc
doxygen doxyfile.dox
popd

%else
%cmake  \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  %nil
%cmake_build
%endif

%install
%if "%flavor" != "doc"
%cmake_install
mv %buildroot%_datadir/cmake %buildroot%_libdir

%else
mkdir -p %buildroot%_docdir/%name-devel-doc
cp -r doc/html %buildroot%_docdir/%name-devel-doc/
%endif

%fdupes %buildroot/%_prefix

%post -n lib%name%libbase -p /sbin/ldconfig
%postun -n lib%name%libbase -p /sbin/ldconfig

%if "%flavor" != "doc"
%files -n lib%name%libbase
%license LICENSE
%_libdir/libmuparserx.so.*

%files devel
%doc Readme.md
%_libdir/libmuparserx.so
%_includedir/*
%_libdir/pkgconfig/%name.pc
%_libdir/cmake/%name

%else

%files devel-doc
%doc doc/html sample
%endif

%changelog
