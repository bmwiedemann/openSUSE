#
# spec file for package lensfun
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


%define sonum   1
Name:           lensfun
Version:        0.3.4
Release:        0
Summary:        A photographic lens database and a library for accessing it
License:        CC-BY-SA-3.0 AND LGPL-3.0-only
URL:            https://lensfun.github.io/
Source0:        https://github.com/lensfun/lensfun/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# updated lens database, use "osc service dr" to update it.
Source1:        data-master.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         lensfun-cmake4.patch
# PATCH-FIX-UPSTREAM
Patch1:         lensfun-python314.patch
# PATCH-FIX-UPSTREAM lensfun-pr2256-setuptools.patch gh#lensfun/lensfun#2256 backported and without build isolation for offline build
Patch2:         lensfun-pr2256-setuptools.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  python3-docutils
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
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
Summary:        Data files for lensfun
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

%package -n liblensfun%{sonum}
Summary:        Library files for lensfun
Requires:       lensfun-data
Provides:       lensfun = %{version}
Obsoletes:      lensfun < %{version}

%description -n liblensfun%{sonum}
Library files needed by the use the lensfun library/database.

%package -n python3-lensfun
Summary:        Python3 lensfun bindings
Requires:       liblensfun%{sonum} = %{version}
BuildArch:      noarch

%description -n python3-lensfun
Lensfun bindings for Python 3

%package tools
Summary:        Tools for managing lensfun data
Requires:       lensfun-data
Requires:       python3-lensfun = %{version}

%description tools
This package contains tools to fetch lens database updates and manage lens
adapters in lensfun.

%package doc
Summary:        Documentation for lensfun
Requires:       lensfun-data
BuildArch:      noarch

%description doc
Documentation and manual files for the lensfun library/database.

%package devel
Summary:        Header and library definition files for lensfun
Requires:       lensfun-data = %{version}
Requires:       liblensfun%{sonum} = %{version}

%description devel
Header and library definition files for developing applications
that use the lensfun library/database.

%prep
%autosetup -p1 -a 1
echo 'HTML_TIMESTAMP=NO' >> docs/doxyfile.in.cmake
# fix python shebangs
sed -i \
    -e "s|^#!/usr/bin/env python3$|#!/usr/bin/python3|g" \
  apps/lensfun-add-adapter \
  apps/lensfun-update-data
# remove shebang from non-executable
sed -i \
    -e '1 {/^#!/d}' \
  apps/lensfun/__init__.py.in

sed -i 's#/usr/bin/env sh#/usr/bin/sh#' apps/g-lensfun-update-data

%build
%cmake \
    -DBUILD_LENSTOOL:BOOL=ON \
    -DBUILD_STATIC:BOOL=OFF \
    -DBUILD_TESTS:BOOL=ON \
    -DBUILD_DOC:BOOL=ON \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_defaultdocdir}/lensfun \
    -DINSTALL_HELPER_SCRIPTS:BOOL=ON \
    -DPYTHON_EXECUTABLE:STRING=python3

%cmake_build

%install
%cmake_install

# Create update folder for lensfun data
mkdir -p %{buildroot}%{_localstatedir}/lib/lensfun-updates

%fdupes %{buildroot}
%python3_fix_shebang

%check
# ERROR: lensfun-0.3.4/tests/test_database.cpp:29:void test_DB_lens_search(lfFixture*, gconstpointer): 'lenses' should not be nullptr
%ifnarch %ix86 armv7hl
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}
%ctest
%endif

%ldconfig_scriptlets -n liblensfun%{sonum}

%files doc
%doc README.md
%doc docs/*
%doc %{_defaultdocdir}/lensfun

%files data
%{_datadir}/lensfun/
%dir %{_localstatedir}/lib/lensfun-updates/

%files -n liblensfun%{sonum}
%{_libdir}/*.so.*

%files -n python3-lensfun
%{python3_sitelib}/lensfun/
%{python3_sitelib}/lensfun-%{version}.dist-info

%files devel
%{_includedir}/lensfun/
%{_libdir}/*.so
%{_libdir}/pkgconfig/lensfun.pc

%files tools
%{_bindir}/g-lensfun-update-data
%{_bindir}/lensfun-add-adapter
%{_bindir}/lensfun-update-data
%{_bindir}/lenstool
%{_mandir}/man?/g-lensfun-update-data*
%{_mandir}/man?/lensfun-add-adapter*
%{_mandir}/man?/lensfun-update-data*

%changelog
