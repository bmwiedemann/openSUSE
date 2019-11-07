#
# spec file for package med-tools
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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
License:        LGPL-3.0
Group:          Productivity/Graphics/Other
Version:        4.0.0
Release:        0
Url:            https://www.salome-platform.org/downloads/current-version
Source0:        https://files.salome-platform.org/Salome/other/med-%{version}.tar.gz
# PATCH-FIX-OPENSUSE
Patch0:         fix-cmakefiles.patch
# PATCH-FIX-OPENSUSE
Patch1:         0001-Fix-error-message-concatenation.patch
# PATCH-FIX-OPENSUSE
Patch2:         0002-Return-this-from-operator-in-medenum-python-wrapper.patch
# PATCH-FIX-OPENSUSE
Patch3:         0003-Avoid-format-warnings-on-64-bit.patch
# PATCH-FIX-OPENSUSE
Patch4:         0004-Fix-allocation-for-MEDfileName-consider-trailing-nul.patch
# PATCH-FIX-OPENSUSE
Patch5:         0005-Respect-DESTDIR-when-byte-compiling-python-code.patch
# PATCH-FIX-OPENSUSE
Patch6:         use_installed_python_modules_for_tests.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  hdf5-devel >= 1.10.2
BuildRequires:  make
BuildRequires:  zlib-devel
%if %{with python_bindings}
BuildRequires:  python3-devel
BuildRequires:  swig
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
Requires:       libmed%{sover} = %{version}
Requires:       libmedC%{sover} = %{version}
Requires:       libmedimport0 = %{version}
Requires:       hdf5-devel >= 1.10.2
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
%setup -q -n med-%{version}
%patch0 -p0
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1


%build
%cmake \
 -DMEDFILE_BUILD_PYTHON:BOOL=%{?with_python_bindings:ON}%{!?with_python_bindings:OFF} \
 -DMEDFILE_USE_MPI:BOOL=%{?with_mpi:ON}%{!?with_mpi:OFF} \
 -DMEDFILE_INSTALL_DOC:BOOL=ON

%make_jobs


%install
%cmake_install

# drop tests
rm -rf %buildroot/usr/bin/test*

# fix bash tag
sed -i -e 's,/usr/bin/env wish,/usr/bin/wish,' %buildroot/usr/bin/xmdump*

# move documentation
mkdir -p %{buildroot}/%{_datadir}/doc/packages/
mv %{buildroot}/%{_datadir}/doc/med* %{buildroot}/%{_datadir}/doc/packages/med-tools

# add missing symlinks, install tries to generate these outside the buildroot
ln -sf mdump3 %{buildroot}/usr/bin/mdump
ln -sf xmdump3 %{buildroot}/usr/bin/xmdump


%check
cd build
export LC_ALL=C.utf8
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:%{buildroot}%{_libdir}
export PYTHONPATH=$PYTHONPATH:%{buildroot}%{python3_sitearch}
make test ARGS="--output-on-failure"

%fdupes -s %{buildroot}

%post -n libmed%{sover} -p /sbin/ldconfig

%post -n libmedC%{sover} -p /sbin/ldconfig

%post -n libmedfwrap%{sover} -p /sbin/ldconfig

%postun -n libmed%{sover} -p /sbin/ldconfig

%postun -n libmedC%{sover} -p /sbin/ldconfig

%postun -n libmedfwrap%{sover} -p /sbin/ldconfig

%post -n libmedimport0 -p /sbin/ldconfig

%postun -n libmedimport0 -p /sbin/ldconfig

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
