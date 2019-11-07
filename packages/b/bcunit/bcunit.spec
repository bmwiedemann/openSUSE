#
# spec file for package bcunit
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


%define soname  libbcunit
%define sover   1
Name:           bcunit
Version:        3.0.2
Release:        0
Summary:        Provide C programmers basic testing functionality
License:        LGPL-2.0-or-later
Url:            https://linphone.org/
Source:         https://linphone.org/releases/sources/%{name}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-OPENSUSE bcunit-link-ncurses.patch jengelh@medozas.de
Patch0:         bcunit-link-ncurses.patch
# PATCH-FIX-OPENSUSE bcunit-ncurses6.patch idonmez@suse.com -- Compile with ncurses6.
Patch1:         bcunit-ncurses6.patch
# PATCH-FIX-OPENSUSE bcunit-sover.patch sor.alexei@meowr.ru -- Correctly set the sover.
Patch2:         bcunit-sover.patch
BuildRequires:  cmake
BuildRequires:  ncurses-devel
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
%setup -q -n BCunit-%{version}-Source
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake \
  -DENABLE_STATIC=OFF    \
  -DENABLE_AUTOMATED=ON  \
  -DENABLE_BASIC=ON      \
  -DENABLE_CONSOLE=ON    \
  -DENABLE_CURSES=ON     \
  -DENABLE_EXAMPLES=ON
make %{?_smp_mflags} V=1

%install
%cmake_install

# Architecture dependent files.
mkdir -p %{buildroot}%{_libdir}/BCUnit/
mv %{buildroot}%{_datadir}/BCUnit/Examples/ \
  %{buildroot}%{_libdir}/BCUnit/

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_libdir}/%{soname}.so.%{sover}*

%files doc
%defattr(-,root,root)
%dir %{_datadir}/BCUnit/
%{_datadir}/BCUnit/*

%files devel
%defattr(-,root,root)
%{_includedir}/BCUnit/
%dir %{_datadir}/BCunit/
%{_libdir}/BCUnit/
%{_libdir}/%{soname}.so
%{_libdir}/pkgconfig/bcunit.pc
%{_datadir}/BCunit/cmake/

%changelog
