#
# spec file for package QCSXCAD
#
# Copyright (c) 2022 SUSE LLC
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
Version:        0.6.2
Release:        0
%define so_ver  0
%define libname lib%{name}%{so_ver}
Summary:        Qt-GUI for CSXCAD library
License:        LGPL-3.0-or-later
Group:          Productivity/Graphics/CAD
URL:            https://openems.de
Source0:        https://github.com/thliebig/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE qt5_use_modules.diff -- qt5_use_modules has been deprecated and removed
Patch0:         qt5_use_modules.diff
# PATCH-FIX-OPENSUSE QCSXCAD-no-build-date.patch -- Remove build date from binaries
Patch1:         QCSXCAD-no-build-date.patch
# PATCH-FIX-OPENSUSE QCSXCAD-vtk.patch -- Avoid pulling in unneeded VTK modules
Patch2:         QCSXCAD-vtk.patch
# PATCH-FIX-UPSTREAM
Patch3:         0001-vtk-use-QVTKOpenGLWidget-for-vtk-8.patch
# PATCH-FIX-UPSTREAM
Patch4:         0001-vtk-fix-changes-for-vtk-8.x.patch
# PATCH-FIX-UPSTREAM
Patch5:         0001-Remove-leftover-QVTKWidget-include-fix-for-VTK-9.patch
# PATCH-FIX-UPSTREAM
Patch6:         0001-Fixup-includes-for-VTK-9.1-compatibility.patch
# PATCH-FIX-UPSTREAM
Patch7:         0001-Add-method-to-get-vtkRenderWindow-from-QVTKStructure.patch
BuildRequires:  CSXCAD-devel
BuildRequires:  cmake
BuildRequires:  double-conversion-devel
BuildRequires:  glew-devel
BuildRequires:  lzma-devel
BuildRequires:  tinyxml-devel
BuildRequires:  vtk-devel
BuildRequires:  vtk-qt
BuildRequires:  cmake(Qt5Sql)
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
