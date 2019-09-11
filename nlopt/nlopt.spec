#
# spec file for package nlopt
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nlopt
Version:        2.6.1
Release:        0
Summary:        A library for nonlinear optimization
License:        LGPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            http://ab-initio.mit.edu/wiki/index.php/NLopt
Source0:        https://github.com/stevengj/nlopt/archive/v%{version}.tar.gz 
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-numpy-devel
BuildRequires:  swig
BuildRequires:  pkgconfig(octave)

%description
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package     -n lib%{name}0
Summary:        A library for nonlinear optimization
Group:          System/Libraries

%description -n lib%{name}0
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}0 = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package     -n python-%{name}
Summary:        Python interface to nonlinear optimization libray
Group:          Development/Libraries/Python
Requires:       python3-numpy

%description -n python-%{name}
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

This package contains Python3 interface to NLopt library.

%package     -n octave-nlopt_optimize
Summary:        Octave interface to nonlinear optimization libray
Group:          Productivity/Scientific/Math
%requires_eq    octave-cli

%description -n octave-nlopt_optimize
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

This package contains Octave interface to NLopt library.

%prep
%autosetup -p1

%build
%cmake -DNLOPT_MATLAB=OFF
%cmake_build

%install
%cmake_install
%fdupes %{buildroot}%{py_sitedir}

%post -n lib%{name}0 -p /sbin/ldconfig
%postun -n lib%{name}0 -p /sbin/ldconfig

%files -n lib%{name}0
%{_libdir}/*.so.*

%files devel
%license COPYING
%doc AUTHORS NEWS.md README.md TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/
%{_mandir}/man3/*.3%{?ext_man}

%files -n python-%{name}
%license COPYING
%{python3_sitearch}/*

%files -n octave-nlopt_optimize
%license COPYING
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%{_datadir}/octave/*/site/m/*

%changelog
