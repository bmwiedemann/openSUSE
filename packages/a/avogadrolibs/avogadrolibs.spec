#
# spec file for package avogadrolibs
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


%if 0%{suse_version} >= 1550
%bcond_without spglib
%bcond_without python
%else
%bcond_with spglib
%bcond_with python
%endif

# Requires genXrdPattern
%bcond_with vtk

%define sonum 1
%define libname libAvogadro%{sonum}
%define molecules_rev b1e16c5dc6d15e72d30dd6c4fca31b2c12025efc
%define crystals_rev  4b39c77ec1043cfb7a73e7b5dd51e24d36a95c44
Name:           avogadrolibs
Version:        1.97.0
Release:        0
Summary:        Avogadro libraries for computational chemistry
License:        BSD-3-Clause
URL:            https://two.avogadro.cc/
Source0:        https://github.com/OpenChemistry/avogadrolibs/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/OpenChemistry/molecules/archive/%{molecules_rev}.tar.gz#/molecules-%{molecules_rev}.tar.gz
Source2:        https://github.com/OpenChemistry/crystals/archive/%{crystals_rev}.tar.gz#/crystals-%{crystals_rev}.tar.gz
# PATCH-FIX-UPSTREAM not-install-gwavi.patch -- Library only used locally so no need to install this helper
Patch0:         not-install-gwavi.patch
# PATCH-FIX-UPSTREAM
Patch1:         https://github.com/OpenChemistry/avogadrolibs/commit/e48e67b85aae1f694b1d8c63b844bf8846006aae.patch#/Fix_qtplugins_surfaces_linking.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Avoid-ambigous-definition-of-mmtf-s-is_polymer.patch
BuildRequires:  cmake >= 3.3
BuildRequires:  eigen3-devel >= 2.91.0
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  libqt5-linguist-devel
BuildRequires:  mmtf-cpp-devel
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(libmsym) >= 0.2.0
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(zlib)
%if %{with python}
BuildRequires:  python3-devel
BuildRequires:  python3-pybind11-devel
%endif
%if %{with spglib}
BuildRequires:  spglib-devel
%endif
%if 0%{?suse_version} <= 1500
BuildRequires:  pkgconfig(glu)
%endif
%if %{with vtk}
BuildRequires:  genXrdPattern
BuildRequires:  cmake(vtk)
%endif

%description
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular
modeling, bioinformatics, materials science, and related areas.

%package -n %{libname}
Summary:        Avogadro libraries for computational chemistry
Recommends:     avogadro2-data >= %{version}
Recommends:     %{name}-plugins >= %{version}

%description -n %{libname}
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular
modeling, bioinformatics, materials science, and related areas.

%package plugins
Summary:        Plugins for Avogadro2libs

%description plugins
This package contains the vendor provided plugins for Avogadro2

%package -n avogadro2-data
Summary:        Data files for Avogadro2 and Avogadro2libs
BuildArch:      noarch

%description -n avogadro2-data
This package contains:
  * Crystallographic files of common materials, elements, oxides, for visualization in Avogadro.
  * Common molecule fragments for visualization in Avogadro

%package devel
Summary:        Header files for Avogadro libraries
Requires:       %{libname} = %{version}
Requires:       %{name}-plugins = %{version}
Requires:       cmake(MoleQueue)
Requires:       cmake(Qt5Network)
Requires:       cmake(Qt5Widgets)
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glew)
%if 0%{?suse_version} <= 1500
Requires:       pkgconfig(glu)
%endif

%description devel
Header files for Avogadro libraries.

%if %{with python}
%package -n python3-avogadro
Summary:        Python bindings for Avogadro libraries

%description -n python3-avogadro
Avogadro libraries provide 3D rendering, visualization, analysis
and data processing useful in computational chemistry, molecular
modeling, bioinformatics, materials science, and related areas.
%endif

%prep
%setup -q -b 1 -b 2
%autopatch -p1
[ -e ../crystals ] && rm -rfv ../crystals; mv ../crystals-%{crystals_rev} ../crystals
[ -e ../molecules ] && rm -rfv ../molecules; mv ../molecules-%{molecules_rev} ../molecules
%ifarch aarch64 %{arm}
# Workaround for Qt GLES builds on ARM, until overlayaxes fixed upstream - https://github.com/OpenChemistry/avogadrolibs/issues/810
# Type of function prototypes differ between GLEW and GLES
sed -i 's/add_subdirectory(overlayaxes)//' avogadro/qtplugins/CMakeLists.txt
%endif

%build
%cmake \
  -DINSTALL_DOC_DIR:PATH=%{_defaultdocdir} \
  -DBUILD_STATIC_PLUGINS:BOOL=OFF \
  -DENABLE_TRANSLATIONS:BOOL=ON \
  -DUSE_MOLEQUEUE:BOOL=ON \
  -DUSE_LIBMSYM:BOOL=ON \
  -DUSE_MMTF:BOOL=ON \
  -DUSE_HDF5:BOOL=ON \
  -DUSE_QT:BOOL=ON \
  -DUSE_VTK:BOOL=%{?with_vtk:ON}%{!?with_vtk:OFF} \
  -DUSE_PYTHON:BOOL=%{?with_python:ON}%{!?with_python:OFF} \
  -DUSE_SPGLIB:BOOL=%{?with_spglib:ON}%{!?with_spglib:OFF} \
  -DOpenGL_GL_PREFERENCE=GLVND \
  %{nil}
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_defaultdocdir}/avogadrolibs/LICENSE
%fdupes %{buildroot}%{_datadir}

%if %{with python}
# Fixup install location
mkdir -p %{buildroot}%{python3_sitearch}
mv %{buildroot}%{_libdir}/avogadro %{buildroot}%{python3_sitearch}/avogadro
%endif

sed -i -e '1 s@^@#!/usr/bin/python3\n@' \
  %{buildroot}%{_libdir}/avogadro2/scripts/charges/*.py \
  %{buildroot}%{_libdir}/avogadro2/scripts/formatScripts/zyx.py

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%{_libdir}/libAvogadro*.so.%{sonum}*

%files plugins
%dir %{_libdir}/avogadro2
%{_libdir}/avogadro2/{plugins,scripts}

%files devel
%dir %{_defaultdocdir}/avogadrolibs
%doc %{_defaultdocdir}/avogadrolibs/*.md
%{_includedir}/avogadro/
%{_libdir}/libAvogadro*.so
%{_libdir}/cmake/*

%files -n avogadro2-data
%dir %{_datadir}/avogadro2
%{_datadir}/avogadro2/crystals
%{_datadir}/avogadro2/molecules

%if %{with python}
%files -n python3-avogadro
%{python3_sitearch}/avogadro
%endif

%changelog
