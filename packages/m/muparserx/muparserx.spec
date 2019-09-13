#
# spec file for package muparserx
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libbase 4_0_8
Name:           muparserx
Version:        4.0.8
Release:        0
Summary:        A C++ Library for Parsing Expressions
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            http://muparserx.beltoforion.de
Source0:        https://github.com/beltoforion/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 2.8.0
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  graphviz-gnome
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A C++ Library for Parsing Expressions with Strings, Complex Numbers,
Vectors, Matrices and more.

%package devel
Summary:        Development files for muparserx
Group:          Development/Languages/C and C++
Requires:       lib%{name}%{libbase} = %{version}

%description devel
The muparserx development files. A C++ Library for Parsing Expressions with
Strings, Complex Numbers, Vectors, Matrices and more.

%package -n lib%{name}%{libbase}
Summary:        A C++ Library for Parsing Expressions
Group:          System/Libraries

%description -n lib%{name}%{libbase}
The muparserx shared library. A C++ Library for Parsing Expressions with
Strings, Complex Numbers, Vectors, Matrices and more.

%prep
%setup -q

%build
%cmake  \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBUILD_SAMPLES:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING=Release
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install
mv %{buildroot}/usr/share/cmake %{buildroot}%{_libdir}
dos2unix License.txt Readme.txt sample/*
pushd doc
doxygen doxyfile.dox
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -r html %{buildroot}%{_docdir}/%{name}-devel/
popd

%fdupes %{buildroot}/%{_prefix}

%post -n lib%{name}%{libbase} -p /sbin/ldconfig

%postun -n lib%{name}%{libbase} -p /sbin/ldconfig

%files -n lib%{name}%{libbase}
%license License.txt
%{_libdir}/libmuparserx.so.*

%files devel
%doc Readme.txt sample html
%license License.txt
%{_libdir}/libmuparserx.so
%{_includedir}/*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}

%changelog
