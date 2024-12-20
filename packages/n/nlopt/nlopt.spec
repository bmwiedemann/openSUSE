#
# spec file for package nlopt
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" == ""
%bcond_without bindings
%endif
%if "%{flavor}" == "main"
%bcond_with   bindings
%define psuffix -main
%endif
%define pname nlopt

Name:           nlopt%{?psuffix}
Version:        2.9.1
Release:        0
Summary:        A library for nonlinear optimization
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://nlopt.readthedocs.io/en/latest/
Source0:        https://github.com/stevengj/nlopt/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
%if %{with bindings}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  swig
BuildRequires:  pkgconfig(octave)
Requires:       python-numpy
%python_subpackages
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

%package -n     %{pname}-devel
Summary:        Development files for %{pname}
Group:          Development/Libraries/C and C++
Requires:       lib%{pname}0 = %{version}

%description -n %{pname}-devel
The %{pname}-devel package contains libraries and header files for
developing applications that use NLopt.

%if %{with bindings}
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
%endif

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
# Must be built with -D_FORTIFY_SOURCE=2 (not 3) for tests to pass, see <https://github.com/stevengj/nlopt/issues/563>
%if %{with bindings}
%{python_expand # Necessary to run configure with all python flavors
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
%cmake \
   -DCMAKE_C_FLAGS="%(echo %optflags | sed 's/-D_FORTIFY_SOURCE=3/-D_FORTIFY_SOURCE=2/g')" \
   -DCMAKE_CXX_FLAGS="%(echo %optflags | sed 's/-D_FORTIFY_SOURCE=3/-D_FORTIFY_SOURCE=2/g')" \
   -DCMAKE_SKIP_RPATH:BOOL=OFF \
   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
   -DNLOPT_MATLAB=OFF \
   -DNLOPT_CXX:BOOL=ON \
   -DNLOPT_TESTS:BOOL=ON \
   -DNLOPT_PYTHON:BOOL=ON \
   -DNLOPT_OCTAVE:BOOL=ON \
   -DNLOPT_SWIG:BOOL=ON \
   -DPython_EXECUTABLE=%{_bindir}/$python \
   %{nil}
%cmake_build
popd
}
%else
%cmake \
   -DCMAKE_C_FLAGS="%(echo %optflags | sed 's/-D_FORTIFY_SOURCE=3/-D_FORTIFY_SOURCE=2/g')" \
   -DCMAKE_CXX_FLAGS="%(echo %optflags | sed 's/-D_FORTIFY_SOURCE=3/-D_FORTIFY_SOURCE=2/g')" \
   -DCMAKE_SKIP_RPATH:BOOL=OFF \
   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
   -DNLOPT_MATLAB=OFF \
   -DNLOPT_CXX:BOOL=ON \
   -DNLOPT_TESTS:BOOL=ON \
   -DNLOPT_PYTHON:BOOL=OFF \
   -DNLOPT_OCTAVE:BOOL=OFF \
   -DNLOPT_SWIG:BOOL=OFF \
   %{nil}
%cmake_build
%endif

%install
%if %{with bindings}
%{python_expand # Necessary to run configure with all python flavors
export PYTHON=$python
pushd ../${PYTHON}_build
%cmake_install
# remove files from the main package
for e in %{_includedir} %{_libdir}/lib\* %{_libdir}/pkgconfig %{_libdir}/cmake %{_mandir} ; do
    rm -R %{buildroot}/${e}
done
%fdupes %{buildroot}%{$python_sitearch}
popd
}
%else
%cmake_install
%endif

%check
%if %{with bindings}
%{python_expand # Necessary to run configure with all python flavors
export PYTHON=$python
pushd ../${PYTHON}_build
%ctest
}
%else
%ctest
%endif

%post -n lib%{pname}0 -p /sbin/ldconfig
%postun -n lib%{pname}0 -p /sbin/ldconfig

%if "%{flavor}" == "main"
%files -n lib%{pname}0
%{_libdir}/*.so.*

%files -n %{pname}-devel
%license COPYING
%doc AUTHORS NEWS.md README.md TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{pname}.pc
%{_libdir}/cmake/%{pname}/
%{_mandir}/man3/*.3%{?ext_man}
%endif

%if %{with bindings}
%files %{python_files}
%license COPYING
%{python_sitearch}/nlopt-%{version}*.*-info/
%{python_sitearch}/nlopt.py
%{python_sitearch}/*.so

%files -n octave-nlopt_optimize
%license COPYING
%dir %{_libdir}/octave/*/site
%dir %{_libdir}/octave/*/site/oct
%dir %{_libdir}/octave/*/site/oct/*
%{_libdir}/octave/*/site/oct/*/*.oct
%{_datadir}/octave/*/site/m/*
%endif

%changelog
