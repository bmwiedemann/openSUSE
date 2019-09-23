#
# spec file for package fityk
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fityk
Version:        1.3.1
Release:        0
%define somajor 4
Summary:        Non-linear curve fitting and data analysis
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Url:            http://fityk.nieto.pl/
Source:         https://github.com/wojdyr/fityk/releases/download/v%{version}/fityk-%{version}.tar.bz2
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel >= 1.35
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnuplot
BuildRequires:  lua-devel >= 5.1
BuildRequires:  ncurses-devel
BuildRequires:  nlopt-devel
BuildRequires:  python-devel
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  wxWidgets-devel >= 3
BuildRequires:  xylib-devel >= 1.0
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%package     -n python-fityk
Summary:        Python bindings to Fityk library
Group:          Development/Libraries/Python 

%description -n python-fityk
Fityk is a program for nonlinear curve-fitting of analytical
functions (especially peak-shaped) to data (usually experimental
data). It can also be used for visualization of x-y data only.

This package contains python bindings to Fityk library.

%prep
%setup -q

%build
%configure \
    --disable-xyconvert \
    --enable-nlopt \
    --enable-python

make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}/%{_libdir}/*.la
%fdupes %{buildroot}%{py_sitedir}

%post   -n lib%{name}%{somajor} -p /sbin/ldconfig
%postun -n lib%{name}%{somajor} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING NEWS README.md TODO
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
%{_mandir}/man1/%{name}.*
# %%{_datadir}/pixmaps/*
%{_datadir}/mime/packages/*

%files -n lib%{name}%{somajor}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.%{somajor}*

%files -n cfityk
%defattr(-,root,root)
%{_bindir}/cfityk

%files devel
%defattr(-,root,root)
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

%files -n python-fityk
%defattr(-,root,root)
%{python_sitearch}/*
%{python_sitelib}/*

%changelog
