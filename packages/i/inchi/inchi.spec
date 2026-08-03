#
# spec file for package inchi
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%{?sle15_python_module_pythons}

%define abiver  1
Name:           inchi
Version:        1.07.5
Release:        0
Summary:        The IUPAC International Chemical Identifier
License:        MIT
URL:            https://www.inchi-trust.org/
Source0:        https://github.com/IUPAC-InChI/InChI/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
## use system installed gtest, do not fetch on-the-fly
Patch0:         inchi-1.07-no-fetchcontent.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
Suggests:       inchi-doc
## test dependencies
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  %{pythons}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pytest}

%description
The IUPAC International Chemical Identifier (InChI) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

This package contains the command line conversion utility.

%package -n libinchi%{abiver}
Summary:        The IUPAC International Chemical Identifier library

%description -n libinchi%{abiver}
The IUPAC International Chemical Identifier (InChI) is a non-proprietary
identifier for chemical substances that can be used in printed and
electronic data sources thus enabling easier linking of diverse data
compilations. It was developed under IUPAC Project 2000-025-1-800 during
the period 2000-2004. Details of the project and the history of its
progress are available from the project web site.

This package contains the InChi shared library.

%package devel
Summary:        Development headers for the InChI library
Requires:       libinchi%{abiver} = %{version}
Suggests:       inchi-doc
# openbabel-devel used to ship the headers of its bundled inchi
Conflicts:      openbabel-devel <= 2.4.1

%description devel
This package contains the development files for the InChI library.

%package doc
Summary:        Documentation for the InChI library
BuildArch:      noarch

%description doc
This package contains the user documentation for the InChI software
and InChI library API reference for developers.

%prep
%setup -q -n InChI-%{version}
%autopatch -p1

## req'd by gtest
sed -e 's:CMAKE_CXX_STANDARD 11:CMAKE_CXX_STANDARD 17:' -i CMakeLists.txt
## fix link failures w/ system gtest
sed -e "/target_link_libraries/s:gtest_main gmock_main test_dependencies libinchi:& gtest gmock:" \
    -i INCHI-1-TEST/tests/test_unit/CMakeLists.txt
## (re-)introduce versioned sonames, see github.com/IUPAC-InChI/InChI/issues/195
sed -e '/add_library(libinchi SHARED)/a\
set_target_properties(libinchi PROPERTIES VERSION ${PROJECT_VERSION} SOVERSION ${PROJECT_VERSION_MAJOR})' \
    -i INCHI-1-SRC/INCHI_API/libinchi/src/CMakeLists.txt

%build
%cmake
%cmake_build

%install
## no cmake install rules provided
# Install binary
install -pm 755 %{__builddir}/INCHI-1-SRC/INCHI_EXE/inchi-1/src/bin/inchi-1 -D -t %{buildroot}%{_bindir}

# Install shared library and do the appropriate links
install -p %{__builddir}/INCHI-1-SRC/INCHI_API/libinchi/src/lib/libinchi.so.%{abiver}.* -D -t %{buildroot}%{_libdir}
ln -s $(basename %{buildroot}%{_libdir}/libinchi.so.%{abiver}.*) %{buildroot}%{_libdir}/libinchi.so.%{abiver}
ln -s libinchi.so.%{abiver} %{buildroot}%{_libdir}/libinchi.so

# Install the headers
install -pm644 INCHI-1-SRC/INCHI_BASE/src/{bcf_s,inchi_api,ixa}.h -D -t %{buildroot}%{_includedir}/inchi

## install doc files, silence rpmlint wrt. file dups
install -d %{buildroot}%{_defaultdocdir}/%{name}-doc
cp -r INCHI-1-DOC/* %{buildroot}%{_defaultdocdir}/%{name}-doc
%fdupes %{buildroot}%{_defaultdocdir}/%{name}-doc

%post -n libinchi%{abiver} -p /sbin/ldconfig
%postun -n libinchi%{abiver} -p /sbin/ldconfig

%check
%ctest
pushd INCHI-1-TEST
## fix hardcoded paths
sed -e "/SDF_PATH = /s:INCHI-1-TEST/::" \
    -e "s:CMake_build/full_build/INCHI-1-SRC/INCHI_API/libinchi/src/lib/libinchi.so:%{buildroot}%{_libdir}/libinchi.so:" \
    -i tests/test_library/test_multithreading.py
## increase assert time (or disable "test_execution_time")
sed -e "/assert execution_time/s: < 10: < 100:" -i tests/test_meta/test_performance.py
## disable test_permutation, unpackaged python module rdkit
mv tests/test_meta/{test,notest}_permutation.py
## fix for use of pydantic v1 in leap 15.6
##%%if 0%%{?sle_version} == 150600 && 0%%{?is_opensuse}
## is_opensuse seems unset in OBS science project
%if 0%{?sle_version} == 150600
sed -e "s:.model_dump_json():.json():" -i src/sdf_pipeline/drivers.py
%endif
export PYTHONPATH=src
pytest --exe-path=%{buildroot}/%{_bindir}/inchi-1
mv tests/test_meta/{notest,test}_permutation.py
popd

%files
%license LICENSE
%{_bindir}/inchi-1

%files -n libinchi%{abiver}
%license LICENSE
%{_libdir}/libinchi.so.%{abiver}*

%files devel
%license LICENSE
%{_includedir}/inchi
%{_libdir}/libinchi.so

%files doc
%license LICENSE
%{_defaultdocdir}/inchi-doc

%changelog
