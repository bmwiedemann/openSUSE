#
# spec file for package AppCSXCAD
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


Name:           AppCSXCAD
Version:        0.2.2
Release:        0
Summary:        Minimal GUI Application using the QCSXCAD library
License:        GPL-3.0-only
Group:          Productivity/Scientific/Other
URL:            https://openems.de
Source0:        https://github.com/thliebig/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         qt5_use_modules.diff
# PATCH-FIX-OPENSUSE
Patch1:         AppCSXCAD-vtk.patch
BuildRequires:  CSXCAD-devel
BuildRequires:  QCSXCAD-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  tinyxml-devel
BuildRequires:  vtk-devel
BuildRequires:  vtk-qt
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xt)

%description
Minimal GUI Application using the QCSXCAD library.

%prep
%autosetup -p1

%build
%cmake

%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README
%{_bindir}/*

%changelog
