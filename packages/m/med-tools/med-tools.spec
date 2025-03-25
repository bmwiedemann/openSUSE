#
# spec file for package med-tools
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


%define sover 11

%bcond_without python_bindings
%bcond_with    mpi

Name:           med-tools
Summary:        A library to store and exchange meshed data
License:        LGPL-3.0-only
Group:          Productivity/Graphics/Other
Version:        5.0.0
Release:        0
URL:            https://www.salome-platform.org/
# Download server is unreachable except for specific user-agents, causing issues with bots
# curl -A MozillaFirefox https://files.salome-platform.org/Salome/medfile/med-%{version}.tar.bz2
# sha256sum 267e76d0c67ec51c10e3199484ec1508baa8d5ed845c628adf660529dce7a3d4
Source0:        med-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE
Patch0:         fix-cmakefiles.patch
# PATCH-FIX-OPENSUSE
Patch1:         0003-Avoid-format-warnings-on-64-bit.patch
# PATCH-FIX-OPENSUSE
Patch2:         use_installed_python_modules_for_tests.patch
# PATCH-FIX-OPENSUSE
Patch3:         Fix-no_return_in_nonvoid_function.patch
# PATCH-FIX-OPENSUSE
Patch4:         0001-Fix-AppendOutput-signature-for-Swig-4.3.patch
# PATCH-FIX-UPSTREAM
Patch5:         https://src.fedoraproject.org/rpms/med/raw/rawhide/f/hdf5-1.14.patch#/med-tools-hdf1_14.patch
# PATCH-FIX-UPSTREAM rebase based on ref:https://src.fedoraproject.org/rpms/med/blob/rawhide/f/med-py3.13.patch
Patch6:         med-tools-python3_13.patch
# PATCH-FIX-UPSTREAM
Patch7:         https://src.fedoraproject.org/rpms/med/raw/rawhide/f/med-gcc15.patch#/med-tools-gcc15.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5-devel >= 1.12.1
BuildRequires:  make
BuildRequires:  zlib-devel
%if %{with python_bindings}
BuildRequires:  python3-devel
BuildRequires:  swig >= 4.1
%endif
# test suite fails and we don't build FreeCAD on 32bit either anymore
ExcludeArch:    %ix86

%description
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

%package -n libmedC%{sover}
Summary:        C++ API for the MED mesh data library
Group:          System/Libraries

%description -n libmedC%{sover}
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

%package -n libmedfwrap%{sover}
Summary:        Fortran API for the MED mesh data library
Group:          System/Libraries

%description -n libmedfwrap%{sover}
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

%package -n libmed%{sover}
Summary:        A library to store and exchange meshed data
Group:          System/Libraries

%description -n libmed%{sover}
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

%package -n libmed-python
Summary:        Python wrapper for the MED library
Group:          Development/Languages/Python

%description -n libmed-python
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

This package contains the python bindings

%package -n libmed-devel
Requires:       hdf5-devel >= 1.12.1
Requires:       libmed%{sover} = %{version}
Requires:       libmedC%{sover} = %{version}
Requires:       libmedimport0 = %{version}
Summary:        Libmed development files
Group:          Development/Libraries/C and C++

%description -n libmed-devel
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

%package -n libmedimport0
Summary:        MED import Library
Group:          System/Libraries

%description -n libmedimport0
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

%package  doc
Summary:        MED documentation
Group:          Documentation/HTML
BuildArch:      noarch

%description  doc
MED-fichier (Modélisation et Echanges de Données,
in English Modelisation and Data Exchange) is a library
to store and exchange meshed data or computation results.
It uses the HDF5 file format to store the data.

%prep
%autosetup -p1 -n med-%{version}

# Fix file not utf8
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.new && \
touch -r ChangeLog ChangeLog.new && \
mv ChangeLog.new ChangeLog

%build
%cmake \
 -DMEDFILE_BUILD_PYTHON:BOOL=%{?with_python_bindings:ON}%{!?with_python_bindings:OFF} \
 -DMEDFILE_USE_MPI:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF} \
 -DMEDFILE_INSTALL_DOC:BOOL=ON

%cmake_build

%install
%cmake_install

# drop tests
rm -rf %buildroot/usr/bin/test*

# fix bash tag
sed -i -e 's,/usr/bin/env wish,/usr/bin/wish,' %buildroot/usr/bin/xmdump*

# move documentation
mkdir -p %{buildroot}/%{_docdir}
mv %{buildroot}/%{_datadir}/doc/med* %{buildroot}/%{_docdir}/med-tools

# add missing symlinks, install tries to generate these outside the buildroot
ln -sf mdump3 %{buildroot}/usr/bin/mdump
ln -sf xmdump3 %{buildroot}/usr/bin/xmdump

%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_includedir}
%if %{with python_bindings}
%fdupes %{buildroot}%{python_sitearch}
%endif

%check
cd build
export LC_ALL=C.utf8
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitearch}
%make_build test ARGS="--output-on-failure"

%ldconfig_scriptlets -n libmed%{sover}
%ldconfig_scriptlets -n libmedC%{sover}
%ldconfig_scriptlets -n libmedfwrap%{sover}
%ldconfig_scriptlets -n libmedimport0

%files
%{_bindir}/mdump*
%{_bindir}/medconforme
%{_bindir}/medimport
%{_bindir}/xmdump*

%files -n libmed%{sover}
%{_libdir}/libmed.so.*

%files -n libmed-devel
%{_datadir}/cmake/*
%{_includedir}/*
%{_libdir}/*.so

%files -n libmedC%{sover}
%{_libdir}/libmedC.so.*

%files -n libmedfwrap%{sover}
%{_libdir}/libmedfwrap.so.*

%files -n libmedimport0
%{_libdir}/libmedimport.so.*

%if %{with python_bindings}
%files -n libmed-python
%{_libdir}/python*
%endif

%files doc
%{_docdir}/med-tools

%changelog
