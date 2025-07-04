#
# spec file for package nlopt
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

%if "%{flavor}" == ""
%bcond_without bindings
%endif
%if "%{flavor}" == "main"
%bcond_with   bindings
%define psuffix -main
%endif
%define pname nlopt
%define so_ver 1

%if 0%{?suse_version} <= 1500
%define gcc_ver 8
%endif

Name:           nlopt%{?psuffix}
Version:        2.10.0
Release:        0
Summary:        A library for nonlinear optimization
License:        LGPL-2.1-or-later
URL:            https://nlopt.readthedocs.io/en/latest/
Source0:        https://github.com/stevengj/nlopt/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM nlopt-dont-force-cxx-standard.patch gh#stevengj/nlopt#597 badshah400@gmail.com -- Do not force c++11 standard; this allows building octave bindings against octave 10+
Patch0:         nlopt-dont-force-cxx-standard.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  hdf5-devel
BuildRequires:  pkgconfig
%if %{with bindings}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  java-devel > 11
BuildRequires:  strip-nondeterminism
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

%package     -n lib%{pname}%{so_ver}
Summary:        A library for nonlinear optimization

%description -n lib%{pname}%{so_ver}
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

%package -n     %{pname}-devel
Summary:        Development files for %{pname}
Requires:       lib%{pname}%{so_ver} = %{version}

%description -n %{pname}-devel
The %{pname}-devel package contains libraries and header files for
developing applications that use NLopt.

%if %{with bindings}
%package     -n octave-nlopt_optimize
Summary:        Octave interface to nonlinear optimization library
%requires_eq    octave-cli

%description -n octave-nlopt_optimize
NLopt is a free/open-source library for nonlinear optimization,
providing a common interface for a number of different free
optimization routines available online as well as original
implementations of various other algorithms.

This package contains the Octave interface for NLopt.
%endif

%package -n %{pname}-java
Summary:        Java bindings for NLopt
BuildArch:      noarch

%description -n %{pname}-java
This package provides java bindings for NLopt, a nonlinear optimization
library.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%if 0%{?gcc_ver}
export CC=gcc-%{gcc_ver}
export CXX=g++-%{gcc_ver}
%endif

%if %{with bindings}
%{python_expand # Necessary to run configure with all python flavors
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
%cmake \
   -DCMAKE_SKIP_RPATH:BOOL=OFF \
   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
   -DNLOPT_MATLAB=OFF \
   -DNLOPT_CXX:BOOL=OM \
   -DNLOPT_TESTS:BOOL=ON \
   -DNLOPT_PYTHON:BOOL=ON \
   -DNLOPT_SWIG:BOOL=ON \
   -DPython_EXECUTABLE=%{_bindir}/$python \
%if "${python_flavor}" == "python3"  || "%{$python_provides}" == "python3"
   -DNLOPT_JAVA:BOOL=ON \
   -DNLOPT_OCTAVE:BOOL=ON \
%else
   -DNLOPT_JAVA:BOOL=OFF \
   -DNLOPT_OCTAVE:BOOL=OFF \
%endif
   %{nil}
%cmake_build
popd
}
%else
%cmake \
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
strip-all-nondeterminism %{buildroot}%{_datadir}/java/%{pname}.jar
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

%if "%{flavor}" == "main"

%ldconfig_scriptlets -n lib%{pname}%{so_ver}

%files -n lib%{pname}%{so_ver}
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

%files -n %{pname}-java
%license COPYING
%{_datadir}/java/%{pname}.jar
%endif

%changelog
