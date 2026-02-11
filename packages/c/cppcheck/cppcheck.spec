#
# spec file for package cppcheck
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


%if 0%{?suse_version} >= 1600
%bcond_with rules
%else
%bcond_without rules
%endif
%{?sle15_python_module_pythons}
%if 0%{?suse_version} == 1500
%define pyver python311
%define pyexecutable python3.11
%else
# latest
%define pyver python3
%define pyexecutable python3
%endif
Name:           cppcheck
Version:        2.19.0
Release:        0
Summary:        A tool for static C/C++ code analysis
License:        GPL-3.0-or-later
URL:            https://github.com/danmar/cppcheck
Source:         https://github.com/danmar/cppcheck/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  chrpath
BuildRequires:  cmake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  %{pyver}-base >= 3.7
BuildRequires:  xsltproc
BuildRequires:  z3-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Help)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
%if %{with rules}
BuildRequires:  pkgconfig(libpcre)
%endif
ExcludeArch:    %ix86 %arm
Requires:       %{pyver}-Pygments

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
sed -i 's#/usr/share/sgml/docbook/stylesheet/xsl/nwalsh/manpages/docbook.xsl#%{_datadir}/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl#' man/CMakeLists.txt

%cmake_qt6 \
  -DCMAKE_CXX_FLAGS="%{optflags} -UNDEBUG" \
  -DFILESDIR="%{_datadir}/%{name}" \
  -DBUILD_GUI=ON \
  -DBUILD_TESTS=ON \
%if %{with rules}
  -DHAVE_RULES=ON \
%else
  -DHAVE_RULES=OFF \
%endif
  -DUSE_Z3=yes \
  -DBUILD_MANPAGE=ON

%qt6_build

cmake --build %{__qt6_builddir} -t man

# use python3 as interpreter
sed -i "s|env python3|%{pyexecutable}|g" htmlreport/cppcheck-htmlreport

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
install -Dpm 0644 build/man/cppcheck.1 \
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
find %{buildroot}%{_datadir}/%{name}/addons -type f -size +0 -exec awk 'NR == 1 && /^#!.*python/ { exit } { exit 1 }' {} \; -print0 | xargs -0 sed -i "s|env python3|%{pyexecutable}|g"
#Cleanup rpath references
chrpath --delete %{buildroot}%{_bindir}/cppcheck
chrpath --delete %{buildroot}%{_bindir}/cppcheck-gui
# Remove duplicate files
%fdupes %{buildroot}%{_datadir}/%{name}/platforms

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
