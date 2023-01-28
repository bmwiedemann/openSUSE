#
# spec file for package fityk
#
# Copyright (c) 2023 SUSE LLC
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


%define somajor 4
Name:           fityk
Version:        1.3.2
Release:        0
Summary:        Non-linear curve fitting and data analysis
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://fityk.nieto.pl/
Source:         https://github.com/wojdyr/fityk/releases/download/v%{version}/fityk-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM fityk-drop-dynamic-exceptions.patch gh#wojdyr/fityk#38 badshah400@gmail.com -- Drop dynamic exceptions to build with c++17 std; patch taken from upstream merge request
Patch1:         fityk-drop-dynamic-exceptions.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libtool
BuildRequires:  lua-devel >= 5.1
BuildRequires:  nlopt-devel
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  wxGTK3-devel >= 3
BuildRequires:  xylib-devel >= 1.0
BuildRequires:  zlib-devel

%description
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.

%package -n     lib%{name}%{somajor}
Summary:        Library for non-linear curve fitting and data analysis
Group:          System/Libraries

%description -n lib%{name}%{somajor}
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.

%package     -n cfityk
Summary:        Non-linear curve fitting and data analysis, command line interface
Group:          Productivity/Scientific/Math
Recommends:     gnuplot

%description -n cfityk
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.

This package contains command line interface for Fityk.

%package        devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{somajor} = %{version}

%description    devel
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.

This package contains libraries and header files for developing
applications that use Fityk library.

%package     -n python3-fityk
Summary:        Python bindings to Fityk library
Group:          Development/Libraries/Python

%description -n python3-fityk
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.

This package contains python bindings to Fityk library.

%prep
%autosetup -p1

%build
export PYTHON=%{_bindir}/python3
%configure \
    --enable-nlopt \
    --enable-python

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{python3_sitearch}
%fdupes %{buildroot}%{python3_sitelib}

%post   -n lib%{name}%{somajor} -p /sbin/ldconfig
%postun -n lib%{name}%{somajor} -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md TODO
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/samples
%{_bindir}/fityk
%{_datadir}/%{name}/html/
%{_datadir}/%{name}/samples/README
%{_datadir}/%{name}/samples/*.dat
%{_datadir}/%{name}/samples/*.fit
%{_datadir}/%{name}/samples/hello.lua
%{_datadir}/icons/hicolor/*/apps/fityk.*
%{_datadir}/applications/*.desktop
%{_datadir}/appdata/fityk.appdata.xml
%{_mandir}/man1/%{name}.*
%{_datadir}/mime/packages/*

%files -n lib%{name}%{somajor}
%{_libdir}/lib%{name}.so.%{somajor}*

%files -n cfityk
%{_bindir}/cfityk

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_datadir}/%{name}/samples/hello.c
%{_datadir}/%{name}/samples/hello.cc
# just as curiosity samples in other languages
%{_datadir}/%{name}/samples/hello.java
%{_datadir}/%{name}/samples/hello.pl
%{_datadir}/%{name}/samples/hello.rb
# -> fityk-python
%{_datadir}/%{name}/samples/*.py*

%files -n python3-fityk
%{python3_sitearch}/*
%{python3_sitelib}/*

%changelog
