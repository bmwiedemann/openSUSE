#
# spec file for package lensfun
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


%define sonum   1
Name:           lensfun
Version:        0.3.2
Release:        0
Summary:        A photographic lens database and a library for accessing it
License:        LGPL-3.0
Group:          Development/Libraries/C and C++
Url:            http://lensfun.sourceforge.net/
Source:         http://downloads.sf.net/lensfun/lensfun-%{version}.tar.gz
# PATCH-FIX-UPSTREAM respect DESTDIR in python call
Patch0:         lensfun-respect-DESTDIR.patch
# PATCH-FIX-UPSTREAM use local database when running tests
Patch1:         lensfun-test-database.patch
# PATCH-FIX-UPSTREAM 0060-Various-CMake-patches-from-the-mailing-list.patch
Patch2:         0060-Various-CMake-patches-from-the-mailing-list.patch
# PATCH-FIX-UPSTREAM lensfun_fix_memory_leak.patch
Patch3:         lensfun_fix_memory_leak.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-docutils
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glib-2.0)

%description
The goal of the lensfun library is to provide a open source database
of photographic lenses and their characteristics. In the past there
was a effort in this direction (see http://www.epaperpress.com/ptlens/),
but then author decided to take the commercial route and the database
froze at the last public stage. This database was used as the basement
on which lensfun database grew, thanks to PTLens author which gave his
permission for this, while the code was totally rewritten from scratch
(and the database was converted to a totally new, XML-based format).

The lensfun library not only provides a way to read the database and
search for specific things in it, but also provides a set of algorithms
for correcting images based on detailed knowledge of lens properties
and calibration data. Right now lensfun is designed to correct distortion,
transversal (also known as lateral) chromatic aberrations, vignetting
and colour contribution index of the lens.

%package data
Summary:        Data files for %{name}/%{name}-devel
Group:          System/Libraries
BuildArch:      noarch

%description data
The goal of the lensfun library is to provide a open source database
of photographic lenses and their characteristics. In the past there
was a effort in this direction (see http://www.epaperpress.com/ptlens/),
but then author decided to take the commercial route and the database
froze at the last public stage. This database was used as the basement
on which lensfun database grew, thanks to PTLens author which gave his
permission for this, while the code was totally rewritten from scratch
(and the database was converted to a totally new, XML-based format).

The lensfun library not only provides a way to read the database and
search for specific things in it, but also provides a set of algorithms
for correcting images based on detailed knowledge of lens properties
and calibration data. Right now lensfun is designed to correct distortion,
transversal (also known as lateral) chromatic aberrations, vignetting
and colour contribution index of the lens.

%package -n lib%{name}%{sonum}
Summary:        Library files for %{name}/%{name}-devel
Group:          System/Libraries
Requires:       %{name}-data
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n lib%{name}%{sonum}
Library files needed by the use the %{name} library/database.

%package -n python3-lensfun
Summary:        Python3 lensfun bindings
Group:          Development/Languages/Python
Requires:       lib%{name}%{sonum} = %{version}

%description -n python3-lensfun
Lensfun bindings for Python 3

%package tools
Summary:        Tools for managing %{name} data
Group:          Development/Tools/Other
Requires:       %{name}-data
Requires:       python3-lensfun = %{version}

%description tools
This package contains tools to fetch lens database updates and manage lens
adapters in lensfun.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/HTML
Requires:       %{name}-data

%description doc
Documentation and manual files for the %{name} library/database.

%package devel
Summary:        Header and library definition files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-data = %{version}
Requires:       lib%{name}%{sonum} = %{version}

%description devel
Header and library definition files for developing applications
that use the %{name} library/database.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
echo 'HTML_TIMESTAMP=NO' >> docs/doxyfile.in.cmake
# fix python shebangs
sed -i \
    -e "s|^#!/usr/bin/env python3$|#!/usr/bin/python3|g" \
  apps/lensfun-add-adapter \
  apps/lensfun-update-data \
  apps/lensfun/__init__.py.in

%build
%cmake \
    -DBUILD_STATIC=OFF \
    -DBUILD_TESTS=ON \
    -DBUILD_DOC=ON \
    -DDOCDIR=%{_defaultdocdir}/%{name} \
    -DCMAKE_INSTALL_DOCDIR=%{_defaultdocdir}/%{name} \
    -DINSTALL_HELPER_SCRIPTS=ON \
    -DPYTHON_EXECUTABLE=%{_bindir}/python3
make %{?_smp_mflags} lensfun doc

%install
%cmake_install
# drop test cases, we should run them here instead
rm -rf %{buildroot}%{_datadir}/lensfun/tests
# Create udate folder for lensfun data
mkdir -p %{buildroot}%{_localstatedir}/lib/lensfun-updates
# Regererate pyc files to not contain %{buildroot}
%py3_compile %{buildroot}/%{python3_sitelib}/lensfun/

%fdupes %{buildroot}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%ctest

%post   -n lib%{name}%{sonum} -p /sbin/ldconfig
%postun -n lib%{name}%{sonum} -p /sbin/ldconfig

%files doc
%doc README.md
%doc docs/*
%doc %{_defaultdocdir}/%{name}

%files data
%{_datadir}/%{name}/
%dir %{_localstatedir}/lib/lensfun-updates/

%files -n lib%{name}%{sonum}
%{_libdir}/*.so.*

%files -n python3-lensfun
%{python3_sitelib}/lensfun/
%{python3_sitelib}/lensfun*.egg-info

%files devel
%{_includedir}/lensfun
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc

%files tools
%{_bindir}/g-lensfun-update-data
%{_bindir}/lensfun-add-adapter
%{_bindir}/lensfun-update-data
%{_mandir}/man?/g-lensfun-update-data*
%{_mandir}/man?/lensfun-add-adapter*
%{_mandir}/man?/lensfun-update-data*

%changelog
