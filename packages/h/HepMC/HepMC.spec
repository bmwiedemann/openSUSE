#
# spec file for package HepMC
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


%bcond_with rootio

%define so_main 3
%define libmain libHepMC3-%{so_main}
%define so_search 4
%define libsearch libHepMC3search%{so_search}
Name:           HepMC
Version:        3.2.5
Release:        0
Summary:        An event record for High Energy Physics Monte Carlo Generators in C++
# PATCH-FEATURE-OPENSUSE HepMC-disable-doxygen-html-timestamp.patch badshah400@gmail.com -- Disable timestamps in doxygen generated HTML footers
Patch0:         HepMC-disable-doxygen-html-timestamp.patch
# Note: pybind11 (BSD-3-Clause) is bundled but not used because we use the system packaged pybind11
License:        GPL-3.0-or-later
URL:            http://hepmc.web.cern.ch/hepmc/
Source:         http://hepmc.web.cern.ch/hepmc/releases/%{name}3-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pybind11-devel >= 2.6.0}
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz-gd
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%python_subpackages

%description
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

%package -n %{libmain}
Summary:        Main shared library for HepMC
License:        GPL-3.0-or-later
Obsoletes:      libHepMC3-1 < %{version}
Provides:       %{name}3 = %{version}

%description -n %{libmain}
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the main shared library for HepMC3.

%package -n %{libsearch}
Summary:        Shared library for HepMC search
License:        GPL-3.0-or-later
Obsoletes:      libHepMC3-1 < %{version}

%description -n %{libsearch}
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the shared library for HepMC3 searches.

%package devel
Summary:        Header files for HepMC
License:        GPL-3.0-or-later
Requires:       %{libmain} = %{version}
Requires:       %{libsearch} = %{version}
Recommends:     %{name}-doc = %{version}
Provides:       %{name}3-devel = %{version}

%description devel
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the source and header files required for
developing with HepMC.

%package doc
Summary:        API documentation for HepMC
License:        GPL-3.0-or-later

%description doc
The HepMC package is an object oriented event record written in C++
for High Energy Physics Monte Carlo Generators. Many extensions from
HEPEVT, the Fortran HEP standard, are supported.

This package provides the API documentation for the HepMC library.

%prep
%autosetup -p1 -n %{name}3-%{version}
# Delete bundled pybind11 dir (we use system installed pybind11 headers)
rm -fr python/include

%build
%{python_expand # Necessary to run configure with all python flavors
export PYTHON=$python
mkdir ../${PYTHON}_build
cp -pr ./ ../${PYTHON}_build
pushd ../${PYTHON}_build
%cmake -DHEPMC3_ENABLE_ROOTIO:BOOL=%{?with_rootio:ON}%{!?with_rootio:OFF} \
       -DHEPMC3_BUILD_STATIC_LIBS:BOOL=OFF \
       -DHEPMC3_INSTALL_INTERFACES:BOOL=ON \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}3 \
       -DHEPMC3_PYTHON_VERSIONS:STRING="%{$python_version}" \
       -DCMAKE_SKIP_RPATH:BOOL=OFF \
       -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
       -DHEPMC3_ENABLE_TEST:BOOL=ON \
%if "%{$python_provides}" == "python3" || "$python_" == "python3_"
       -DHEPMC3_BUILD_EXAMPLES:BOOL=ON \
       -DHEPMC3_BUILD_DOCS:BOOL=ON \
%else
       -DHEPMC3_BUILD_EXAMPLES:BOOL=OFF \
       -DHEPMC3_BUILD_DOCS:BOOL=OFF \
%endif
       %{nil}
%cmake_build
popd
}

%install
%{python_expand # For all python flavors
export PYTHON=$python
pushd ../${PYTHON}_build
%cmake_install
popd
}

%fdupes %{buildroot}%{_docdir}/%{name}3/

# Temporarily disable tests for i586 until tolerance issues are sorted out
%ifnarch %ix86
%check
%{python_expand # For all python flavors
export PYTHON=$python
pushd ../${PYTHON}_build
%ctest
popd
}
%endif

%post   -n %{libmain} -p /sbin/ldconfig
%postun -n %{libmain} -p /sbin/ldconfig
%post   -n %{libsearch} -p /sbin/ldconfig
%postun -n %{libsearch} -p /sbin/ldconfig

%files -n %{libmain}
%license LICENCE COPYING
%{_libdir}/libHepMC3.so.%{so_main}*

%files -n %{libsearch}
%license LICENCE COPYING
%{_libdir}/libHepMC3search.so.%{so_search}*

%files -n %{name}-devel
%license LICENCE COPYING
%doc README* ChangeLog
%{_bindir}/HepMC3-config
%{_libdir}/libHepMC3.so
%{_libdir}/libHepMC3search.so
%{_includedir}/%{name}3/
%{_datadir}/%{name}3/

%files -n %{name}-doc
%doc %{_docdir}/%{name}3/

%files %{python_files}
%license LICENCE COPYING
%{python_sitearch}/pyHepMC3/
%{python_sitearch}/pyHepMC3-%{version}-py%{python_version}.egg-info
%{python_sitearch}/pyHepMC3.search-%{version}-py%{python_version}.egg-info

%changelog
