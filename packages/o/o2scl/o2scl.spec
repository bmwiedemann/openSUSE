#
# spec file for package o2scl
#
# Copyright (c) 2025 SUSE LLC
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
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
# Python binding tests do not work in the chroot env
%bcond_with python3
%else
%bcond_with test
%bcond_without python3
%define psuffix %{nil}
%endif
%define pname o2scl
%define shlib lib%{pname}0
Name:           %{pname}%{?psuffix}
Version:        0.930
Release:        0
Summary:        Object-oriented Scientific Computing Library
License:        GPL-3.0-only
Group:          Productivity/Scientific/Math
URL:            https://awsteiner.org/code/o2scl
Source0:        https://github.com/awsteiner/o2scl/releases/download/v%{version}/%{pname}-%{version}.tar.gz
Source1:        %{pname}.rpmlintrc
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
# Required For Patch0
BuildRequires:  libtool
BuildRequires:  libboost_headers-devel >= 1.80
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(armadillo)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(ncurses)
%if %{with test}
BuildRequires:  %{pname}-devel = %{version}
%endif
%if %{with python3}
BuildRequires:  python3-devel
BuildRequires:  python3-numpy-devel
BuildRequires:  readline-devel
%endif
Recommends:     %{pname}-doc = %{version}

%description
O2scl is a C++ library for object-oriented numerical programming. It
includes interpolation, differentiation, integration, roots of
polynomials, equation solving, minimization, constrained minimization,
Monte Carlo integration, simulated annealing, least-squares fitting,
solution of ordinary differential equations, two-dimensional
interpolation, Chebyshev approximation, unit conversions, and file I/O
with HDF5.

%package -n %{shlib}
Summary:        Shared libraries for O2scl, a scientific computation library
Group:          System/Libraries

%description -n %{shlib}
O2scl is a C++ library for object-oriented numerical programming.

This package provides the shared libraries for %{name}.

%package -n %{pname}-devel
Summary:        Source and header files for O2scl
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}
Requires:       armadillo-devel
Requires:       cblas-devel
Requires:       eigen3-devel
Requires:       gcc-c++
Requires:       hdf5-devel
Requires:       readline-devel
Requires:       pkgconfig(fftw3)
Requires:       pkgconfig(gsl)
Requires:       pkgconfig(mpfr)

%description -n %{pname}-devel
O2scl is a C++ library for object-oriented numerical programming.

This package provides the source and header files for writing software
using %{name}.

%package -n %{pname}-doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description -n %{pname}-doc
O2scl is a C++ library for object-oriented numerical programming.
This package provides the documentation for %{name}.

%prep
%autosetup -p1 -n %{pname}-%{version}
cp %{SOURCE1} doc/o2scl/
sed -Ei "s/\r$/\n/g" doc/o2scl/html/_static/evan.eml

%build
autoreconf -fvi
%limit_build -m 2500
# *_OPENSUSE_* flags disable some tolerance related tests as recommended upstream: https://github.com/awsteiner/o2scl/issues/37
export CXXFLAGS+="-DO2SCL_PLAIN_HDF5_HEADER%{?with_test: -DO2SCL_OPENSUSE -DO2SCL_OPENSUSE_I386}%{?with_python3: `numpy-config --cflags`}"
# Leap 15.X has hdf5 1.10.X
%if 0%{?suse_version} < 1650
export CXXFLAGS+=" -DO2SCL_HDF5_PRE_1_12"
%endif
# Needed to avoid "undefined symbol: GOMP_critical_name_end" when using o2sclpy from python
# https://github.com/awsteiner/o2scl/issues/40
export LDFLAGS+="-lgomp"
%configure                           \
  --enable-armadillo                 \
  --enable-eigen                     \
  --enable-fftw                      \
  --enable-openmp                    \
  --enable-ncurses                   \
  --disable-pugixml                   \
  %{?with_python3:--enable-python}   \
  %{!?with_python3:--disable-python} \
  %{nil}

%make_build

%install
%if %{without test}
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/o2scl/* %{buildroot}%{_docdir}/%{name}/

# REMOVE BOGUS DUPLICATD DOC
rm -fr %{buildroot}%{_prefix}/search

# Remove Makefile junk
find %{buildroot}%{_docdir}/%{name}/ -name "Makefile.*" -delete -print

# Remove static libs and libtool archives
find %{buildroot}%{_libdir} "(" -name "*.a" -o -name "*.la" ")" -delete -print

%fdupes %{buildroot}%{_docdir}/%{name}/
%fdupes %{buildroot}%{_datadir}/%{name}/

%ldconfig_scriptlets -n %{shlib}

%files -n %{shlib}
%{_libdir}/*.so.*

%files -n %{pname}-devel
%doc AUTHORS ChangeLog README NEWS
%license COPYING
%{_bindir}/acol
%{_bindir}/ame_parse
%{_bindir}/nucleus
%{_bindir}/yanic
%{_datadir}/%{name}/
%{_libdir}/*.so
%{_includedir}/o2scl/

%files -n %{pname}-doc
%doc %{_docdir}/%{name}/

%else

%check
%make_build check

%endif

%changelog
