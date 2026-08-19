#
# spec file for package QCSXCAD
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


Name:           QCSXCAD
Version:        0.6.3
Release:        0
%define so_ver  0
%define libname lib%{name}%{so_ver}
Summary:        Qt-GUI for CSXCAD library
License:        LGPL-3.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://openems.de
Source0:        https://github.com/thliebig/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         qcsxcad-cmp0020.patch
Patch2:         https://github.com/thliebig/QCSXCAD/commit/3c7b0d114063.patch#/fix_missing_std_ns_identifier.patch
BuildRequires:  CSXCAD-devel
BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  lzma-devel
BuildRequires:  tinyxml-devel
BuildRequires:  vtk-devel
BuildRequires:  vtk-qt
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xt)

%description
A Qt-GUI for the CSXCAD library.

%package -n     %{libname}
Summary:        Qt-GUI for CSXCAD library
Group:          System/Libraries

%description -n %{libname}
A Qt-GUI for the CSXCAD library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description    devel
A Qt-GUI for the CSXCAD library.

This package contains libraries and header files for developing
applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING
%doc NEWS README
%{_libdir}/lib%{name}.so.*

%files devel
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/

%changelog
