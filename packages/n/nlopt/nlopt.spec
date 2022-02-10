#
# spec file for package nlopt
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == ""
%bcond_with    bindings
%endif
%if "%{flavor}" == "bindings"
%bcond_without bindings
%define psuffix -bindings
%endif
%define pname nlopt

Name:           nlopt%{?psuffix}
Version:        2.7.1
Release:        0
Summary:        A library for nonlinear optimization
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://nlopt.readthedocs.io/en/latest/
Source0:        https://github.com/stevengj/nlopt/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
%if %{with bindings}
BuildRequires:  python3-numpy-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(octave)
%endif

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package     -n lib%{pname}0
Summary:        A library for nonlinear optimization
Group:          System/Libraries

%description -n lib%{pname}0
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package        devel
Summary:        Development files for %{pname}
Group:          Development/Libraries/C and C++
Requires:       lib%{pname}0 = %{version}

%description    devel
The %{pname}-devel package contains libraries and header files for
developing applications that use NLopt.

%package     -n python3-%{pname}
Summary:        Python interface to nonlinear optimization libray
Group:          Development/Libraries/Python
Requires:       python3-numpy
Provides:       python-%{pname} = %{version}-%{release}
Obsoletes:      python-%{pname} < %{version}-%{release}


%description -n python3-%{pname}
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

This package contains the Python3 interface for NLopt.

%package     -n octave-nlopt_optimize
Summary:        Octave interface to nonlinear optimization libray
Group:          Productivity/Scientific/Math
%requires_eq    octave-cli

%description -n octave-nlopt_optimize
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

This package contains the Octave interface for NLopt.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%cmake \
   -DCMAKE_SKIP_RPATH:BOOL=OFF \
   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
   -DNLOPT_MATLAB=OFF \
   -DNLOPT_CXX:BOOL=ON \
   -DNLOPT_TESTS:BOOL=ON \
   %{!?with_bindings:-DNLOPT_PYTHON:BOOL=OFF} \
   %{!?with_bindings:-DNLOPT_OCTAVE:BOOL=OFF} \
   %{!?with_bindings:-DNLOPT_SWIG:BOOL=OFF} \
   %{nil}
%cmake_build

%install
%cmake_install
%if %{with bindings}
# remove files from the main package
for e in %{_includedir} %{_libdir}/lib\* %{_libdir}/pkgconfig %{_libdir}/cmake %{_mandir} ; do
    rm -R %{buildroot}/${e}
done
%fdupes %{buildroot}%{pyton3_sitearch}
%endif

%check
%ctest

%post -n lib%{pname}0 -p /sbin/ldconfig
%postun -n lib%{pname}0 -p /sbin/ldconfig

%if "%{flavor}" == ""
%files -n lib%{pname}0
%{_libdir}/*.so.*

%files devel
%license COPYING
%doc AUTHORS NEWS.md README.md TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{pname}.pc
%{_libdir}/cmake/%{pname}/
%{_mandir}/man3/*.3%{?ext_man}
%endif

%if %{with bindings}
%files -n python3-%{pname}
%license COPYING
%{python3_sitearch}/*

%files -n octave-nlopt_optimize
%license COPYING
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%{_datadir}/octave/*/site/m/*
%endif

%changelog
