#
# spec file for package grantlee5
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           grantlee5
Version:        5.1.0
Release:        0
Summary:        Qt string template library
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://grantlee.org/
Source:         http://downloads.grantlee.org/grantlee-%{version}.tar.gz
Source2:        baselibs.conf
# PATCH-FIX-UPSTREAM includes.diff -- since upstream doesn't provide a way to install to custom directory, we cheat!
Patch0:         includes.diff
# PATCH-FIX-UPSTREAM fix-build-with-Qt-5.13.patch
Patch1:         fix-build-with-Qt-5.13.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Remove-vestigial-ansi-flag.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core) >= 5.3
BuildRequires:  pkgconfig(Qt5Gui) >= 5.3
BuildRequires:  pkgconfig(Qt5Script) >= 5.3

%description
Grantlee is a string template engine based on the Django template system and
written in Qt.

%package devel
Summary:        Include Files and Libraries Mandatory for Development with Grantlee
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       cmake >= 2.8.12
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5Gui)

%description devel
This package contains include files and libraries needed for development with
grantlee.

%prep
%autosetup -p1 -n grantlee-%{version}

%build
%cmake \
  -DCMAKE_BUILD_TYPE=None \
  -DBUILD_TESTS=OFF

# Still not available on all leap flavors
# %%cmake_build
%make_jobs

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING*
%doc AUTHORS CHANGELOG README*
%{_libdir}/libGrantlee_TextDocument.so.*
%{_libdir}/libGrantlee_Templates.so.*
%{_libdir}/grantlee/

%files devel
%license COPYING*
%doc AUTHORS CHANGELOG README*
%{_includedir}/grantlee5/
%{_libdir}/libGrantlee_TextDocument.so
%{_libdir}/libGrantlee_Templates.so
%{_libdir}/cmake/Grantlee5/

%changelog
