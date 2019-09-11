#
# spec file for package cppcheck
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


Name:           cppcheck
Version:        1.88
Release:        0
Summary:        A tool for static C/C++ code analysis
License:        GPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://cppcheck.sourceforge.net/
Source:         https://downloads.sourceforge.net/cppcheck/cppcheck-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc-c++
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libpcre)
Requires:       python3-Pygments

%description
This program tries to detect bugs that your C/C++ compiler don't see. Cppcheck
is versatile. You can check non-standard code that includes various compiler
extensions, inline assembly code, etc. Checking covers for example these
errors:

 * Out of bounds
 * Uninitialized member variable 'classname::varname'
 * Using 'memfunc' on class
 * Using 'memfunc' on struct that contains a 'std::classname'
 * Class Base which is inherited by class Derived does not have a virtual
   destructor
 * Memory leak: varname
 * Resource leak: varname
 * Deallocating a deallocated pointer: varname
 * Using 'varname' after it is deallocated / released
 * Invalid radix in call to strtol or strtoul. Must be 0 or 2-36
 * Overlapping data buffer varname
 * Unsigned division. The result will be wrong.
 * Unusual pointer arithmetic

%package gui
Summary:        A tool for static C/C++ code analysis
Group:          Development/Languages/C and C++
Requires:       cppcheck

%description gui

This is the gui for Cppcheck, a program to detect bugs that your C/C++ compiler
doesn't see.

%prep
%setup -q

%build
%cmake \
  -DCMAKE_CXX_FLAGS="-DNDEBUG %{optflags} -UCFGDIR -DCFGDIR=\\\"%{_datadir}/%{name}\\\"" \
  -DBUILD_GUI=ON \
  -DBUILD_TESTS=ON \
  -DHAVE_RULES=yes
%make_jobs

# does not work with CMake, directly call provided Makefile from source directory
cd ..
make man \
    DB2MAN=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl

# use python3 as interpreter
sed -i "s|env python|python3|g" htmlreport/cppcheck-htmlreport

%check
export CXXFLAGS="%{optflags}"
%make_jobs check

%install
install -Dpm 0755 build/bin/cppcheck \
  %{buildroot}%{_bindir}/cppcheck
install -Dpm 0755 htmlreport/cppcheck-htmlreport \
  %{buildroot}%{_bindir}/cppcheck-htmlreport
install -Dpm 0755 build/bin/cppcheck-gui \
  %{buildroot}%{_bindir}/cppcheck-gui
install -Dpm 0644  cppcheck.1 \
  %{buildroot}%{_mandir}/man1/cppcheck.1
install -d %{buildroot}%{_datadir}/%{name}
install -pm 0644 cfg/*.cfg %{buildroot}%{_datadir}/%{name}

%files
%doc AUTHORS
%license COPYING
%{_bindir}/cppcheck
%{_bindir}/cppcheck-htmlreport
%{_datadir}/%{name}/
%{_mandir}/man1/cppcheck.1%{?ext_man}

%files gui
%{_bindir}/cppcheck-gui

%changelog
