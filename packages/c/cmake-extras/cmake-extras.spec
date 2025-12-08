#
# spec file for package cmake-extras
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           cmake-extras
Version:        1.9
Release:        0
Summary:        A collection of add-ons for the CMake build tool
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://gitlab.com/ubports/development/core/cmake-extras
Source:         https://gitlab.com/ubports/development/core/cmake-extras/-/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE hillwood@opensuse.org fix-filename-and-path-of-qmlplugindump.patch
Patch:          fix-filename-and-path-of-qmlplugindump.patch
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcovr
BuildRequires:  gettext
BuildRequires:  gmock
BuildRequires:  intltool
BuildRequires:  lcov
BuildRequires:  llvm-gold
BuildRequires:  pkg-config
BuildRequires:  qmlpluginexports-qt5
BuildRequires:  vala
# BuildRequires:  licensecheck
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
Requires:       clang
Requires:       cmake
Requires:       doxygen
Requires:       gcovr
Requires:       gettext
Requires:       gmock
Requires:       intltool
Requires:       lcov
Requires:       llvm-gold
Requires:       pkg-config
Requires:       qmlpluginexports-qt5
Requires:       vala
Requires:       pkgconfig(gio-2.0)
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(gobject-introspection-1.0)
BuildArch:      noarch

%description
A collection of add-ons for the CMake build tool.

%prep
%autosetup -p1
sed -i 's|/usr/bin/env python|/usr/bin/python3|g' src/IncludeChecker/include_checker.py
# rm -rf src/CopyrightTest examples/copyrighttest-demo

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md ChangeLog AUTHORS
%{_datadir}/cmake/*

%changelog
