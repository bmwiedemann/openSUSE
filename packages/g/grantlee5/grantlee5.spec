#
# spec file for package grantlee5
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without tests

%{?!cmake_build:%global cmake_build() make %{?_smp_mflags} VERBOSE=1}
%{?!cmake_install:%global cmake_install() DESTDIR=%{buildroot} make install}

Name:           grantlee5
Version:        5.2.0
Release:        0
Summary:        Qt string template library
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            http://grantlee.org/
Source:         http://www.grantlee.org/downloads/grantlee-%{version}.tar.gz
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE includes.diff -- since upstream doesn't provide a way to install to custom directory, we cheat!
Patch0:         includes.diff
# PATCH-FIX-OPENSUSE grantlee-5.2.0-fix-ctest-ld-library-path.patch -- set ld library path for tests
Patch1:         grantlee-5.2.0-fix-ctest-ld-library-path.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  cmake(Qt5Core) >= 5.3
BuildRequires:  cmake(Qt5Gui) >= 5.3
BuildRequires:  cmake(Qt5Qml) >= 5.3
%if %{with tests}
BuildRequires:  /usr/bin/Xvfb
BuildRequires:  xvfb-run
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test) >= 5.3
%endif

%description
Grantlee is a string template engine based on the Django template system and
written in Qt.

%package devel
Summary:        Include Files and Libraries Mandatory for Development with Grantlee
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       cmake >= 3.5
Requires:       cmake(Qt5Core) >= 5.3
Requires:       cmake(Qt5Gui) >= 5.3

%description devel
This package contains include files and libraries needed for development with
grantlee.

%prep
%autosetup -p1 -n grantlee-%{version}

%build
%cmake \
  %{!?with_tests:-DBUILD_TESTS:BOOL=OFF}

%cmake_build

%install
%cmake_install

%if %{with tests}
%check
export CTEST_OUTPUT_ON_FAILURE=1
xvfb-run -a make test -C %{__builddir}
%endif

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
