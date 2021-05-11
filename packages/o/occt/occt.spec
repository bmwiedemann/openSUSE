#
# spec file for package occt
#
# Copyright (c) 2021 SUSE LLC
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


Name:           occt
Version:        7.5.1
Release:        0
%define soname 7
Summary:        OpenCASCADE Official Edition
License:        LGPL-2.1-only WITH OCCT-exception-1.0
Group:          Productivity/Graphics/CAD
URL:            https://www.opencascade.com/open-cascade-technology/
# Password protected URL, factory validation will fail
# https://www.opencascade.com/sites/default/files/private/occt/OCC_%%{version}_release/opencascade-%%{version}.tgz
# getting it from git for patch level releases not existing as tar ball
Source0:        occt-%{version}.tar.xz
Patch1:         fix_build.patch
# PATCH-FIX-UPSTREAM - https://gitlab.com/blobfish/occt/-/commit/ad0ba55f55b36dc957f66192c4766ace83f82b7e
Patch2:         0001-Add-error-checking-to-chamfer-and-fillet-code.patch
Provides:       OpenCASCADE = %{version}
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  mathjax
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  pkgconfig(RapidJSON)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xmu)

%description
OpenCASCADE is a suite for 3D surface and solid modeling, visualization, data
exchange and rapid application development. It is an excellent platform for
development of numerical simulation software including CAD/CAM/CAE, AEC and
GIS, as well as PDM applications.

%package resources
Summary:        Binary resource files for %{name}
Group:          System/Libraries
BuildArch:      noarch

%description resources
This package contains resource files imported from the libraries.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Provides:       OpenCASCADE-devel = %{version}
Requires:       libopencascade%{soname} = %{version}
Requires:       tcl-devel
Requires:       tk-devel
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xmu)
Conflicts:      oce-devel

%description devel
This package contains the files needed for development with OpenCASCADE.

%package devel-doc
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description devel-doc
Developer documentation for OpenCASCADE

%package -n libopencascade%{soname}
Summary:        OpenCASCADE libraries
Group:          System/Libraries
Requires:       %{name}-resources

%description -n libopencascade%{soname}
This package contain the needed libraries for OpenCASCADE

%package DRAWEXE
Summary:        Development files for %{name}
Group:          Productivity/Graphics/CAD
Conflicts:      oce-DRAWEXE

%description DRAWEXE
This package contains the DRAWEXE executable of OpenCASCADE.

%prep
%autosetup -p1

%build
%cmake \
  -DCMAKE_POLICY_DEFAULT_CMP0083=NEW \
  -DBUILD_RELEASE_DISABLE_EXCEPTIONS:BOOL=false \
  -DUSE_RAPIDJSON:BOOL=true \
  -DINSTALL_DIR_LIB=%{_lib} \
  -DINSTALL_DIR_CMAKE=%{_lib}/cmake/opencascade \
  ..
%cmake_build

cd ..
# Sidestep gendoc error (#32156) by adding -pdf option
./gendoc -refman -html -pdf -mathjax="%{_datadir}/javascript/mathjax"

%install
%cmake_install

# Make scripts executable
chmod 0755 %buildroot/usr/bin/*

# fixing up broken files
sed -i -e 's,'%{_lib}'\\${OCCT_INSTALL_BIN_LETTER}/,'%{_lib}'/,' %{buildroot}%{_libdir}/cmake/opencascade/*
sed -i -e 's,/lib\$,/'%{_lib}'\$,' %{buildroot}%{_libdir}/cmake/opencascade/*

rm -rf %buildroot/usr/share/doc

%fdupes -s %{buildroot}

%post -n libopencascade%{soname} -p /sbin/ldconfig

%postun -n libopencascade%{soname} -p /sbin/ldconfig

%files -n libopencascade%{soname}
%license LICENSE_LGPL_21.txt OCCT_LGPL_EXCEPTION.txt
%_libdir/lib*.so.%{soname}*

%files resources
%dir %{_datadir}/opencascade
%{_datadir}/opencascade/resources

%files DRAWEXE
%{_bindir}/custom*
%{_bindir}/draw.sh
%{_bindir}/env.sh
%{_bindir}/DRAWEXE*
%{_datadir}/opencascade/samples
%{_datadir}/opencascade/data

%files devel
%doc README.txt
%{_includedir}/opencascade
%dir %{_libdir}/cmake
%{_libdir}/cmake/opencascade
%{_libdir}/lib*.so

%files devel-doc
%doc doc/refman/html

%changelog
