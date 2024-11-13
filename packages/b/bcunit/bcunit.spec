#
# spec file for package bcunit
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


%define soname  libbcunit
%define sover   1
Name:           bcunit
Version:        5.3.95
Release:        0
Summary:        Provide C programmers basic testing functionality
License:        LGPL-2.0-or-later
URL:            https://linphone.org/
Source:         https://gitlab.linphone.org/BC/public/bcunit/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE bcunit-link-ncurses.patch jengelh@medozas.de
Patch0:         bcunit-link-ncurses.patch
# PATCH-FIX-OPENSUSE bcunit-ncurses6.patch idonmez@suse.com -- Compile with ncurses6.
Patch1:         bcunit-ncurses6.patch
# PATCH-FIX-OPENSUSE bcunit-sover.patch sor.alexei@meowr.ru -- Correctly set the sover.
Patch2:         bcunit-sover.patch
# PATCH-FIX-UPSTREAM
Patch3:         set_current_version.patch
BuildRequires:  cmake >= 3.22
BuildRequires:  git-core >= 1.7.10
BuildRequires:  pkgconfig

%description
BCUnit is a unit testing framework for C, derived from CUnit.
(B)CUnit provides various interfaces to the framework, some of which
are platform dependent (e.g. curses on *nix). The framework complies
with the conventional structure of test cases bundled into suites
which are registered with the framework for running.

%package devel
Summary:        BCUnit development files
Requires:       %{soname}%{sover} = %{version}
Requires:       ncurses-devel
Recommends:     %{name}-doc = %{version}

%description devel
BCUnit is a unit testing framework for C.
This package installs the BCUnit development files.

%package doc
Summary:        BCUnit documentation
Requires:       %{soname}%{sover} = %{version}

%description doc
BCUnit is a unit testing framework for C.
This package installs the BCUnit documentation files.

%package -n %{soname}%{sover}
Summary:        BCUnit shared library

%description  -n %{soname}%{sover}
BCUnit is a unit testing framework for C.
This package installs the BCUnit shared library.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_BCUNIT_DOC=ON
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_libdir}/BCUnit/

%post -n %{soname}%{sover} -p /sbin/ldconfig
%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%doc AUTHORS ChangeLog NEWS README.md TODO
%license COPYING
%{_libdir}/%{soname}.so.%{sover}*

%files doc
%dir %{_datadir}/BCUnit/
%{_datadir}/BCUnit/*dtd
%{_datadir}/BCUnit/*xsl
%{_datadir}/man/man3/BCUnit.3.gz

%files devel
%dir %{_datadir}/BCUnit/
%dir %{_datadir}/BCUnit/cmake
%{_includedir}/BCUnit/
%{_libdir}/BCUnit/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/bcunit.pc
%{_datadir}/BCUnit/cmake/*

%changelog
