#
# spec file for package cppcheck
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


Name:           cppcheck
Version:        2.14.2
Release:        0
Summary:        A tool for static C/C++ code analysis
License:        GPL-3.0-or-later
URL:            https://github.com/danmar/cppcheck
Source:         https://github.com/danmar/cppcheck/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  xsltproc
BuildRequires:  z3-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libpcre)
ExcludeArch:    %ix86 %arm
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
Requires:       cppcheck

%description gui

This is the gui for Cppcheck, a program to detect bugs that your C/C++ compiler
doesn't see.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_CXX_FLAGS="%{optflags} -UNDEBUG" \
  -DFILESDIR="%{_datadir}/%{name}" \
  -DBUILD_GUI=ON \
  -DBUILD_TESTS=ON \
  -DHAVE_RULES=yes \
  -DUSE_Z3=yes
%cmake_build

# does not work with CMake, directly call provided Makefile from source directory
cd ..
%make_build man \
    DB2MAN=%{_datadir}/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl

# use python3 as interpreter
sed -i "s|env python3|python3|g" htmlreport/cppcheck-htmlreport

%check
export CXXFLAGS="%{optflags}"
%define _smp_mflags -j1
%ctest

%install
install -Dpm 0755 build/bin/cppcheck \
  %{buildroot}%{_bindir}/cppcheck
install -Dpm 0755 htmlreport/cppcheck-htmlreport \
  %{buildroot}%{_bindir}/cppcheck-htmlreport
install -Dpm 0755 build/bin/cppcheck-gui \
  %{buildroot}%{_bindir}/cppcheck-gui
install -Dpm 0644  cppcheck.1 \
  %{buildroot}%{_mandir}/man1/cppcheck.1
install -d %{buildroot}%{_datadir}/%{name}/cfg
install -pm 0644 cfg/*.cfg %{buildroot}%{_datadir}/%{name}/cfg
install -d %{buildroot}%{_datadir}/%{name}/platforms
install -pm 0644 platforms/*.xml %{buildroot}%{_datadir}/%{name}/platforms
install -d %{buildroot}%{_datadir}/%{name}/addons
install -pm 0644 addons/*.py %{buildroot}%{_datadir}/%{name}/addons
# Give execute permission to python addons with a shebang to fix non-executable-script
find %{buildroot}%{_datadir}/%{name}/addons -type f -size +0 -exec awk 'NR == 1 && /^#!.*python/ { exit } { exit 1 }' {} \; -print0 | xargs -0 chmod +x
# Correct shebang to fix env-script-interpreter
find %{buildroot}%{_datadir}/%{name}/addons -type f -size +0 -exec awk 'NR == 1 && /^#!.*python/ { exit } { exit 1 }' {} \; -print0 | xargs -0 sed -i "s|env python3|python3|g"
# Remove duplicate files
%fdupes -s %{buildroot}%{_datadir}/%{name}/platforms

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
